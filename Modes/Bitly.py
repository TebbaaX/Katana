# @name:    Katana-DorkScanner
# @repo:    https://github.com/adnane-X-tebbaa/Katana-ds
# @author:  Adnane tebbaa (AXT)
# Bit.ly-file Dev
"""
MIT License

Copyright (c) 2020 adnane tebbaa

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
import requests
import os
import time
import sys
import strgen
from bs4 import BeautifulSoup , SoupStrainer
import re
import strgen
from termcolor import colored, cprint

O = """
 ____  _ _     _
| __ )(_) |_  | |_   _  
|  _ \| | __| | | | | | Katana-ds V1.5
| |_) | | |_ _| | |_| | Bit.ly Mode
|____/|_|\__(_)_|\__, | Coded by Adnane-X-Tebbaa (AXT)
                 |___/
"""

print (O) 
print(colored('Note: the script still in dev', 'red', 'on_grey'))
Xbeta = "https://bit.ly/"
resp = requests.get(Xbeta)
print("[+] got :" , resp.status_code )
print(colored('[+] bit.ly is up', 'green', 'on_grey'))
def a () :
 randomString1 = strgen.StringGenerator("[\w\c]{5}").render()
 randomString2 = strgen.StringGenerator("[\w\c]{5}").render()
 randomString3 = strgen.StringGenerator("[\w\c]{5}").render()
 randomString4 = strgen.StringGenerator("[\w\c]{5}").render()
 randomString5 = strgen.StringGenerator("[\w\c]{5}").render()
 randomString6 = strgen.StringGenerator("[\w\c]{6}").render()
 randomString7 = strgen.StringGenerator("[\w\c]{6}").render()
 randomString8 = strgen.StringGenerator("[\w\c]{6}").render()
 randomString9 = strgen.StringGenerator("[\w\c]{6}").render()
 randomString10 = strgen.StringGenerator("[\w\c]{6}").render()
 
 page = requests.get(Xbeta + randomString1)
 print (Xbeta + randomString1 , page.status_code )
 time.sleep(1)
 page = requests.get(Xbeta + randomString2)
 print (Xbeta + randomString2 , page.status_code )
 time.sleep(1)
 page = requests.get(Xbeta + randomString3)
 print (Xbeta + randomString3 , page.status_code  )
 time.sleep(1)
 page = requests.get(Xbeta + randomString4)
 print (Xbeta + randomString4 , page.status_code  )
 time.sleep(1)
 page = requests.get(Xbeta + randomString5)
 print (Xbeta + randomString5 , page.status_code  )
 time.sleep(1)
 page = requests.get(Xbeta + randomString5)
 print (Xbeta + randomString6 , page.status_code )
 time.sleep(1)
 page = requests.get(Xbeta + randomString2)
 print (Xbeta + randomString7 , page.status_code )
 time.sleep(1)
 page = requests.get(Xbeta + randomString3)
 print (Xbeta + randomString8 , page.status_code  )
 time.sleep(1)
 page = requests.get(Xbeta + randomString4)
 print (Xbeta + randomString9 , page.status_code  )
 time.sleep(1)
 page = requests.get(Xbeta + randomString5)
 print (Xbeta + randomString10 , page.status_code  )
 
try :
 a ()
except requests.exceptions.RequestException as e: 
 print(colored('got an ERROR...Overriding...:', 'green' ))  
 print(colored('[>] Sleeping for 5s :', 'yellow' , resp.status_code))
 a ()  
