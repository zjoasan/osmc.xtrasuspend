import xbmcaddon
import xbmcgui
import xbmcvfs
import os
import shutil

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
ahome = addon.getAddonInfo('path')
srcw_path = os.path.join(ahome, 'resources/data/src_wake.py')
srcsb_path = os.path.join(ahome, 'resources/data/src_standby.py')
bu_wake_path = os.path.join(ahome, 'resources/data/backup/bu_wake.py')
bu_sb_path = os.path.join(ahome, 'resources/data/backup/bu_standby.py')
destw_path = xbmcvfs.translatePath("special://userdata/wake.py")
destsb_path = xbmcvfs.translatePath("special://userdata/standby.py")
runopath = os.path.join(ahome + 'resources/data/runonce.txt')

check_runofile = os.path.isfile(runopath)
if not check_runofile:
    f = open(runopath, "x")

    check_wakefile = os.path.isfile(destw_path)
    if check_wakefile:
        shutil.move(destw_path, bu_wake_path)

    check_sbfile = os.path.isfile(destsb_path)
    if check_sbfile:
        shutil.move(destsb_path, bu_sb_path)

    shutil.copyfile(srcw_path, destw_path)
    shutil.copyfile(srcsb_path, destsb_path)

    xbmcaddon.Addon().openSettings()
    
else:
    check_wake_bu = os.path.isfile(bu_wake_path)
    check_sb_bu = os.path.isfile(bu_sb_path)

    if check_wake_bu:
        restore_w = TRUE
    
    if check_sb_bu:
        restore_sb = TRUE

    rest_choice = xbmcgui.Dialog().yesno(addonname, addon.getLocalizedString(32004))
    if rest_choice:
        if restore_w:
            os.remove(destw_path)
            shutil.copyfile(bu_wake_path, destw_path)
        if restore_sb:
            os.remove(destsb_path)
            shutil.copyfile(bu_sb_path, destsb_path)
         
    else:
        del_choice = xbmcgui.Dialog().yesno(addonname, addon.getLocalizedString(32005))    
        if del_choice:
           os.remove(destw_path)
           os.remove(destsb_path)

xbmcgui.Dialog().ok(addonname, addon.getLocalizedString(32006))
