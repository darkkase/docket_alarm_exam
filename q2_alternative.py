#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import urllib2
'''
Write a program that prints the IP address of the computer that it
is being run on. If the computer is not connected to the internet, it should print "not connected"
'''


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    IP = s.getsockname()[0]
    s.close()
    return IP


try:
    response = urllib2.urlopen('https://api.ipify.org?format=json')  # if this  trow a exception then the computer dosent have internet
    print(get_ip())
except Exception as e:
    print 'not connected'
