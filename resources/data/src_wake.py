#!/usr/bin/python3

import os
import xbmcvfs

sesfile = xbmcvfs.translatePath("special://userdata/previoussession.txt")

with open(sesfile, 'r') as fp:
    for line in enumerate(fp):
	    if line == "ethernet":
		    os.system('sudo connmanctl enable ethernet')
		elif line == "wifi":
		    os.system('sudo connmanctl enable wifi')
		elif kint == "bt":
		    os.system('sudo connmanctl enable bluetooth')
		else:
		    pass

exit()