import pyautogui
import ctypes
import sys
import PyWallpaper
import time

from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


def main():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "vlc.exe":
            print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
            volume.SetMasterVolume(100, None)

main()