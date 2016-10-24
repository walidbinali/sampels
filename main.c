#include <stdio.h>
#include <windows.h>

int main(int argc, char* argv[])
{
  char* buffer = "C:\\Windows\\System32\\test.dll" ;

  int procID;

  printf("Enter process ID of the targeted process: ");
  scanf(&procID) ;
  printf(procID);


  /* HANDLE process = OpenProcess(PROCESS_ALL_ACCESS ,FALSE ,procID) ;
  if(process == NULL){
    printf("Error: the specified process couldn't be found.\n") ;
  }

  LPVOID addr = (LPVOID)GetProcAddress(GetModuleHandle(L"kernel32.dll"), "LoadLibraryA") ;
  if(addr == NULL){
    printf("Error: the LoadlLibraryA function was not found inside kernel32.dll library.\n") ;
    }

  LPVOID arg = (LPVOID)VirtualAllocEx(process, NULL, strlen(buffer), MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE) ;
  if(arg == NULL){
    printf("Error : the memory could not be allocated inside the chosen process.\n");
  }

  int n = WriteProcessMemory(process, arg,buffer, strlen(buffer),NULL);
  if(n == 0){
    printf("Error: there was no bytes written to the process's address space.\n") ;
  }

  HANDLE threadID = CreateRemoteThread(process, NULL, 0,(LPTHREAD_START_ROUTINE)addr, arg, NULL, NULL);
  if(threadID == NULL){
    printf("Error: the remote thread could not be created.\n");
  }

  else{
    printf("the remote thread was successfully created..") ;
  }

  CloseHandle(process);

  getchar();*/
  return 0;
}
