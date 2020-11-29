import requests
from bs4 import BeautifulSoup
import re

def bookSearch(query, exact = False, extension = '', limit = 20):
    url='https://b-ok.cc/s/'
    if query != '':
        url += query+'/?'
    if exact == True:
        url += 'e=1&'
    if extension != '':
        url += 'extension='+extension
    print(url)
    booklist=[]
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    allbooks=soup.findAll(itemprop="name")
    for bookindex in range(len(allbooks)):
        bookname=allbooks[bookindex]
        bookauthor=soup.findAll("div", {"class": "authors"})[bookindex].getText()
        bookextension =soup.findAll("div", {"class": "property_value"})[2+(3*bookindex)].getText()
        link=''
        for link in bookname.findAll('a'):
            link="https://b-ok.cc"+link.get('href')
        bookname=bookname.getText().replace("\n","")
        booklist.append((bookname, bookauthor, link))
    return booklist[:limit]

def getDownloadLink(bookurl, cookies={'remix_userkey': '', 'remix_userid': ''}):
    bookrequests = requests.get(bookurl, cookies=cookies)
    booksoup = BeautifulSoup(bookrequests.text, "html.parser")
    try:
        booklink = 'https://b-ok.cc'+booksoup.find("a", {"class": "btn btn-primary dlButton addDownloadedBook"}).get('href')
        return booklink
    except AttributeError:
        return None

def downloadBook(bookLink, cookies={'remix_userkey': '', 'remix_userid': ''}):
    r = requests.get(getDownloadLink(bookLink, cookies), allow_redirects=True, cookies=cookies, stream=True)
    contentdisposition = r.headers.get('content-disposition')
    fname = re.findall('filename=(.+)', contentdisposition)[0]
    with open(fname, 'wb') as file:
        for data in r:
            file.write(data)