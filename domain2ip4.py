#!/usr/bin/python

# Name:     domain2ip.py (With Request Method)
# Purpose:  Get IP from domain name
# By:       Chetan Soni
# Date:     06 Oct 2017
# ------------------------------------------------------------------
# Downloaded from GitHub page: https://github.com/yeahhub/domain2ip
# Author Website: http://www.yeahhub.com/
# ------------------------------------------------------------------

import requests
from termcolor import colored
print('\n')
name = raw_input("Enter website here (Ex: http://google.com): ") 
print colored("===========================================================", 'green')
try:
    rsp=requests.get(name, stream=True)
    print rsp.raw._connection.sock.getpeername() 
except socket.gaierror:  
    print colored("Cannot resolve hostname", 'red')
    
    
    
