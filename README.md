NBI techniques for Gilat's Total_NMS
====================================
### *By Javier Sorribes*, Hispasat S.A.

This repository collects a series of techniques to interact with the Northbound Interface (NBI) server for Gilat's TotalNMS.

For comprehensive information, open *Manual NBI* (in Spanish). Below however, some quick descriptions and a map of this repo's content are provided, in alphabetical order.

techniques
--------------

### EasySoap(Beta)
Contains just a few attempts to use EasySoap for NodeJS. Not of much interest, but could investigate further on this topic.

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
├── .gitignore
├── README.md
├── src
│   ├── helpers.js
│   ├── serve.py
│   ├── XMLReqs
│   │   ├── getCPEpartNumber.xml
│   │   ├── getCPEsByManagedGroup.xml
│   │   ├── getCPEVolumes.xml
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
│   ├── .reqes.js.swp
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
```
