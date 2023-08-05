"""
MIT License

Copyright (c) 2020 TebbaaX

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
import sys
import time
import requests
import asyncio
from proxybroker import Broker
from termcolor import colored, cprint
from bs4 import BeautifulSoup , SoupStrainer
from urllib.request import urlparse, urljoin
import re

T = """

  _____
 |_   _|__  _ __
   | |/ _ \| '__| Katana-ds V1.5.3
   | | (_) | |    Tor Mode
   |_|\___/|_|    Coded by TebbaaX
             
    """
print(T)
print(colored('[!] Tor proxy must be on port 9050 ', 'yellow' )) 
print(colored('[+] Checking TOR... ', 'green' )) 
#search launch**

session = requests.session()
session.proxies = {'http':  'socks5h://localhost:9050',
                   'https': 'socks5h://localhost:9050'}
print(session.get('http://httpbin.org/ip').text) 
print(colored('[+] Got session... ', 'green' ))
###################################################################################################### 
print ("") 
xquery = input ("Please set your query : ") 



#####
##### Phobos
#####
print ("")
print(colored('[+] Searching in "Phobos" http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion...  ', 'green' ))
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=1" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=1" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=2" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=2" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=3" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=3" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=4" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=4" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=5" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=5" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=6" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=6" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=8" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=8" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))  
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=9" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=9" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=10" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=10" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href')) 
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=11" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=11" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))  
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=12" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=12" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))  
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=13" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=13" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=" + xquery + "&p=14" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&p=14" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
print(colored('[+] Done from Phobos', 'yellow' ))

#####
##### TOR66
##### 
print ("")
print(colored('[+] Searching in "TOR66" http://tor77orrbgejplwp.onion... ', 'green' ))
session.get("http://tor66sewebgixwhcqfnp5inzp5x5uohhdy3kvtnyfxc2e5mxiuh34iid.onion/search?q=" + xquery + "&sorttype=rel&page=1" )
page = session.get("http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query="+ xquery + "&sorttype=rel&page=1" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
print(colored('[+] Done from TOR66', 'yellow' ))
print ("")  
#####
##### TOrdex
##### 
print(colored('[+] Searching in "Tordex" http://tordex7iie7z2wcg.onion  ', 'green' )) 
session.get("http://tordex7iie7z2wcg.onion/search?query=" + xquery + "&page=1" )
page = session.get("http://tordex7iie7z2wcg.onion/search?query="+ xquery + "&page=1" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
session.get("http://tordex7iie7z2wcg.onion/search?query=" + xquery + "&page=2" )
page = session.get("http://tordex7iie7z2wcg.onion/search?query="+ xquery + "&page=2" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
session.get("http://tordex7iie7z2wcg.onion/search?query=" + xquery + "&page=3" )
page = session.get("http://tordex7iie7z2wcg.onion/search?query="+ xquery + "&page=3" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))
session.get("http://tordex7iie7z2wcg.onion/search?query=" + xquery + "&page=4" )
page = session.get("http://tordex7iie7z2wcg.onion/search?query="+ xquery + "&page=4" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))  
session.get("http://tordex7iie7z2wcg.onion/search?query=" + xquery + "&page=5" )
page = session.get("http://tordex7iie7z2wcg.onion/search?query="+ xquery + "&page=5" )
soup = BeautifulSoup(page.text, 'html.parser')
tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
for tag in tags:
  print (tag.get('href'))  
print(colored('[+] Done from Tordex', 'yellow' ))

  
