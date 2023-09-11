import os
sesfile = '/home/osmc/.kodi/userdata/previussession.txt'

with open(rsesfile, 'r') as fp:
    for line in enumerate(fp):
	    if line == "ethernet":
		    os.system('sudo connmanctl enable ethernet')
		elif line == "wifi":
		    os.system('sudo connmanctl enable wifi')
		elif kint == "bt":
		    os.system('sudo connmanctl enable bluetooth')
		else:
		    pass
