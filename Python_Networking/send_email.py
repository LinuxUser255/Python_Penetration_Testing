#!/usr/bin/env python3

#Sendmail must be installed prior to use.

import smtplib
import string
import os
import time

os.system("/etc/init.d/sendmail start")
time.sleep(4)

HOST = "localhost"
SUBJECT = "email from spoofed sender"
TO = "target@emal.com"
FROM = "spoof@email.com"
TEXT = "Message Body"
BODY = string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT ,
    "",
    TEXT
    ), "\R\N")
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()

time.sleep(4)
os.system("/etc/init.d/sendmail stop")

