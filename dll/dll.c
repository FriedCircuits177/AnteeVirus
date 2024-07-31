#include <windows.h>

BOOL WINAPI
DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved)
{
    switch (dwReason)
    {
        case DLL_PROCESS_ATTACH:
            MessageBox(NULL, //Owner
                      "Please subscribe to INgo Poretra iskandr", //Message
                      "ippsec", //Title
                      MB_ICONERROR | MB_OK //TYPE
                      );
            break;
    }
return TRUE;
}