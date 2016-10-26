####################################################################
# samples is used to explain and for educational porpuse only !!!  #
# that sample and simple DLL injector is using handling process ,  #
# ( and there many ways ) to perform the injection in the targeted #
# process , so when it dosn't work for windows 7 , you should ask  #
# about your ability to handle a proccess in the mention way ...   #
####################################################################

#!/usr/bin/env python

import sys
from ctypes import * #to be able use C language types .. all of it 

print "#######################"
print "**sample DLL INJECTOR** "
print "#######################"

if len(sys.argv) < 3:
    print "Usage: %s <PID> <DLL's Path>" % (sys.argv[0])
    print "Ex : %s 1234 C:\\home\\yourdll.dll" % (sys.argv[0]) #the script will take PID and DLL path as a parameters ..
    sys.exit(0)

PAGE_READWRITE = 0x04 #set block of memory to read and write access
PROCESS_ALL_ACCESS = (0x00F000 | 0x0010000 | 0xFFF)  # set the access rights for a function 
VIRTUAL_MEM = (0x1000 | 0x2000) #set the virtual memory region 

kernel32 = windll.kernel32 #we use kernel32.dll , wich contain the nedded api functions .
PID = sys.argv[1]
dll_path = sys.argv[2]
dll_len = len(dll_path)

Hprocess = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, int(PID))

if not Hprocess:
    print "Unexcpected : Couldn't get handle to PID: %s" % PID
    print "are you proved a valid process id !"
    sys.exit(0)

al_address = kernel32.VirtualAllocEx(Hprocess, 0, dll_len, VIRTUAL_MEM, PAGE_READWRITE)

WriteToMem = c_int(0)
kernel32.WriteProcessMemory(Hprocess, al_address, dll_path, WriteToMem)

Hkernel32 = kernel32.GetModuleHandleA("kernel32.dll")
Hloadlib = kernel32.GetprocAddress(Hkernel32, "LoadLibraryA")

Thread_Id = c_ulong(0)

if not kernel32.CreateRemoteThread(Hprocess, None, 0, Hloadlib, al_address, 0, byref(Thread_Id)):
    print "[Oops] Failed to inject DLL, exit ..."
    sys.exit(0)

print "[Hah] Remote Thread with ID 0x%08x created." % Thread_Id.value
