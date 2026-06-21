import xbmcaddon
import os

SETTINGS = xbmcaddon.Addon('osmc.xtrasuspend')
ethersus = SETTINGS.getSetting('ether')
wifisus = SETTINGS.getSetting('wifi')
btsus = SETTINGS.getSetting('bt')
sesfile = '/home/osmc/.kodi/userdata/previussession.txt'

# open with "w" truncates the file if it already exists
f = open(sesfile, "w")

if ethersus:
    f.write("ethernet\n")
    os.system('sudo connmanctl disable ethernet')

if wifisus:
    f.write("wifi\n")
    os.system('sudo connmanctl disable wifi')   # fix: indentation (was tab)

if btsus:
    f.write("bt\n")
    os.system('sudo connmanctl disable bluetooth')  # fix: indentation (was tab)

f.close()