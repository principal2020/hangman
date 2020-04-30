# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:57:57 2020

"""

#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#
#
#def getLinks(articleUrl):
#    html = urlopen("http://www.c21eje.jp/")
#    bsObj = BeautifulSoup(html, "html.parser")
#    return bsObj.find("ul", {"id": "sitemap_list"}).findall("a")
#
#
#links = getLinks("")
#for link in links:
#    print(link)
#    
#    
from bs4 import BeautifulSoup
import urllib.request as req

#指定のURLから全てのリンクを取得する処理
url = "http://www.c21eje.jp/"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
url_items = soup.find_all('a')
for url in url_items:
    print(url)
#print("a = ",url_items)


#import requests, bs4
#res = requests.get('http://www.c21eje.jp/')
#res.raise_for_status()
#soup = bs4.BeautifulSoup(res.text, "html.parser")
#elems = soup.select('#list a')
#for elem in elems:
#    print('{}'.format(elem.get('href')))
#print('Hello')