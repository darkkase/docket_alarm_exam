#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from urllib import urlencode
from BeautifulSoup import BeautifulSoup

'''
a. Create a program that downloads the page located here and saves it to the file q5-1.html.
b. Then have the program click the checkbox, and select continue, download the resulting case
search page and save it into a file named q5-2.html

    well, this is not tecnically a click and submit, but this web dosen't have security. so i write  q5_selenium.py for trully click
'''


class Response(object):
    '''
        just a response class  used for the requests class
        for simulate the requests library :'(
    '''
    def __init__(self, response):
        self.response = response

    @property
    def text(self):
        ''' return the html of the text '''
        return self.response.read()

    @property
    def soup(self):
        '''return  the beautifulsoup object'''
        return BeautifulSoup(self.text)


class requests(object):

    @classmethod
    def get(cls, url, data=None):
        '''get the url'''
        if data:
            response = urllib2.urlopen(url, urlencode(data))
        else:
            response = urllib2.urlopen(url)
        return Response(response)

    @classmethod
    def post(cls, url, data):
        '''post to a url'''
        return cls.get(url, data)


def save_html(html, file):
    with open(file, 'w') as file:
        file.write(html)


if __name__ == '__main__':
    url = 'http://casesearch.courts.state.md.us/casesearch/'
    response = requests.get(url)
    save_html(response.text, 'q5-1.html')
    soup = response.soup
    response = requests.post(url + 'processDisclaimer.jis', {'disclaimer': 'Y'})
    save_html(response.text, 'q5-2.html')
