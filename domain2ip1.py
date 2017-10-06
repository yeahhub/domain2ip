#!/usr/bin/python

# Name:     domain2ip.py (Without any Exception)
# Purpose:  Get IP from domain name
# By:       Chetan Soni
# Date:     07 Oct 2017
# ------------------------------------------------------------------
# Downloaded from GitHub page: https://github.com/yeahhub/domain2ip
# Author Website: http://www.yeahhub.com/
# ------------------------------------------------------------------

from socket import *

website=raw_input("Enter website here: ") 
output = gethostbyname(website)
print "Your Domain IP address is:" , output






