import ctypes
from ctypes import wintypes
import threading

def keyboard_hookproc(nCode, wParam, lParam):
    if nCode == 0 and wParam == 0x11 and ctypes.windll.user32.GetAsyncKeyState(0x11) < 0 and ctypes.windll.user32.GetAsyncKeyState(0x12) < 0:
        return 1
    return ctypes.windll.user32.CallNextHookEx(None, nCode, wParam, lParam)

keyboard_hookproc_cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)
keyboard_hookproc_ptr = keyboard_hookproc_cb(keyboard_hookproc)

def install_hook():
    hook = ctypes.windll.user32.SetWindowsHookExW(13, keyboard_hookproc_ptr, None, 0)
    if hook == 0:
        raise ctypes.WinError()
    return hook

def pump_messages():
    msg = wintypes.MSG()
    while ctypes.windll.user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
        ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
        ctypes.windll.user32.DispatchMessageW(ctypes.byref(msg))

hook = install_hook()
thread = threading.Thread(target=pump_messages)
thread.start()

while True:
    pass