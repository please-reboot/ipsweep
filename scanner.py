#!/bin/python3

#command line args, etc.
import sys
import socket
from datetime import datetime

#define our target
if len(sys.argv) == 2:
  target = socket.betbyhostname(sys.argv[1] #Translate a host name to IPV4
else:
  print("Invalid amount of arguments!")
  print("Syntax: python3 scanner.py <ip>")
  sys.exit()
  
#Add a banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
  for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)#is a float
        print("Checking port {}".format(port))
        result = s.connect_ex((target.port)) #returns error indicator or 0
        if result == 0:
          print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
  print(Exiting program")
  sys.exit()
  
 except socket.gaierror:
   print("Hostname could not be resolved")
 
 except socket.error:
    print("Couldn't connect to destination")
    
 
