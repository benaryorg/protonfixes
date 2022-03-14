""" Game fix for FFXIV
"""
#pylint: disable=C0103

from protonfixes import util
import os

def main():
    """ FFXIV add NOSTEAM option.
    """
    # Fixes the startup process.
    if 'NOSTEAM' in os.environ:
        util.replace_command('-issteam', '')
    
    # Runs XIVLauncher instead of Stock Launcher
    if 'XL_WINEONLINUX' in os.environ:
        util.protontricks_proton_5('dotnet48')
        util.protontricks('vcrun2019')
        util.replace_command('common/FINAL FANTASY XIV Online/boot/ffxivboot.exe', 'compatdata/39210/pfx/drive_c/users/steamuser/AppData/Local/XIVLauncher/XIVLauncher.exe')
        util.replace_command('-issteam', '')
