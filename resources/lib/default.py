import xbmcaddon
import xbmcgui
import os
import shutil

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
ahome = addon.getAddonInfo('path')
srcw_path = ahome + '/resources/data/src_wake.py'
srcb_path = ahome + '/resources/data/src_standby.py'
bu_wake_path = ahome + '/resources/data/backup/bu_wake.py'
bu_sb_path = ahome + '/resources/data/backup/bu_standby.py'  # fix: backu -> backup
destw_path = '/home/osmc/.kodi/userdata/wake.py'
destsb_path = '/home/osmc/.kodi/userdata/standby.py'
runopath = ahome + '/resources/data/runonce.txt'

check_runofile = os.path.isfile(runopath)  # fix: ropath -> runopath
if not check_runofile:
    with open(runopath, "x"):
        pass

    check_wakefile = os.path.isfile(destw_path)
    if check_wakefile:
        shutil.move(destw_path, bu_wake_path)

    check_sbfile = os.path.isfile(destsb_path)
    if check_sbfile:
        shutil.move(destsb_path, bu_sb_path)

    shutil.copyfile(srcw_path, destw_path)
    shutil.copyfile(srcb_path, destsb_path)  # fix: srcsb_path -> srcb_path

else:
    check_wake_bu = os.path.isfile(bu_wake_path)
    check_sb_bu = os.path.isfile(bu_sb_path)

    restore_w = False   # fix: initialize before conditionals
    restore_sb = False  # fix: initialize before conditionals

    if check_wake_bu:
        restore_w = True   # fix: TRUE -> True

    if check_sb_bu:        # fix: check_sb_path -> check_sb_bu
        restore_sb = True  # fix: TRUE -> True

    rest_choice = xbmcgui.Dialog().yesno(addonname, "Restore old wake/standby scripts?")
    if rest_choice:
        if restore_w:
            os.remove(destw_path)
            shutil.copyfile(bu_wake_path, destw_path)
        if restore_sb:
            os.remove(destsb_path)
            shutil.copyfile(bu_sb_path, destsb_path)

    else:
        del_choice = xbmcgui.Dialog().yesno(addonname, "Remove wake/standby scripts?")
        if del_choice:
            os.remove(destw_path)
            os.remove(destsb_path)  # fix: indentation aligned

xbmcaddon.Addon().openSettings()
xbmcgui.Dialog().ok(addonname, "Suspend extras configured")