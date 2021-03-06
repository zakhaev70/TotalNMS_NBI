NBI techniques for Gilat's Total_NMS
====================================
### *By Javier Sorribes*, Hispasat S.A.

This repository collects a series of techniques to interact with the Northbound Interface (NBI) server for Gilat's TotalNMS.

For comprehensive information, open *Manual NBI* (in Spanish). Below however, usage details as well as some quick descriptions and a map of this repo's content are provided, in alphabetical order.

Usage
-----
### Requirements
The only installations and downloads needed are those pertaining to *Python 3*:
- Python 3: [download here](https://www.python.org/downloads/)
- Recommended Python's venv (virtual environment). If you work on a venv, you will be able to update requirements_py.txt appropriately: `python3 -m venv __pyvenv__`, then `source __pyvenv__/bin/activate` ([Python 3 docs](https://docs.python.org/3/library/venv.html))
- Modules: `pip install -r requirements_py.txt`

You may also just execute `./tools/setup_for_py3.sh` from the root directory after adding execution permissions (`chmod +x ./tools/setup_for_py3.sh`). The sript executed will be:
```bash
sudo apt-get install python3;  #comment out if not on Linux or permission errors
python3 -m venv __pyvenv__;
source __pyvenv__/bin/activate;  #specific to bash, check docs for more
pip install --upgrade pip;
pip install -r requirements_py.txt;
```
After executing this script, you would still want to activate the venv by running `source __pyvenv__/bin/activate`.

If you are on Windows, however, the script to execute would be `. ./tools/setup_for_py3_win.sh` (Git Bash recommended).

### Contribution instructions
Before submitting any changes, make sure to (review and) run `./tools/updatereadme.sh .` from the root directory of the repo. This will update requirements_py.txt and README.md (text and sitemap). You might need to add some permissions: `chmod +x ./tools/updatereadme.sh` & `chmod +x ./tools/writemap.sh`

You may add new XML files as needed at /src/XMLReqs. Make sure to document all changes.

### Running the scripts
If ran locally, cross-origin errors might occur, especially with .html and .js files. We recommend opening .html files through a local server, like *Web Server for Chrome*.

Since the NBI server currently does not fulfill all CORS requirements, you might need to send all your requests (especially those from .js files) to the proxy server found in /src/serve.py, through ip address `http://127.0.0.1:9000`. This is a Python 3 script, so you will need to run it as such, and keep it running while your application is in process.

/functions
----------
Contains a set of functions in Python to work with NBI.

### NBI.py
Module with useful functionality, common for most functions and applications. Includes host, authentication credentials, namespace definitions, etc.

/techniques
-----------
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

