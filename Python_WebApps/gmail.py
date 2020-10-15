#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys

# Email Sender

def main():
	os.system('clear')

os.system('clear')
try:
    print('Email Sender')
except Exception:
	print('')

#Input
print( '''
Choose a Mail Service:
1) Gmail
2) Yahoo
3) Hotmail/Outlook
''' + '--------------------------------------------------------------')

server = raw_input('Mail Server: ')
user = raw_input('Your Email: ')
pwd = getpass.getpass('Password: ')
to = raw_input('To: ')
subject = raw_input('Subject (Optional): ')
body = raw_input('Message: ')

message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body

#Gmail
if server == '1' or server == 'gmail' or server == 'Gmail':
	main()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print('Your Username or Password is incorrect')
		sys.exit()

	try:
		server.sendmail(user, to, message)
		print('email sent')
		time.sleep(.8)
	except KeyboardInterrupt:
		print('Canceled')
		sys.exit()
	except:
		print "Failed to Send "
	server.close()
