# Katana-ds 
[![Github All Releases](https://img.shields.io/badge/Katana--ds-Version%201.5-red)]()
[![Github All Releases](https://img.shields.io/badge/support-python%203.x-brightgreen)]()
[![Github All Releases](https://img.shields.io/badge/Supported%20OS-Windows%2FLinux-brightgreen)]()

Katana-ds (ds for dork_scanner) is a simple python tool that automates Google Hacking/Dorking and support Tor  
It becomes a more powerfull in combinision with [GHDB](https://www.exploit-db.com/google-hacking-database)

![Alt text](https://raw.githubusercontent.com/adnane-X-tebbaa/Katana/master/imgs/img1.jpg)

## Installation :
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirments
```bash
cd Katana
python3 pip install -r requirments
python3 katana-ds.py 
```
### Tested on Windows [ConEmu](https://conemu.github.io/) [![Github All Releases](https://conemu.github.io/img/logo.png)]() 
## Usage :
```bash
cd Katana
python3 katana-ds.py -h (for help)
Options :
-g :for google mode
-s :for scada mode
-t :for tor mode
-p :for proxy mode
-b :for bitly mode

```
## Google Mode :
Google mode gives you 2 inputs the "Dork" and the "TLD" (Top Level Domain) that gives you ability to search in specific countries.

e.g : com for Usa / co.ma for Morocoo / be for Belgium

For more please see the included [TLDs.txt](https://github.com/adnane-X-tebbaa/Katana/blob/master/TLDs.txt) file.

![Alt text](https://raw.githubusercontent.com/adnane-X-tebbaa/Katana/master/imgs/google-m.PNG)

## Scada Mode :
Scada mode search in google for online PLCs this actually use multiple requests so your ip will be blocked by Google
so changing the TLD will solve the probleme and the script provides inputs for that.

-!> this is just an example actually it shows a lot of results

![Alt text](https://raw.githubusercontent.com/adnane-X-tebbaa/Katana/master/imgs/scada-m.PNG)


Example of [Allen-Bradley](https://ab.rockwellautomation.com/lang-selection.html) PLC dashboard found using Scada Mode

![Alt text](https://github.com/adnane-X-tebbaa/Katana/blob/master/imgs/e.g.PNG)

## Tor Mode :

[![Github All Releases](http://icons.iconarchive.com/icons/blackvariant/button-ui-requests-8/256/Tor-icon.png)]()

Tor mode gives you 1 input wich is the search query but before you should have tor proxy running on port 9050 
this time there is no ip blocking the script search in 3 tor search engines Phobos,Tor66 and Tordex (more will be added) 

-!> this is just an example actually it shows a lot of results

![Alt text](https://github.com/adnane-X-tebbaa/Katana/blob/master/imgs/tor.PNG)

## What if :
- The script print 'Error too many requests'           : change the TLD
- Changing the TLD don't work                          : change your ip by disconnecting and reconnecting again
- Tor mode show 'Failed to establish a new connection' : make sure that tor proxy up and running on port 9050

## Soon :
- More Scada Dorks
- More Tor search engines
- More modes
- Proxy support for Google mode
- Proxy support for Scada mode
and More...

##  License :
MIT
