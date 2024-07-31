#include <windows.h>
#include <stdio.h>

int main(void){
    HINSTANCE hDll;

    //Load a DLL
    hDll = LoadLibrary(TEXT("dll.dll"));

    //if DLL was loaded
    if (hDll != NULL){
        printf("Dll Found\n");
    } else {
        printf("DLL Not Found");
    }

    return 0;
}