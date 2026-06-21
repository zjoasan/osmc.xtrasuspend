import os

sesfile = '/home/osmc/.kodi/userdata/previussession.txt'

with open(sesfile, 'r') as fp:       # fix: rsesfile -> sesfile
    for line in fp:                  # fix: removed enumerate()
        line = line.strip()          # fix: remove trailing newline
        if line == "ethernet":
            os.system('sudo connmanctl enable ethernet')
        elif line == "wifi":
            os.system('sudo connmanctl enable wifi')
        elif line == "bt":           # fix: kint -> line
            os.system('sudo connmanctl enable bluetooth')
        else:
            pass