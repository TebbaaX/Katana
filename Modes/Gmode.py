# @name:    Katana-dorkscanner
# @repo:    https://github.com/adnane-X-tebbaa/Katana
# @author:  Adnane tebbaa (AXT)
# Main Google Dorking file V2.0
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
import proxybroker
from googlesearch import search
import sys
import sys
import os
from termcolor import colored, cprint
import warnings
import random
from http import cookiejar
import time


class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, * \
        args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False


def fxn():
    warnings.warn("deprecated", DeprecationWarning)


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


print("")

A = """
,_._._._._._._._._|__________________________________________________________
|G|o|o|g|l|e|_|_|_|_________________________________________________________/
                  |
    Katana dork scanner (Katana-ds V1.5.3) coded by adnane-X-tebbaa 
    Google Mode
"""
print("")
print(A)
TLD = ["com", "com.tw", "co.in", "be", "de",
       "co.uk", "co.ma", "dz", "ru", "ca"]
s = requests.Session()
s.cookies.set_policy(BlockAll())
alpha = input(colored('[>] Please set a Dork : ', 'green'))


def worker(dork, ss):
    query = dork
    beta = random.choice(TLD)
    for gamma in search(query, tld=beta, num=10, stop=95, pause=2):
        print(colored('[+] Found > ', 'yellow') + (gamma))
        if ss:
            ss.write(gamma+"\n")
    print(colored('[+] Done  ', 'green'))
    os.remove("./.google-cookie")


save_state = False

if alpha[-3:] == " \s":
    save_state = True
    alpha = alpha[:-3]

result = ""
if save_state:
    result = open('./result'+str(time.time())+".txt", 'w+')
if alpha[0:4] == "\\f: ":
    fName = "./"+alpha[4:]
    f = open(fName, 'r')
    dork = f.readline()
    while dork:
        print(colored('Working on dork : ' + dork, 'green'))
        worker(dork, result)
        dork = f.readline()
    f.close()
else:
    worker(alpha, result)

if save_state:
    result.close()
