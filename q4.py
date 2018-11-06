#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import json
from time import sleep
'''
a. Build on top of the previous answer to create a program that downloads 50 cases
sequentially. Note the form of the URL, to scan through caseids 23800 to 23850.
b. Output the result into a JSON format into a file named q4.json. The JSON format should be a
list, where each list item is in the same form of the JSON object you created in question 3.
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


def save_json(j, file):
    with open(file + '.json', 'w') as f:
        json.dump(j, f)


# main script
if __name__ == '__main__':
    url = 'https://eapps.courts.state.va.us/cav-public/caseInquiry/showCasePublicInquiry?caseId='
    list_data = []
    for caseId in xrange(23800, 23851):
        print(caseId)
        response = requests.get(url + str(caseId))
        soup = response.soup
        appellants = soup.find(id='listAllPartiesAPL')
        appellant_names = [item('td')[0].text for item in appellants('tr')]  # i assume that could be more than one appellant
        cav_record_number = soup.find('input', {'name': 'caseNumber'}).get('value')
        cav_received = soup.find('input', {'name': 'noticeOfAplDt'}).get('value')
        data = {
            'caseId': caseId,
            'appellants': appellant_names,
            'cav_record_number': cav_record_number,
            'date_received': cav_received,
        }
        list_data.append(data)
        print(list_data)
        sleep(0.5)  # the server looks really old, i don't want to saturate it
    save_json(list_data, 'q4')
