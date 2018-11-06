#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json

'''
Write a program that prints the IP address of the computer that it
is being run on. If the computer is not connected to the internet, it should print "not connected"

    i'm not sure if the problem is obtain the  computer ip or obtain the public ip.
    so i write this code for obtain the public ip
    and i write q2_alternative.py for the ip of the computer
'''


try:
    response = urllib2.urlopen('https://api.ipify.org?format=json')
except Exception as e:
    response = None

if response and response.getcode() == 200:
    html = response.read()
    j = json.loads(html)
    print(j['ip'])
else:
    print 'not connected'
