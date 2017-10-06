#!/usr/bin/python

# Name:     domain2ip.py (For python3)
# Purpose:  Get IP from domain name
# By:       Chetan Soni
# Date:     06 Oct 2017
# ------------------------------------------------------------------
# Downloaded from GitHub page: https://github.com/yeahhub/domain2ip
# Author Website: http://www.yeahhub.com/
# ------------------------------------------------------------------

from socket import gethostbyname
print('\n')
name = str(input('Enter website here: '))
print('\n')
try:
    host = gethostbyname(name)
    print ("Your Domain IP address is:" , host)
except:  
    print ("Cannot resolve hostname")
    
    
    
    
    
