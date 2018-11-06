#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
List the libraries or framework you have used creating a python web crawler. In 200 words or
less, describe the working flow.
    anwer:  scrapy, request, selenium, beautifulsoup4, re.
        1) check the web  to scraping
        2) define the data to extracting
        3) write a code for get the web (with scrapy, request, urllib2) and extract the data (with beautifulsoup scrapy, re)
        4) save the data

Explain difference between python list and tuple.
    answer:  tuple is a immutable list of elements,  list is a list of mutable elements.

'''


'''
Write a program that prints numbers from 1 to 1000 on each line. But for numbers that are
multiples of 7 print "Docket" instead of the number. For multiples of 6 print "Alarm" instead
of the number. For numbers that are multiples of both 6 and 7 print "Docket Alarm".
'''

print('1 to 1000 with range\n\n')
for x in range(1, 1001):
    if (x % 7 == 0) and (x % 6 == 0):
        print x, 'Docket Alarm'
    elif x % 7 == 0:
        print x, 'Docket'
    elif x % 6 == 0:
        print x, 'Alarm'
    else:
        print x


'''
-----------------------
Explain what a Python generator is. Modify the answer to part “c” to utilize a generator.
    answer: a generator is a function for create the next item in a sequence without overcharge all items in ram
'''
print('\n\n1 to 1000 with xrange (the generator of python)\n\n')
for x in xrange(1, 1001):
    if (x % 7 == 0) and (x % 6 == 0):
        print x, 'Docket Alarm'
    elif x % 7 == 0:
        print x, 'Docket'
    elif x % 6 == 0:
        print x, 'Alarm'
    else:
        print x


'''
----------------------
plus: custom generator
'''


class custom_range(object):
    '''
        generator for consecutive numbers
    '''

    def __init__(self, x, y, z=1):
        '''
            x: start
            y: end
            z: intervals
        '''
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        return self

    def next(self):
        if self.x < self.y:
            now = self.x
            self.x += self.z
            return now
        else:
            raise StopIteration()


print('\n\n1 to 1000 with custom_range (my custom generator  python)\n\n')
for x in custom_range(1, 1001):
    if (x % 7 == 0) and (x % 6 == 0):
        print x, 'Docket Alarm'
    elif x % 7 == 0:
        print x, 'Docket'
    elif x % 6 == 0:
        print x, 'Alarm'
    else:
        print x
