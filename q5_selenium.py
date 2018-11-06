#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
'''
for firefox driver  go to https://github.com/mozilla/geckodriver/releases  and put gekodriver on /urs/local/bin
'''


def save_html(html, file):
    with open(file, 'w') as file:
        file.write(html)


if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.get('http://casesearch.courts.state.md.us/casesearch/')
    html = browser.page_source.encode('utf-8')
    save_html(html, 'q5_selenium-1.html')
    # do the click and form submit
    browser.find_element_by_xpath("//input[@name='disclaimer']").click()
    browser.find_element_by_xpath("//input[@type='submit']").click()
    #  save the new response
    html = browser.page_source.encode('utf-8')
    save_html(html, 'q5_selenium-2.html')
