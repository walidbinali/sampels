#!/usr/bin/env python

import sys
import ctypes

print "#######################"
print "**sample DLL INJECTOR** "
print "#######################"

if len(sys.argv) < 3:
    print "Usage: %s <PID> <DLL's Path>" % (sys.argv[0])
    print "Ex : %s 1234 C:\\home\\yourdll.dll" % (sys.argv[0])
    sys.exit(0)

PAGE_READWRITE = 0x04
PROCESS_ALL_ACCESS = (0x00F000 | 0x0010000 | 0xFFF)
VIRTUAL_MEM = (0x1000 | 0x2000)

kernel32 = ctypes.windll.kernel32
PID = sys.argv[1]
dll_path = sys.argv[2]
dll_len = len(dll_path)

Hprocess = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, int(PID))

if not Hprocess:
    print "Unexcpected : Couldn't get handle to PID: %s" % PID
    print "are you proved a valid process id !"
    sys.exit(0)

al_address = kernel32.VirtualAllocEx(Hprocess, 0, dll_len, VIRTUAL_MEM, PAGE_READWRITE)

WriteToMem = ctypes.c_int(0)
kernel32.WriteProcessMemory(Hprocess, al_address, dll_path, WriteToMem)

Hkernel32 = kernel32.GetModuleHandleA("kernel32.dll")
Hloadlib = kernel32.GetprocAddress(Hkernel32, "LoadLibraryA")

Thread_Id = ctypes.c_ulong(0)

if not kernel32.CreateRemoteThread(Hprocess, None, 0, Hloadlib, al_address, 0, ctypes.byref(Thread_Id)):
    print "[Oops] Failed to inject DLL, exit ..."
    sys.exit(0)

print "[Hah] Remote Thread with ID 0x%08x created." % Thread_Id.value
