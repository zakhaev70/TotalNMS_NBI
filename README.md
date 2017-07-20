NBI techniques for Gilat's Total_NMS
====================================
### *By Javier Sorribes*, Hispasat S.A.

This repository collects a series of techniques to interact with the Northbound Interface (NBI) server for Gilat's TotalNMS.

For comprehensive information, open *Manual NBI* (in Spanish). Below however, usage details as well as some quick descriptions and a map of this repo's content are provided, in alphabetical order.

Usage
-----
### Contribution instructions
Before submitting any changes, make sure to run `./tools/updatereadme.sh .` from the root directory of the repo. You might need to add some permissions: `chmod +x ./tools/updatereadme.sh` & `chmod +x ./tools/writemap.sh`

You may add new XML files as needed at /src/XMLReqs. Make sure to document all changes.

### Running the scripts
If ran locally, cross-origin errors might occur, especially with .html and .js files. We recommend opening .html files through a local server, like *Web Server for Chrome*.

Since the NBI server currently does not fulfill all CORS requirements, you might need to send all your requests (especially those from .js files) to the proxy server found in /src/serve.py, through ip address `http://127.0.0.1:9000`. This is a Python 3 script, so you will need to run it as such, and keep it running while your application is in process.

/techniques
--------------
### EasySoap(Beta)
Contains just a few attempts to use EasySoap for NodeJS. Not of much interest, but could investigate further on this topic.

### JQuery
...

### JS
Sample JS request which fails due to CORS' preflight issues, at least when run locally.

### JS_PYServer
Sample JS requests that work when serve.py (proxy server, accounts for CORS) is running. If run locally, should do so from Web Server for  Chrome.
Also a few Python scripts that send requests to serve.py as well.

### PY
...
 
Sitemap
-------

```
.TotalNMS_NBI
├── docs
│   ├── Manual NBI.DOC
│   ├── Manual NBI.pdf
│   ├── Presentación NBI.pptx
├── functions
│   ├── NBI.py
│   ├── onlineReport.py
├── .gitignore
├── README.md
├── src
│   ├── helpers.js
│   ├── ns.json
│   ├── serve.py
│   ├── XMLReqs
│   │   ├── getCPEpartNumber.xml
│   │   ├── getCPEsByManagedGroup.xml
│   │   ├── getCPEVolumes.xml
│   │   ├── getNumberOfActiveCPEs.xml
│   │   ├── req_headers.txt
├── techniques
│   ├── EasySoap(Beta)
│   │   ├── reqes.html
│   │   ├── reqes.js
│   ├── JQuery
│   │   ├── indexjq2.html
│   │   ├── indexjq.html
│   │   ├── reqjq2.js
│   │   ├── reqjq.js
│   ├── JS
│   │   ├── req.html
│   │   ├── req.js
│   ├── JS_PYServer
│   │   ├── comb.py
│   │   ├── index.html
│   │   ├── req.js
│   │   ├── req.py
│   ├── PY
│   │   ├── comb.py
│   │   ├── p.py
│   │   ├── req.py
│   ├── TutorialJS
│   │   ├── hello.html
│   │   ├── hello.js
│   │   ├── hello.txt
│   │   ├── req.html
│   │   ├── req.js
│   ├── TutorialPY
│   │   ├── nbi2.py
│   │   ├── nbi3.py
│   │   ├── nbi4.py
│   │   ├── nbi.py
│   │   ├── out.txt
├── tools
│   ├── readmetxt.md
│   ├── sitemap.md
│   ├── updatereadme.sh
│   ├── writemap.sh
│   ├── WSDL
│   │   ├── cpeService.xml
│   │   ├── elementsInformationService.xml
│   │   ├── multiCastService.xml
│   │   ├── qosService.xml
```
