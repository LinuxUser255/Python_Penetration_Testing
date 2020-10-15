#!/usr/bin/python3


import socket
import os
import signal
import time
import threading
import sys
import subprocess
from queue import Queue
from datetime import datetime

# Start Thread Ripper with clear terminal


subprocess.call('clear', shell=True)

# Define the Main Function
def main():
    socket.setdefaulttimeout(0.30)
    print_lock = threading.Lock()
    discovered_ports = []

# Print/display the Welcome Banner
    print("-" * 60)
    print("        Thread Ripper, a Multi-threaded Port Scanner          ")
    print("                                       ")
    print("                        ")
    print("-" * 60)
    
    time.sleep(1)
    target = input("Enter your target IP address or URL here: ")
    error = ("Invalid Input")
    
    # Use try-except block for socket
    try:
        t_ip = socket.gethostbyname(target)
    except (UnboundLocalError, socket.gaierror):
        print("\n[-]Invalid format. Please use a correct IP or web address[-]\n")
        sys.exit()
    
    # Banner
    print("-" * 60)
    print("Scanning target "+ t_ip)
    print("Time started: "+ str(datetime.now()))
    print("-" * 60)
    t1 = datetime.now()

    # Create a port scan function using try: with except pass
    def portscan(port):
        
       # Use Classic socket object
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
       # Attempt making a connection and use the try with exept pass block
       try:
          conx = s.connect((t_ip, port))
          with print_lock:
             print("Port {} is open".format(port))
             discovered_ports.append(str(port))
          conx.close()

       except (ConnectionRefusedError, AttributeError, OSError):
          pass

    # Define the threader function and create a while loop for worker
    def threader():
       while True:
          worker = q.get()
          portscan(worker)
          q.task_done()
      
    # Set the Queue
    q = Queue()
     
    #startTime = time.time()
    
    #For x in range
    for x in range(200):
       t = threading.Thread(target = threader)
       t.daemon = True
       t.start()

    # For worker in range including all ports 1 - 65536
    # And join the worker
    for worker in range(1, 65536):
       q.put(worker)

    q.join()

# Recommend nmap scans. Set datetime 
    t2 = datetime.now()
    total = t2 - t1
    print("Port scan completed in "+str(total))
    print("-" * 60)
    print("Thread Ripper recommends the following Nmap scan:")
    print("*" * 60)
    print("nmap -p{ports} -sV -sC -T4 -Pn -oA {ip} {ip}".format(ports=",".join(discovered_ports), ip=target))
    print("*" * 60)
    outfile = "nmap -p{ports} -sV -sC -Pn -T4 -oA {ip} {ip}".format(ports=",".join(discovered_ports), ip=target)
    t3 = datetime.now()
    total1 = t3 - t1

# Nmap Integration (in progress) 
# & define automation function
    def automate():
       choice = '0'
       while choice =='0':
          print("Would you like to run Nmap or quit to terminal?")
          print("-" * 60)
          print("1 = Run suggested Nmap scan")
          print("2 = Run another Thread Ripper scan")
          print("3 = Exit to terminal")
          print("-" * 60)
          choice = input("Option Selection: ")
          if choice == "1":
             try:
                print(outfile)
                os.mkdir(target)
                os.chdir(target)
                os.system(outfile)
                #The xsltproc is experimental and 
                #will convert XML to a HTML readable format; requires xsltproc on your machine to work
                #convert = "xsltproc "+target+".xml -o "+target+".html"
                #os.system(convert)
                t3 = datetime.now()
                total1 = t3 - t1
                print("-" * 60)
                print("Combined scan completed in "+str(total1))
                print("Press enter to quit...")
                input()
             except FileExistsError as e:
                print(e)
                exit()
          elif choice =="2":
             main()
          elif choice =="3":
             sys.exit()
          else:
             print("Please make a valid selection")
             automate()
    automate()
# name and main
# ANd call the main function usinf try-except block. The ecept will be a keyboard interrupt
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram exited.")
        quit()#!/usr/bin/python
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
