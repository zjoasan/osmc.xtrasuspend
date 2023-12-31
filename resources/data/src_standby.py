#!/usr/bin/python3

import xbmcaddon
import os

SETTINGS = xbmcaddon.Addon('osmc.xtrasuspend')
ethersus = SETTINGS.getSetting('ether')
wifisus = SETTINGS.getSetting('wifi')
btsus = SETTINGS.getSetting('bt')
sesfile = xbmcvfs.translatePath("special://userdata/previoussession.txt")
os.system('rm -f %s' % sesfile)
f = open(sesfile, "w")

if ethersus:
    f.write("ethernet\n")    
    os.system('sudo connmanctl disable ethernet')

if wifisus:
    f.write("wifi\n")
    os.system('sudo connmanctl disable wifi')

if btsus:
    f.write("bt\n")
	os.system('sudo connmanctl disable bluetooth')

f.close()

exit()
