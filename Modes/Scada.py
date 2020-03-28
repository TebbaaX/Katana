# @name:    Katana-DorkScanner
# @repo:    https://github.com/adnane-X-tebbaa/Katana
# @author:  Adnane-X-tebbaa (AXT)
# Scada-file V0.1
# I used dorks for the most used PLCs

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

import sys
import os
import time
from googlesearch import search
import sys
from termcolor import colored, cprint

def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
       

NPP = """ 

         ) ) )               
        ( ( (                   
      ) ) )                   
   (~~~~~~~~~)                
    | POWER |    Katana-ds V1.5              
    |       |    Find online PLCs             
    |      _._   by AXT (adnane-X-tebbaa)             
    |    /    `\            
    |   |   N   |              
    |   |   |~~~~~~~~~~~~~~|   
   /    |   ||~~~~~~~~|    | 
__/_____|___||__|||___|____|__________________________________________
 
 Note: That will take some time
       and you well be asked to change the TLD 
 """

print (NPP)
print (" ")
beta = input (colored('[>] Please set a TLD : ', 'red' )) ###TLD1
print(colored('[+] Searching ', 'green', 'on_grey')) 
B =  """ intitle:"Rockwell Automation" "Device Name" "Uptime" """
query = B
# ****
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
for _ in range(100):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
#*****
for gamma in search(query, tld=beta,stop=50, num=10,pause=2): 
  print(colored ('[+] Found > ' ,'yellow')  + (gamma) )       
print(colored('[+] 18% done ', 'green', 'on_grey')) 
print(colored('[+] 27% done', 'green', 'on_grey'))     
print(colored('[+] 36% done', 'green', 'on_grey'))
 
betax = input (colored('[>] Please set a new TLD to avoid ip blocking : ' , 'red' )) ### TLD2
 
B = """ inurl:dtm.html intitle:1747-L551 """
query = B
# ****
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
for _ in range(100):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
#*****
for gamma in search(query, tld=betax, num=10,stop=50,pause=2): 
     print(colored ('[+] Found > ' ,'yellow')  + (gamma) )    
print(colored('[+] 45% done ', 'green' )) # more scada dorks will be added here
print(colored('[+] 54% done ', 'green' )) #some dorks removed because ip blocking    
print(colored('[+] 63% done', 'green' ))  # but the problme solved 
print(colored('[+] 72% done', 'green' ))  # update soon
print(colored('[+] 81% done', 'green' ))
print(colored('[+] 90% done...', 'green' ))
print(colored('[+] 100% done...', 'green' ))
   




