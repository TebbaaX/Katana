# @name:    Katana-dorkscanner
# @repo:    https://github.com/adnane-X-tebbaa/Katana
# @author:  Adnane tebbaa (AXT)
# Main Google Dorking file V0.1
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
import requests # in DEV
import proxybroker # in DEV
from googlesearch import search
import sys
import sys
from termcolor import colored, cprint
import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
        
        
    
print ("")

A = """
,_._._._._._._._._|__________________________________________________________
|G|o|o|g|l|e|_|_|_|_________________________________________________________/
                  |
    Katana dork scanner (Katana-ds) coded by adnane tebbaa 
    
"""
print ("")
print(A)

alpha = input (colored('[>] Please set a Dork : ', 'green', 'on_grey')) 
query = alpha
beta = input (colored('[>] Please set a TLD : ', 'green', 'on_grey')) 
    
for gamma in search(query, tld=beta, num=7,pause=2): 
     print(colored ('[+] Found > ' ,'yellow')  + (gamma) )