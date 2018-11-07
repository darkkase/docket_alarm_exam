#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import json
'''
a. Write a scraper which can download and parse the page here
b. The program should output the Appellant name, Appellee name, CAV record number, and
date received. The format should be in JSON and saved to a filename q3.json. The exact
format of the JSON file is not important.
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
        return BeautifulSoup(self.text, 'html.parser')


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


def save_json(j, file):
    with open(file + '.json', 'w') as f:
        json.dump(j, f)


# main script
if __name__ == '__main__':
    url = 'https://eapps.courts.state.va.us/cav-public/caseInquiry/showCasePublicInquiry?caseId=23811'
    response = requests.get(url)
    soup = response.soup
    appellants = soup.find(id='listAllPartiesAPL')
    appellant_names = [item('td')[0].text.strip() for item in appellants('tr')]  # i assume that could be more than one appellant
    cav_record_number = soup.find('input', {'name': 'caseNumber'}).get('value').strip()
    cav_received = soup.find('input', {'name': 'noticeOfAplDt'}).get('value').strip()
    data = {
        'appellants': appellant_names,
        'cav_record_number': cav_record_number,
        'date_received': cav_received,
    }
    save_json(data, 'q3')
