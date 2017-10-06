#!/usr/bin/python

# Name:     domain2ip.py (With Socket Method & Colored Module)
# Purpose:  Get IP from domain name
# By:       Chetan Soni
# Date:     06 Oct 2017
# ------------------------------------------------------------------
# Downloaded from GitHub page: https://github.com/yeahhub/domain2ip
# Author Website: http://www.yeahhub.com/
# ------------------------------------------------------------------

import socket
from termcolor import colored
print('\n')
name = raw_input("Enter website here: ") 
print colored("===========================================", 'green')
try:
    host = socket.gethostbyname(name)
    print "Your Domain IP address is:" , colored(host, 'yellow')
    print('\n')
except socket.gaierror:  
    print colored("Cannot resolve hostname", 'red')
    
    
   
