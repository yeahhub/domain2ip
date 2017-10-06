#!/usr/bin/python

# Name:     domain2ip.py (With Exception)
# Purpose:  Get IP from domain name
# By:       Chetan Soni
# Date:     06 Oct 2017
# ------------------------------------------------------------------
# Downloaded from GitHub page: https://github.com/yeahhub/domain2ip
# Author Website: http://www.yeahhub.com/
# ------------------------------------------------------------------

import socket

name = raw_input("Enter website here: ") 
try:
    host = socket.gethostbyname(name)
    print "Your Domain IP address is:" , host
except socket.gaierror, err:  
    print "Cannot resolve hostname: ", name, err
    
    
    
    
    
    
