#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
'''
a. You should have received the HTML files q6-1.html, q6-2.html, and q6-3.html
b. Open each HTML file in a web browser. After scrolling down, you should see an “Actions”
table, with headings “Viewed” and “Date”, among several others.
c. Create a program that opens each file and creates a corresponding file called q6-1.json, q6-
2.json, and q6-3.json, respectively.
d. Each JSON file should be a list of dictionaries, where each entry corresponds to the values in
the table. So for example, the first entry in q6-1.html should be:
'''


def extract_col_content(col):
    '''
    look in for a  link or image or both, if not just return the text inside the col
    '''
    if col.a:
        if col.a.img:
            img = col.a.img['src']
            return {'link': col.a['href'], 'img': img}
        else:
            text = col.a.text.strip().replace('&nbsp;', '')
            return {'link': col.a['href'], 'text': text}
    elif col.img:
        return col.img['src']
    elif col.text:
        return col.text.strip().replace('&nbsp;', '')
    else:
        return ''


def table_to_json(table):
    '''
    fist create a list of rows, and then convert the list in to a dict (using zip function), where the first row are the keys
    '''
    print(table)
    print(table('tr'))
    data_as_list = [[extract_col_content(col) for col in row("td")] for row in table("tr")]
    data = [dict(zip(data_as_list[0], items)) for items in data_as_list[1:]]
    return data


def save_json(j, file):
    with open(file + '.json', 'w') as f:
        json.dump(j, f)


# main script
if __name__ == '__main__':
    for file in ['q6-1', 'q6-2', 'q6-3']:
        with open(file + '.html', 'r') as f:
            html = f.read()
        soup = BeautifulSoup(html, "lxml")
        table = soup.center.findChildren('table', recursive=False)[1]
        j = table_to_json(table)
        save_json(j, file)
