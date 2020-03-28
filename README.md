# Katana-ds (dork scanner)
[![Github All Releases](https://img.shields.io/badge/Katana--ds-Version%201.5-red)]()
[![Github All Releases](https://img.shields.io/badge/support-python%203.x-brightgreen)]()
[![Github All Releases](https://img.shields.io/badge/Supported%20OS-Windows%2FLinux-brightgreen)]()

Katana-ds (ds for dork_scanner) is a simple python tool that automates Google Hacking/Dorking and support Tor  
It becomes a more powerfull in combination with [GHDB](https://www.exploit-db.com/google-hacking-database)

![Alt text](https://github.com/adnane-X-tebbaa/imgs/blob/master/img1.jpg)

## Installation :
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements
```bash
cd Katana
python3 -m pip install -r requirements.txt
python3 kds.py 
```
### Tested on Windows [ConEmu](https://conemu.github.io/) [![Github All Releases](https://conemu.github.io/img/logo.png)]() 
## Usage :
```bash
cd Katana
python3 kds.py -h (for help)
Options :
-g :for google mode
-s :for scada mode
-t :for tor mode
-p :for proxy mode
-b :for bitly mode

```
## Google Mode : (supported by python 3.7 and 3.8)
Google mode gives you 2 inputs the "Dork" and the "TLD" (Top Level Domain) that gives you ability to search in specific countries.

e.g : com for Usa / co.ma for Morocoo / be for Belgium

For more please see the included [TLDs.txt](https://github.com/adnane-X-tebbaa/Katana/blob/master/TLDs.txt) file.

![Alt text](https://github.com/adnane-X-tebbaa/imgs/blob/master/google_mode.gif)

## Scada Mode : (supported by python 3.7 and 3.8) 
Scada mode search in google for online PLCs this actually use multiple requests so your ip will be blocked by Google
so changing the TLD will solve the probleme and the script provides inputs for that.

-!> this is just an example actually it shows a lot of results

![Alt text](https://github.com/adnane-X-tebbaa/imgs/blob/master/scada_mode.gif)


Example of [Allen-Bradley](https://ab.rockwellautomation.com/lang-selection.html) PLC dashboard found using Scada Mode

![Alt text](https://github.com/adnane-X-tebbaa/imgs/blob/master/e.g.PNG)

## Tor Mode : (supported by python 3.7 and 3.8) 

[![Github All Releases](http://icons.iconarchive.com/icons/blackvariant/button-ui-requests-8/256/Tor-icon.png)]()

Tor mode gives you 1 input wich is the search query but before you should have tor proxy running on port 9050 
this time there is no ip blocking the script search in 3 tor search engines Phobos, Tor66 and Tordex (more will be added) 

-!> this is just an example actually it shows a lot of results

![Alt text](https://github.com/adnane-X-tebbaa/imgs/blob/master/tor_mode.gif)

![Alt text](http://icons.iconarchive.com/icons/graphicrating/koloria/32/Warning-2-icon.png) 
## What if :
- The script print 'HTTP Error 429 too many requests' :          
**change the TLD**
- The script print 'urllib.error.URLError Errno 1104' :            
**chek if the TLD is true**
- Changing the TLD don't work :                                    
**change your ip by disconnecting and reconnecting again**
- Tor mode show 'Failed to establish a new connection' :          
**make sure that tor proxy up and running on port 9050**

## Proxy Mode :(supported by python 3.7 only ) 
Proxy mode find proxy servers and print them it will print 25 Different Proxy server Each time 

![Alt text](https://github.com/adnane-X-tebbaa/imgs/blob/master/proxy_mode.gif)

## Bitly Mode : (In Development) (supported by python 3.7 and 3.8) 
Find intersting shorted links that sometimes lead to intersting website pages 
the script print currently 10 bitly links with their responses
(script still in development if you got connection error or so many 404,403 just run it again)

![Alt text](https://github.com/adnane-X-tebbaa/imgs/blob/master/bitly_mode.gif)

## Special thanks to :
[LuongPhuHoa](https://github.com/adnane-X-tebbaa/Katana/issues/1) for the Recommendation

#### please feel free to open ISSUES or contact me on [twitter](https://twitter.com/TebbaaX)

## License
[MIT](https://github.com/adnane-X-tebbaa/Katana/blob/master/LICENSE.txt)
