from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ["random","os","subprocess","winreg","ctypes","sys","tkinter.messagebox","time","threading","playsound","pyautogui","PyWallpaper"], \
                 'excludes': ["tkinter.colorchooser","tkinter.filedialog","tkinter.font","tkinter.scrolledtext","tkinter.simpledialog","tkinter.ttk"],\
                'include_files':['black.png','b.wav'],\
                'include_msvcr':True}

base = 'gui'

executables = [
    Executable('main.py', base=base, target_name = 'AnteeVirus',uac_admin=True,uac_uiaccess=True)
]

setup(name='AnteeVirus',
      version = '0.1',
      description = 'Totally innocent normal horse',
      options = {'build_exe': build_options},
      executables = executables)
