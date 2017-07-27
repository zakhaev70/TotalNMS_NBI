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

```
.TotalNMS_NBI
├── docs
│   ├── Manual NBI.DOC
│   ├── Manual NBI.pdf
│   ├── Presentación NBI.pptx
├── functions
│   ├── elementPerformance.py
│   ├── NBI.py
│   ├── onlineReport.py
│   ├── __pycache__
│   │   ├── NBI.cpython-35.pyc
│   ├── RFAudit.py
│   ├── RFAuditResults
│   │   ├── RFAudit2.csv
│   │   ├── RFAudit6.csv
├── .gitignore
├── __pyvenv__
│   ├── bin
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── chardetect
│   │   ├── easy_install
│   │   ├── easy_install-3.5
│   │   ├── pip
│   │   ├── pip3
│   │   ├── pip3.5
│   │   ├── python
│   │   ├── python3
│   ├── include
│   ├── lib
│   │   ├── python3.5
│   │   │   ├── site-packages
│   │   │   │   ├── certifi
│   │   │   │   │   ├── cacert.pem
│   │   │   │   │   ├── core.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── __main__.py
│   │   │   │   │   ├── old_root.pem
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── core.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── __main__.cpython-35.pyc
│   │   │   │   │   ├── weak.pem
│   │   │   │   ├── certifi-2017.4.17.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   │   │   │   ├── chardet
│   │   │   │   │   ├── big5freq.py
│   │   │   │   │   ├── big5prober.py
│   │   │   │   │   ├── chardistribution.py
│   │   │   │   │   ├── charsetgroupprober.py
│   │   │   │   │   ├── charsetprober.py
│   │   │   │   │   ├── cli
│   │   │   │   │   │   ├── chardetect.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── chardetect.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── codingstatemachine.py
│   │   │   │   │   ├── compat.py
│   │   │   │   │   ├── cp949prober.py
│   │   │   │   │   ├── enums.py
│   │   │   │   │   ├── escprober.py
│   │   │   │   │   ├── escsm.py
│   │   │   │   │   ├── eucjpprober.py
│   │   │   │   │   ├── euckrfreq.py
│   │   │   │   │   ├── euckrprober.py
│   │   │   │   │   ├── euctwfreq.py
│   │   │   │   │   ├── euctwprober.py
│   │   │   │   │   ├── gb2312freq.py
│   │   │   │   │   ├── gb2312prober.py
│   │   │   │   │   ├── hebrewprober.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── jisfreq.py
│   │   │   │   │   ├── jpcntx.py
│   │   │   │   │   ├── langbulgarianmodel.py
│   │   │   │   │   ├── langcyrillicmodel.py
│   │   │   │   │   ├── langgreekmodel.py
│   │   │   │   │   ├── langhebrewmodel.py
│   │   │   │   │   ├── langhungarianmodel.py
│   │   │   │   │   ├── langthaimodel.py
│   │   │   │   │   ├── langturkishmodel.py
│   │   │   │   │   ├── latin1prober.py
│   │   │   │   │   ├── mbcharsetprober.py
│   │   │   │   │   ├── mbcsgroupprober.py
│   │   │   │   │   ├── mbcssm.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── big5freq.cpython-35.pyc
│   │   │   │   │   │   ├── big5prober.cpython-35.pyc
│   │   │   │   │   │   ├── chardistribution.cpython-35.pyc
│   │   │   │   │   │   ├── charsetgroupprober.cpython-35.pyc
│   │   │   │   │   │   ├── charsetprober.cpython-35.pyc
│   │   │   │   │   │   ├── codingstatemachine.cpython-35.pyc
│   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   ├── cp949prober.cpython-35.pyc
│   │   │   │   │   │   ├── enums.cpython-35.pyc
│   │   │   │   │   │   ├── escprober.cpython-35.pyc
│   │   │   │   │   │   ├── escsm.cpython-35.pyc
│   │   │   │   │   │   ├── eucjpprober.cpython-35.pyc
│   │   │   │   │   │   ├── euckrfreq.cpython-35.pyc
│   │   │   │   │   │   ├── euckrprober.cpython-35.pyc
│   │   │   │   │   │   ├── euctwfreq.cpython-35.pyc
│   │   │   │   │   │   ├── euctwprober.cpython-35.pyc
│   │   │   │   │   │   ├── gb2312freq.cpython-35.pyc
│   │   │   │   │   │   ├── gb2312prober.cpython-35.pyc
│   │   │   │   │   │   ├── hebrewprober.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── jisfreq.cpython-35.pyc
│   │   │   │   │   │   ├── jpcntx.cpython-35.pyc
│   │   │   │   │   │   ├── langbulgarianmodel.cpython-35.pyc
│   │   │   │   │   │   ├── langcyrillicmodel.cpython-35.pyc
│   │   │   │   │   │   ├── langgreekmodel.cpython-35.pyc
│   │   │   │   │   │   ├── langhebrewmodel.cpython-35.pyc
│   │   │   │   │   │   ├── langhungarianmodel.cpython-35.pyc
│   │   │   │   │   │   ├── langthaimodel.cpython-35.pyc
│   │   │   │   │   │   ├── langturkishmodel.cpython-35.pyc
│   │   │   │   │   │   ├── latin1prober.cpython-35.pyc
│   │   │   │   │   │   ├── mbcharsetprober.cpython-35.pyc
│   │   │   │   │   │   ├── mbcsgroupprober.cpython-35.pyc
│   │   │   │   │   │   ├── mbcssm.cpython-35.pyc
│   │   │   │   │   │   ├── sbcharsetprober.cpython-35.pyc
│   │   │   │   │   │   ├── sbcsgroupprober.cpython-35.pyc
│   │   │   │   │   │   ├── sjisprober.cpython-35.pyc
│   │   │   │   │   │   ├── universaldetector.cpython-35.pyc
│   │   │   │   │   │   ├── utf8prober.cpython-35.pyc
│   │   │   │   │   │   ├── version.cpython-35.pyc
│   │   │   │   │   ├── sbcharsetprober.py
│   │   │   │   │   ├── sbcsgroupprober.py
│   │   │   │   │   ├── sjisprober.py
│   │   │   │   │   ├── universaldetector.py
│   │   │   │   │   ├── utf8prober.py
│   │   │   │   │   ├── version.py
│   │   │   │   ├── chardet-3.0.4.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── entry_points.txt
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   │   │   │   ├── easy_install.py
│   │   │   │   ├── idna
│   │   │   │   │   ├── codec.py
│   │   │   │   │   ├── compat.py
│   │   │   │   │   ├── core.py
│   │   │   │   │   ├── idnadata.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── intranges.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── codec.cpython-35.pyc
│   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   ├── core.cpython-35.pyc
│   │   │   │   │   │   ├── idnadata.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── intranges.cpython-35.pyc
│   │   │   │   │   │   ├── uts46data.cpython-35.pyc
│   │   │   │   │   ├── uts46data.py
│   │   │   │   ├── idna-2.5.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── pbr.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   │   │   │   ├── pip
│   │   │   │   │   ├── basecommand.py
│   │   │   │   │   ├── baseparser.py
│   │   │   │   │   ├── cmdoptions.py
│   │   │   │   │   ├── commands
│   │   │   │   │   │   ├── check.py
│   │   │   │   │   │   ├── completion.py
│   │   │   │   │   │   ├── download.py
│   │   │   │   │   │   ├── freeze.py
│   │   │   │   │   │   ├── hash.py
│   │   │   │   │   │   ├── help.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── install.py
│   │   │   │   │   │   ├── list.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── check.cpython-35.pyc
│   │   │   │   │   │   │   ├── completion.cpython-35.pyc
│   │   │   │   │   │   │   ├── download.cpython-35.pyc
│   │   │   │   │   │   │   ├── freeze.cpython-35.pyc
│   │   │   │   │   │   │   ├── hash.cpython-35.pyc
│   │   │   │   │   │   │   ├── help.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── install.cpython-35.pyc
│   │   │   │   │   │   │   ├── list.cpython-35.pyc
│   │   │   │   │   │   │   ├── search.cpython-35.pyc
│   │   │   │   │   │   │   ├── show.cpython-35.pyc
│   │   │   │   │   │   │   ├── uninstall.cpython-35.pyc
│   │   │   │   │   │   │   ├── wheel.cpython-35.pyc
│   │   │   │   │   │   ├── search.py
│   │   │   │   │   │   ├── show.py
│   │   │   │   │   │   ├── uninstall.py
│   │   │   │   │   │   ├── wheel.py
│   │   │   │   │   ├── compat
│   │   │   │   │   │   ├── dictconfig.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── dictconfig.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── download.py
│   │   │   │   │   ├── exceptions.py
│   │   │   │   │   ├── index.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── locations.py
│   │   │   │   │   ├── __main__.py
│   │   │   │   │   ├── models
│   │   │   │   │   │   ├── index.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── index.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── operations
│   │   │   │   │   │   ├── check.py
│   │   │   │   │   │   ├── freeze.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── check.cpython-35.pyc
│   │   │   │   │   │   │   ├── freeze.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── pep425tags.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── basecommand.cpython-35.pyc
│   │   │   │   │   │   ├── baseparser.cpython-35.pyc
│   │   │   │   │   │   ├── cmdoptions.cpython-35.pyc
│   │   │   │   │   │   ├── download.cpython-35.pyc
│   │   │   │   │   │   ├── exceptions.cpython-35.pyc
│   │   │   │   │   │   ├── index.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── locations.cpython-35.pyc
│   │   │   │   │   │   ├── __main__.cpython-35.pyc
│   │   │   │   │   │   ├── pep425tags.cpython-35.pyc
│   │   │   │   │   │   ├── status_codes.cpython-35.pyc
│   │   │   │   │   │   ├── wheel.cpython-35.pyc
│   │   │   │   │   ├── req
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── req_file.cpython-35.pyc
│   │   │   │   │   │   │   ├── req_install.cpython-35.pyc
│   │   │   │   │   │   │   ├── req_set.cpython-35.pyc
│   │   │   │   │   │   │   ├── req_uninstall.cpython-35.pyc
│   │   │   │   │   │   ├── req_file.py
│   │   │   │   │   │   ├── req_install.py
│   │   │   │   │   │   ├── req_set.py
│   │   │   │   │   │   ├── req_uninstall.py
│   │   │   │   │   ├── status_codes.py
│   │   │   │   │   ├── utils
│   │   │   │   │   │   ├── appdirs.py
│   │   │   │   │   │   ├── build.py
│   │   │   │   │   │   ├── deprecation.py
│   │   │   │   │   │   ├── encoding.py
│   │   │   │   │   │   ├── filesystem.py
│   │   │   │   │   │   ├── glibc.py
│   │   │   │   │   │   ├── hashes.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── logging.py
│   │   │   │   │   │   ├── outdated.py
│   │   │   │   │   │   ├── packaging.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── appdirs.cpython-35.pyc
│   │   │   │   │   │   │   ├── build.cpython-35.pyc
│   │   │   │   │   │   │   ├── deprecation.cpython-35.pyc
│   │   │   │   │   │   │   ├── encoding.cpython-35.pyc
│   │   │   │   │   │   │   ├── filesystem.cpython-35.pyc
│   │   │   │   │   │   │   ├── glibc.cpython-35.pyc
│   │   │   │   │   │   │   ├── hashes.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── logging.cpython-35.pyc
│   │   │   │   │   │   │   ├── outdated.cpython-35.pyc
│   │   │   │   │   │   │   ├── packaging.cpython-35.pyc
│   │   │   │   │   │   │   ├── setuptools_build.cpython-35.pyc
│   │   │   │   │   │   │   ├── ui.cpython-35.pyc
│   │   │   │   │   │   ├── setuptools_build.py
│   │   │   │   │   │   ├── ui.py
│   │   │   │   │   ├── vcs
│   │   │   │   │   │   ├── bazaar.py
│   │   │   │   │   │   ├── git.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── mercurial.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── bazaar.cpython-35.pyc
│   │   │   │   │   │   │   ├── git.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── mercurial.cpython-35.pyc
│   │   │   │   │   │   │   ├── subversion.cpython-35.pyc
│   │   │   │   │   │   ├── subversion.py
│   │   │   │   │   ├── _vendor
│   │   │   │   │   │   ├── appdirs.py
│   │   │   │   │   │   ├── cachecontrol
│   │   │   │   │   │   │   ├── adapter.py
│   │   │   │   │   │   │   ├── cache.py
│   │   │   │   │   │   │   ├── caches
│   │   │   │   │   │   │   │   ├── file_cache.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── file_cache.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── redis_cache.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── redis_cache.py
│   │   │   │   │   │   │   ├── _cmd.py
│   │   │   │   │   │   │   ├── compat.py
│   │   │   │   │   │   │   ├── controller.py
│   │   │   │   │   │   │   ├── filewrapper.py
│   │   │   │   │   │   │   ├── heuristics.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── adapter.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── cache.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _cmd.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── controller.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── filewrapper.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── heuristics.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── serialize.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── wrapper.cpython-35.pyc
│   │   │   │   │   │   │   ├── serialize.py
│   │   │   │   │   │   │   ├── wrapper.py
│   │   │   │   │   │   ├── colorama
│   │   │   │   │   │   │   ├── ansi.py
│   │   │   │   │   │   │   ├── ansitowin32.py
│   │   │   │   │   │   │   ├── initialise.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── ansi.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── ansitowin32.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── initialise.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── win32.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── winterm.cpython-35.pyc
│   │   │   │   │   │   │   ├── win32.py
│   │   │   │   │   │   │   ├── winterm.py
│   │   │   │   │   │   ├── distlib
│   │   │   │   │   │   │   ├── _backport
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── misc.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── misc.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── shutil.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── sysconfig.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── tarfile.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── shutil.py
│   │   │   │   │   │   │   │   ├── sysconfig.cfg
│   │   │   │   │   │   │   │   ├── sysconfig.py
│   │   │   │   │   │   │   │   ├── tarfile.py
│   │   │   │   │   │   │   ├── compat.py
│   │   │   │   │   │   │   ├── database.py
│   │   │   │   │   │   │   ├── index.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── locators.py
│   │   │   │   │   │   │   ├── manifest.py
│   │   │   │   │   │   │   ├── markers.py
│   │   │   │   │   │   │   ├── metadata.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── database.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── index.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── locators.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── manifest.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── markers.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── metadata.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── resources.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── scripts.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── util.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── version.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── wheel.cpython-35.pyc
│   │   │   │   │   │   │   ├── resources.py
│   │   │   │   │   │   │   ├── scripts.py
│   │   │   │   │   │   │   ├── t32.exe
│   │   │   │   │   │   │   ├── t64.exe
│   │   │   │   │   │   │   ├── util.py
│   │   │   │   │   │   │   ├── version.py
│   │   │   │   │   │   │   ├── w32.exe
│   │   │   │   │   │   │   ├── w64.exe
│   │   │   │   │   │   │   ├── wheel.py
│   │   │   │   │   │   ├── distro.py
│   │   │   │   │   │   ├── html5lib
│   │   │   │   │   │   │   ├── constants.py
│   │   │   │   │   │   │   ├── filters
│   │   │   │   │   │   │   │   ├── alphabeticalattributes.py
│   │   │   │   │   │   │   │   ├── base.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── inject_meta_charset.py
│   │   │   │   │   │   │   │   ├── lint.py
│   │   │   │   │   │   │   │   ├── optionaltags.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── alphabeticalattributes.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── base.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── inject_meta_charset.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── lint.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── optionaltags.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── sanitizer.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── whitespace.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── sanitizer.py
│   │   │   │   │   │   │   │   ├── whitespace.py
│   │   │   │   │   │   │   ├── html5parser.py
│   │   │   │   │   │   │   ├── _ihatexml.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── _inputstream.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── constants.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── html5parser.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _ihatexml.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _inputstream.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── serializer.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _tokenizer.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _utils.cpython-35.pyc
│   │   │   │   │   │   │   ├── serializer.py
│   │   │   │   │   │   │   ├── _tokenizer.py
│   │   │   │   │   │   │   ├── treeadapters
│   │   │   │   │   │   │   │   ├── genshi.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── genshi.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── sax.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── sax.py
│   │   │   │   │   │   │   ├── treebuilders
│   │   │   │   │   │   │   │   ├── base.py
│   │   │   │   │   │   │   │   ├── dom.py
│   │   │   │   │   │   │   │   ├── etree_lxml.py
│   │   │   │   │   │   │   │   ├── etree.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── base.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── dom.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── etree.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── etree_lxml.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── treewalkers
│   │   │   │   │   │   │   │   ├── base.py
│   │   │   │   │   │   │   │   ├── dom.py
│   │   │   │   │   │   │   │   ├── etree_lxml.py
│   │   │   │   │   │   │   │   ├── etree.py
│   │   │   │   │   │   │   │   ├── genshi.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── base.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── dom.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── etree.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── etree_lxml.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── genshi.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── _trie
│   │   │   │   │   │   │   │   ├── _base.py
│   │   │   │   │   │   │   │   ├── datrie.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── _base.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── datrie.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── py.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── py.py
│   │   │   │   │   │   │   ├── _utils.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── ipaddress.py
│   │   │   │   │   │   ├── lockfile
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── linklockfile.py
│   │   │   │   │   │   │   ├── mkdirlockfile.py
│   │   │   │   │   │   │   ├── pidlockfile.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── linklockfile.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── mkdirlockfile.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── pidlockfile.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── sqlitelockfile.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── symlinklockfile.cpython-35.pyc
│   │   │   │   │   │   │   ├── sqlitelockfile.py
│   │   │   │   │   │   │   ├── symlinklockfile.py
│   │   │   │   │   │   ├── ordereddict.py
│   │   │   │   │   │   ├── packaging
│   │   │   │   │   │   │   ├── __about__.py
│   │   │   │   │   │   │   ├── _compat.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── markers.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── __about__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _compat.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── markers.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── requirements.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── specifiers.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _structures.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── utils.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── version.cpython-35.pyc
│   │   │   │   │   │   │   ├── requirements.py
│   │   │   │   │   │   │   ├── specifiers.py
│   │   │   │   │   │   │   ├── _structures.py
│   │   │   │   │   │   │   ├── utils.py
│   │   │   │   │   │   │   ├── version.py
│   │   │   │   │   │   ├── pkg_resources
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── progress
│   │   │   │   │   │   │   ├── bar.py
│   │   │   │   │   │   │   ├── counter.py
│   │   │   │   │   │   │   ├── helpers.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── bar.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── counter.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── helpers.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── spinner.cpython-35.pyc
│   │   │   │   │   │   │   ├── spinner.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── appdirs.cpython-35.pyc
│   │   │   │   │   │   │   ├── distro.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── ipaddress.cpython-35.pyc
│   │   │   │   │   │   │   ├── ordereddict.cpython-35.pyc
│   │   │   │   │   │   │   ├── pyparsing.cpython-35.pyc
│   │   │   │   │   │   │   ├── retrying.cpython-35.pyc
│   │   │   │   │   │   │   ├── re-vendor.cpython-35.pyc
│   │   │   │   │   │   │   ├── six.cpython-35.pyc
│   │   │   │   │   │   ├── pyparsing.py
│   │   │   │   │   │   ├── requests
│   │   │   │   │   │   │   ├── adapters.py
│   │   │   │   │   │   │   ├── api.py
│   │   │   │   │   │   │   ├── auth.py
│   │   │   │   │   │   │   ├── cacert.pem
│   │   │   │   │   │   │   ├── certs.py
│   │   │   │   │   │   │   ├── compat.py
│   │   │   │   │   │   │   ├── cookies.py
│   │   │   │   │   │   │   ├── exceptions.py
│   │   │   │   │   │   │   ├── hooks.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── models.py
│   │   │   │   │   │   │   ├── packages
│   │   │   │   │   │   │   │   ├── chardet
│   │   │   │   │   │   │   │   │   ├── big5freq.py
│   │   │   │   │   │   │   │   │   ├── big5prober.py
│   │   │   │   │   │   │   │   │   ├── chardetect.py
│   │   │   │   │   │   │   │   │   ├── chardistribution.py
│   │   │   │   │   │   │   │   │   ├── charsetgroupprober.py
│   │   │   │   │   │   │   │   │   ├── charsetprober.py
│   │   │   │   │   │   │   │   │   ├── codingstatemachine.py
│   │   │   │   │   │   │   │   │   ├── compat.py
│   │   │   │   │   │   │   │   │   ├── constants.py
│   │   │   │   │   │   │   │   │   ├── cp949prober.py
│   │   │   │   │   │   │   │   │   ├── escprober.py
│   │   │   │   │   │   │   │   │   ├── escsm.py
│   │   │   │   │   │   │   │   │   ├── eucjpprober.py
│   │   │   │   │   │   │   │   │   ├── euckrfreq.py
│   │   │   │   │   │   │   │   │   ├── euckrprober.py
│   │   │   │   │   │   │   │   │   ├── euctwfreq.py
│   │   │   │   │   │   │   │   │   ├── euctwprober.py
│   │   │   │   │   │   │   │   │   ├── gb2312freq.py
│   │   │   │   │   │   │   │   │   ├── gb2312prober.py
│   │   │   │   │   │   │   │   │   ├── hebrewprober.py
│   │   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   │   ├── jisfreq.py
│   │   │   │   │   │   │   │   │   ├── jpcntx.py
│   │   │   │   │   │   │   │   │   ├── langbulgarianmodel.py
│   │   │   │   │   │   │   │   │   ├── langcyrillicmodel.py
│   │   │   │   │   │   │   │   │   ├── langgreekmodel.py
│   │   │   │   │   │   │   │   │   ├── langhebrewmodel.py
│   │   │   │   │   │   │   │   │   ├── langhungarianmodel.py
│   │   │   │   │   │   │   │   │   ├── langthaimodel.py
│   │   │   │   │   │   │   │   │   ├── latin1prober.py
│   │   │   │   │   │   │   │   │   ├── mbcharsetprober.py
│   │   │   │   │   │   │   │   │   ├── mbcsgroupprober.py
│   │   │   │   │   │   │   │   │   ├── mbcssm.py
│   │   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   │   ├── big5freq.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── big5prober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── chardetect.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── chardistribution.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── charsetgroupprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── charsetprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── codingstatemachine.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── constants.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── cp949prober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── escprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── escsm.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── eucjpprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── euckrfreq.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── euckrprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── euctwfreq.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── euctwprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── gb2312freq.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── gb2312prober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── hebrewprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── jisfreq.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── jpcntx.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── langbulgarianmodel.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── langcyrillicmodel.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── langgreekmodel.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── langhebrewmodel.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── langhungarianmodel.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── langthaimodel.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── latin1prober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── mbcharsetprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── mbcsgroupprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── mbcssm.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── sbcharsetprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── sbcsgroupprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── sjisprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── universaldetector.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── utf8prober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── sbcharsetprober.py
│   │   │   │   │   │   │   │   │   ├── sbcsgroupprober.py
│   │   │   │   │   │   │   │   │   ├── sjisprober.py
│   │   │   │   │   │   │   │   │   ├── universaldetector.py
│   │   │   │   │   │   │   │   │   ├── utf8prober.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── urllib3
│   │   │   │   │   │   │   │   │   ├── _collections.py
│   │   │   │   │   │   │   │   │   ├── connectionpool.py
│   │   │   │   │   │   │   │   │   ├── connection.py
│   │   │   │   │   │   │   │   │   ├── contrib
│   │   │   │   │   │   │   │   │   │   ├── appengine.py
│   │   │   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   │   │   ├── ntlmpool.py
│   │   │   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   │   │   ├── appengine.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── ntlmpool.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── pyopenssl.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── socks.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── pyopenssl.py
│   │   │   │   │   │   │   │   │   │   ├── socks.py
│   │   │   │   │   │   │   │   │   ├── exceptions.py
│   │   │   │   │   │   │   │   │   ├── fields.py
│   │   │   │   │   │   │   │   │   ├── filepost.py
│   │   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   │   ├── packages
│   │   │   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   │   │   ├── ordered_dict.py
│   │   │   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── ordered_dict.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── six.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── six.py
│   │   │   │   │   │   │   │   │   │   ├── ssl_match_hostname
│   │   │   │   │   │   │   │   │   │   │   ├── _implementation.py
│   │   │   │   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   │   │   │   ├── _implementation.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── poolmanager.py
│   │   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   │   ├── _collections.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── connection.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── connectionpool.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── exceptions.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── fields.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── filepost.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── poolmanager.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── request.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── response.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── request.py
│   │   │   │   │   │   │   │   │   ├── response.py
│   │   │   │   │   │   │   │   │   ├── util
│   │   │   │   │   │   │   │   │   │   ├── connection.py
│   │   │   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   │   │   ├── connection.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── request.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── response.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── retry.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── ssl_.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── timeout.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── url.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── request.py
│   │   │   │   │   │   │   │   │   │   ├── response.py
│   │   │   │   │   │   │   │   │   │   ├── retry.py
│   │   │   │   │   │   │   │   │   │   ├── ssl_.py
│   │   │   │   │   │   │   │   │   │   ├── timeout.py
│   │   │   │   │   │   │   │   │   │   ├── url.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── adapters.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── api.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── auth.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── certs.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── cookies.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── exceptions.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── hooks.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── models.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── sessions.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── status_codes.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── structures.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── utils.cpython-35.pyc
│   │   │   │   │   │   │   ├── sessions.py
│   │   │   │   │   │   │   ├── status_codes.py
│   │   │   │   │   │   │   ├── structures.py
│   │   │   │   │   │   │   ├── utils.py
│   │   │   │   │   │   ├── retrying.py
│   │   │   │   │   │   ├── re-vendor.py
│   │   │   │   │   │   ├── six.py
│   │   │   │   │   │   ├── webencodings
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── labels.py
│   │   │   │   │   │   │   ├── mklabels.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── labels.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── mklabels.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── tests.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── x_user_defined.cpython-35.pyc
│   │   │   │   │   │   │   ├── tests.py
│   │   │   │   │   │   │   ├── x_user_defined.py
│   │   │   │   │   ├── wheel.py
│   │   │   │   ├── pip-9.0.1.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── entry_points.txt
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   │   │   │   ├── pkg_resources
│   │   │   │   │   ├── extern
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── _vendor
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── packaging
│   │   │   │   │   │   │   ├── __about__.py
│   │   │   │   │   │   │   ├── _compat.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── markers.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── __about__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _compat.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── markers.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── requirements.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── specifiers.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _structures.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── utils.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── version.cpython-35.pyc
│   │   │   │   │   │   │   ├── requirements.py
│   │   │   │   │   │   │   ├── specifiers.py
│   │   │   │   │   │   │   ├── _structures.py
│   │   │   │   │   │   │   ├── utils.py
│   │   │   │   │   │   │   ├── version.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── pyparsing.cpython-35.pyc
│   │   │   │   │   │   │   ├── six.cpython-35.pyc
│   │   │   │   │   │   ├── pyparsing.py
│   │   │   │   │   │   ├── six.py
│   │   │   │   ├── pkg_resources-0.0.0.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── WHEEL
│   │   │   │   ├── __pycache__
│   │   │   │   │   ├── easy_install.cpython-35.pyc
│   │   │   │   ├── requests
│   │   │   │   │   ├── adapters.py
│   │   │   │   │   ├── api.py
│   │   │   │   │   ├── auth.py
│   │   │   │   │   ├── certs.py
│   │   │   │   │   ├── compat.py
│   │   │   │   │   ├── cookies.py
│   │   │   │   │   ├── exceptions.py
│   │   │   │   │   ├── help.py
│   │   │   │   │   ├── hooks.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _internal_utils.py
│   │   │   │   │   ├── models.py
│   │   │   │   │   ├── packages.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── adapters.cpython-35.pyc
│   │   │   │   │   │   ├── api.cpython-35.pyc
│   │   │   │   │   │   ├── auth.cpython-35.pyc
│   │   │   │   │   │   ├── certs.cpython-35.pyc
│   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   ├── cookies.cpython-35.pyc
│   │   │   │   │   │   ├── exceptions.cpython-35.pyc
│   │   │   │   │   │   ├── help.cpython-35.pyc
│   │   │   │   │   │   ├── hooks.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── _internal_utils.cpython-35.pyc
│   │   │   │   │   │   ├── models.cpython-35.pyc
│   │   │   │   │   │   ├── packages.cpython-35.pyc
│   │   │   │   │   │   ├── sessions.cpython-35.pyc
│   │   │   │   │   │   ├── status_codes.cpython-35.pyc
│   │   │   │   │   │   ├── structures.cpython-35.pyc
│   │   │   │   │   │   ├── utils.cpython-35.pyc
│   │   │   │   │   │   ├── __version__.cpython-35.pyc
│   │   │   │   │   ├── sessions.py
│   │   │   │   │   ├── status_codes.py
│   │   │   │   │   ├── structures.py
│   │   │   │   │   ├── utils.py
│   │   │   │   │   ├── __version__.py
│   │   │   │   ├── requests-2.18.2.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   │   │   │   ├── setuptools
│   │   │   │   │   ├── archive_util.py
│   │   │   │   │   ├── command
│   │   │   │   │   │   ├── alias.py
│   │   │   │   │   │   ├── bdist_egg.py
│   │   │   │   │   │   ├── bdist_rpm.py
│   │   │   │   │   │   ├── bdist_wininst.py
│   │   │   │   │   │   ├── build_ext.py
│   │   │   │   │   │   ├── build_py.py
│   │   │   │   │   │   ├── develop.py
│   │   │   │   │   │   ├── easy_install.py
│   │   │   │   │   │   ├── egg_info.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── install_egg_info.py
│   │   │   │   │   │   ├── install_lib.py
│   │   │   │   │   │   ├── install.py
│   │   │   │   │   │   ├── install_scripts.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── alias.cpython-35.pyc
│   │   │   │   │   │   │   ├── bdist_egg.cpython-35.pyc
│   │   │   │   │   │   │   ├── bdist_rpm.cpython-35.pyc
│   │   │   │   │   │   │   ├── bdist_wininst.cpython-35.pyc
│   │   │   │   │   │   │   ├── build_ext.cpython-35.pyc
│   │   │   │   │   │   │   ├── build_py.cpython-35.pyc
│   │   │   │   │   │   │   ├── develop.cpython-35.pyc
│   │   │   │   │   │   │   ├── easy_install.cpython-35.pyc
│   │   │   │   │   │   │   ├── egg_info.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── install.cpython-35.pyc
│   │   │   │   │   │   │   ├── install_egg_info.cpython-35.pyc
│   │   │   │   │   │   │   ├── install_lib.cpython-35.pyc
│   │   │   │   │   │   │   ├── install_scripts.cpython-35.pyc
│   │   │   │   │   │   │   ├── register.cpython-35.pyc
│   │   │   │   │   │   │   ├── rotate.cpython-35.pyc
│   │   │   │   │   │   │   ├── saveopts.cpython-35.pyc
│   │   │   │   │   │   │   ├── sdist.cpython-35.pyc
│   │   │   │   │   │   │   ├── setopt.cpython-35.pyc
│   │   │   │   │   │   │   ├── test.cpython-35.pyc
│   │   │   │   │   │   │   ├── upload.cpython-35.pyc
│   │   │   │   │   │   │   ├── upload_docs.cpython-35.pyc
│   │   │   │   │   │   ├── register.py
│   │   │   │   │   │   ├── rotate.py
│   │   │   │   │   │   ├── saveopts.py
│   │   │   │   │   │   ├── sdist.py
│   │   │   │   │   │   ├── setopt.py
│   │   │   │   │   │   ├── test.py
│   │   │   │   │   │   ├── upload_docs.py
│   │   │   │   │   │   ├── upload.py
│   │   │   │   │   ├── depends.py
│   │   │   │   │   ├── dist.py
│   │   │   │   │   ├── extension.py
│   │   │   │   │   ├── extern
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── launch.py
│   │   │   │   │   ├── lib2to3_ex.py
│   │   │   │   │   ├── msvc9_support.py
│   │   │   │   │   ├── package_index.py
│   │   │   │   │   ├── py26compat.py
│   │   │   │   │   ├── py27compat.py
│   │   │   │   │   ├── py31compat.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── archive_util.cpython-35.pyc
│   │   │   │   │   │   ├── depends.cpython-35.pyc
│   │   │   │   │   │   ├── dist.cpython-35.pyc
│   │   │   │   │   │   ├── extension.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── launch.cpython-35.pyc
│   │   │   │   │   │   ├── lib2to3_ex.cpython-35.pyc
│   │   │   │   │   │   ├── msvc9_support.cpython-35.pyc
│   │   │   │   │   │   ├── package_index.cpython-35.pyc
│   │   │   │   │   │   ├── py26compat.cpython-35.pyc
│   │   │   │   │   │   ├── py27compat.cpython-35.pyc
│   │   │   │   │   │   ├── py31compat.cpython-35.pyc
│   │   │   │   │   │   ├── sandbox.cpython-35.pyc
│   │   │   │   │   │   ├── site-patch.cpython-35.pyc
│   │   │   │   │   │   ├── ssl_support.cpython-35.pyc
│   │   │   │   │   │   ├── unicode_utils.cpython-35.pyc
│   │   │   │   │   │   ├── utils.cpython-35.pyc
│   │   │   │   │   │   ├── version.cpython-35.pyc
│   │   │   │   │   │   ├── windows_support.cpython-35.pyc
│   │   │   │   │   ├── sandbox.py
│   │   │   │   │   ├── script
│   │   │   │   │   ├── (dev).tmpl
│   │   │   │   │   ├── script.tmpl
│   │   │   │   │   ├── site-patch.py
│   │   │   │   │   ├── ssl_support.py
│   │   │   │   │   ├── unicode_utils.py
│   │   │   │   │   ├── utils.py
│   │   │   │   │   ├── version.py
│   │   │   │   │   ├── windows_support.py
│   │   │   │   ├── setuptools-20.7.0.dist-info
│   │   │   │   │   ├── dependency_links.txt
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── entry_points.txt
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   │   │   │   │   ├── zip-safe
│   │   │   │   ├── urllib3
│   │   │   │   │   ├── _collections.py
│   │   │   │   │   ├── connectionpool.py
│   │   │   │   │   ├── connection.py
│   │   │   │   │   ├── contrib
│   │   │   │   │   │   ├── appengine.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── ntlmpool.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── appengine.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── ntlmpool.cpython-35.pyc
│   │   │   │   │   │   │   ├── pyopenssl.cpython-35.pyc
│   │   │   │   │   │   │   ├── securetransport.cpython-35.pyc
│   │   │   │   │   │   │   ├── socks.cpython-35.pyc
│   │   │   │   │   │   ├── pyopenssl.py
│   │   │   │   │   │   ├── _securetransport
│   │   │   │   │   │   │   ├── bindings.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── low_level.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── bindings.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── low_level.cpython-35.pyc
│   │   │   │   │   │   ├── securetransport.py
│   │   │   │   │   │   ├── socks.py
│   │   │   │   │   ├── exceptions.py
│   │   │   │   │   ├── fields.py
│   │   │   │   │   ├── filepost.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── packages
│   │   │   │   │   │   ├── backports
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── makefile.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── makefile.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── ordered_dict.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── ordered_dict.cpython-35.pyc
│   │   │   │   │   │   │   ├── six.cpython-35.pyc
│   │   │   │   │   │   ├── six.py
│   │   │   │   │   │   ├── ssl_match_hostname
│   │   │   │   │   │   │   ├── _implementation.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── _implementation.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── poolmanager.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── _collections.cpython-35.pyc
│   │   │   │   │   │   ├── connection.cpython-35.pyc
│   │   │   │   │   │   ├── connectionpool.cpython-35.pyc
│   │   │   │   │   │   ├── exceptions.cpython-35.pyc
│   │   │   │   │   │   ├── fields.cpython-35.pyc
│   │   │   │   │   │   ├── filepost.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── poolmanager.cpython-35.pyc
│   │   │   │   │   │   ├── request.cpython-35.pyc
│   │   │   │   │   │   ├── response.cpython-35.pyc
│   │   │   │   │   ├── request.py
│   │   │   │   │   ├── response.py
│   │   │   │   │   ├── util
│   │   │   │   │   │   ├── connection.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── connection.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── request.cpython-35.pyc
│   │   │   │   │   │   │   ├── response.cpython-35.pyc
│   │   │   │   │   │   │   ├── retry.cpython-35.pyc
│   │   │   │   │   │   │   ├── selectors.cpython-35.pyc
│   │   │   │   │   │   │   ├── ssl_.cpython-35.pyc
│   │   │   │   │   │   │   ├── timeout.cpython-35.pyc
│   │   │   │   │   │   │   ├── url.cpython-35.pyc
│   │   │   │   │   │   │   ├── wait.cpython-35.pyc
│   │   │   │   │   │   ├── request.py
│   │   │   │   │   │   ├── response.py
│   │   │   │   │   │   ├── retry.py
│   │   │   │   │   │   ├── selectors.py
│   │   │   │   │   │   ├── ssl_.py
│   │   │   │   │   │   ├── timeout.py
│   │   │   │   │   │   ├── url.py
│   │   │   │   │   │   ├── wait.py
│   │   │   │   ├── urllib3-1.22.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   ├── lib64
│   │   ├── python3.5
│   │   │   ├── site-packages
│   │   │   │   ├── certifi
│   │   │   │   │   ├── cacert.pem
│   │   │   │   │   ├── core.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── __main__.py
│   │   │   │   │   ├── old_root.pem
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── core.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── __main__.cpython-35.pyc
│   │   │   │   │   ├── weak.pem
│   │   │   │   ├── certifi-2017.4.17.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   │   │   │   ├── chardet
│   │   │   │   │   ├── big5freq.py
│   │   │   │   │   ├── big5prober.py
│   │   │   │   │   ├── chardistribution.py
│   │   │   │   │   ├── charsetgroupprober.py
│   │   │   │   │   ├── charsetprober.py
│   │   │   │   │   ├── cli
│   │   │   │   │   │   ├── chardetect.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── chardetect.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── codingstatemachine.py
│   │   │   │   │   ├── compat.py
│   │   │   │   │   ├── cp949prober.py
│   │   │   │   │   ├── enums.py
│   │   │   │   │   ├── escprober.py
│   │   │   │   │   ├── escsm.py
│   │   │   │   │   ├── eucjpprober.py
│   │   │   │   │   ├── euckrfreq.py
│   │   │   │   │   ├── euckrprober.py
│   │   │   │   │   ├── euctwfreq.py
│   │   │   │   │   ├── euctwprober.py
│   │   │   │   │   ├── gb2312freq.py
│   │   │   │   │   ├── gb2312prober.py
│   │   │   │   │   ├── hebrewprober.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── jisfreq.py
│   │   │   │   │   ├── jpcntx.py
│   │   │   │   │   ├── langbulgarianmodel.py
│   │   │   │   │   ├── langcyrillicmodel.py
│   │   │   │   │   ├── langgreekmodel.py
│   │   │   │   │   ├── langhebrewmodel.py
│   │   │   │   │   ├── langhungarianmodel.py
│   │   │   │   │   ├── langthaimodel.py
│   │   │   │   │   ├── langturkishmodel.py
│   │   │   │   │   ├── latin1prober.py
│   │   │   │   │   ├── mbcharsetprober.py
│   │   │   │   │   ├── mbcsgroupprober.py
│   │   │   │   │   ├── mbcssm.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── big5freq.cpython-35.pyc
│   │   │   │   │   │   ├── big5prober.cpython-35.pyc
│   │   │   │   │   │   ├── chardistribution.cpython-35.pyc
│   │   │   │   │   │   ├── charsetgroupprober.cpython-35.pyc
│   │   │   │   │   │   ├── charsetprober.cpython-35.pyc
│   │   │   │   │   │   ├── codingstatemachine.cpython-35.pyc
│   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   ├── cp949prober.cpython-35.pyc
│   │   │   │   │   │   ├── enums.cpython-35.pyc
│   │   │   │   │   │   ├── escprober.cpython-35.pyc
│   │   │   │   │   │   ├── escsm.cpython-35.pyc
│   │   │   │   │   │   ├── eucjpprober.cpython-35.pyc
│   │   │   │   │   │   ├── euckrfreq.cpython-35.pyc
│   │   │   │   │   │   ├── euckrprober.cpython-35.pyc
│   │   │   │   │   │   ├── euctwfreq.cpython-35.pyc
│   │   │   │   │   │   ├── euctwprober.cpython-35.pyc
│   │   │   │   │   │   ├── gb2312freq.cpython-35.pyc
│   │   │   │   │   │   ├── gb2312prober.cpython-35.pyc
│   │   │   │   │   │   ├── hebrewprober.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── jisfreq.cpython-35.pyc
│   │   │   │   │   │   ├── jpcntx.cpython-35.pyc
│   │   │   │   │   │   ├── langbulgarianmodel.cpython-35.pyc
│   │   │   │   │   │   ├── langcyrillicmodel.cpython-35.pyc
│   │   │   │   │   │   ├── langgreekmodel.cpython-35.pyc
│   │   │   │   │   │   ├── langhebrewmodel.cpython-35.pyc
│   │   │   │   │   │   ├── langhungarianmodel.cpython-35.pyc
│   │   │   │   │   │   ├── langthaimodel.cpython-35.pyc
│   │   │   │   │   │   ├── langturkishmodel.cpython-35.pyc
│   │   │   │   │   │   ├── latin1prober.cpython-35.pyc
│   │   │   │   │   │   ├── mbcharsetprober.cpython-35.pyc
│   │   │   │   │   │   ├── mbcsgroupprober.cpython-35.pyc
│   │   │   │   │   │   ├── mbcssm.cpython-35.pyc
│   │   │   │   │   │   ├── sbcharsetprober.cpython-35.pyc
│   │   │   │   │   │   ├── sbcsgroupprober.cpython-35.pyc
│   │   │   │   │   │   ├── sjisprober.cpython-35.pyc
│   │   │   │   │   │   ├── universaldetector.cpython-35.pyc
│   │   │   │   │   │   ├── utf8prober.cpython-35.pyc
│   │   │   │   │   │   ├── version.cpython-35.pyc
│   │   │   │   │   ├── sbcharsetprober.py
│   │   │   │   │   ├── sbcsgroupprober.py
│   │   │   │   │   ├── sjisprober.py
│   │   │   │   │   ├── universaldetector.py
│   │   │   │   │   ├── utf8prober.py
│   │   │   │   │   ├── version.py
│   │   │   │   ├── chardet-3.0.4.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── entry_points.txt
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   │   │   │   ├── easy_install.py
│   │   │   │   ├── idna
│   │   │   │   │   ├── codec.py
│   │   │   │   │   ├── compat.py
│   │   │   │   │   ├── core.py
│   │   │   │   │   ├── idnadata.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── intranges.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── codec.cpython-35.pyc
│   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   ├── core.cpython-35.pyc
│   │   │   │   │   │   ├── idnadata.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── intranges.cpython-35.pyc
│   │   │   │   │   │   ├── uts46data.cpython-35.pyc
│   │   │   │   │   ├── uts46data.py
│   │   │   │   ├── idna-2.5.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── pbr.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   │   │   │   ├── pip
│   │   │   │   │   ├── basecommand.py
│   │   │   │   │   ├── baseparser.py
│   │   │   │   │   ├── cmdoptions.py
│   │   │   │   │   ├── commands
│   │   │   │   │   │   ├── check.py
│   │   │   │   │   │   ├── completion.py
│   │   │   │   │   │   ├── download.py
│   │   │   │   │   │   ├── freeze.py
│   │   │   │   │   │   ├── hash.py
│   │   │   │   │   │   ├── help.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── install.py
│   │   │   │   │   │   ├── list.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── check.cpython-35.pyc
│   │   │   │   │   │   │   ├── completion.cpython-35.pyc
│   │   │   │   │   │   │   ├── download.cpython-35.pyc
│   │   │   │   │   │   │   ├── freeze.cpython-35.pyc
│   │   │   │   │   │   │   ├── hash.cpython-35.pyc
│   │   │   │   │   │   │   ├── help.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── install.cpython-35.pyc
│   │   │   │   │   │   │   ├── list.cpython-35.pyc
│   │   │   │   │   │   │   ├── search.cpython-35.pyc
│   │   │   │   │   │   │   ├── show.cpython-35.pyc
│   │   │   │   │   │   │   ├── uninstall.cpython-35.pyc
│   │   │   │   │   │   │   ├── wheel.cpython-35.pyc
│   │   │   │   │   │   ├── search.py
│   │   │   │   │   │   ├── show.py
│   │   │   │   │   │   ├── uninstall.py
│   │   │   │   │   │   ├── wheel.py
│   │   │   │   │   ├── compat
│   │   │   │   │   │   ├── dictconfig.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── dictconfig.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── download.py
│   │   │   │   │   ├── exceptions.py
│   │   │   │   │   ├── index.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── locations.py
│   │   │   │   │   ├── __main__.py
│   │   │   │   │   ├── models
│   │   │   │   │   │   ├── index.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── index.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── operations
│   │   │   │   │   │   ├── check.py
│   │   │   │   │   │   ├── freeze.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── check.cpython-35.pyc
│   │   │   │   │   │   │   ├── freeze.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── pep425tags.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── basecommand.cpython-35.pyc
│   │   │   │   │   │   ├── baseparser.cpython-35.pyc
│   │   │   │   │   │   ├── cmdoptions.cpython-35.pyc
│   │   │   │   │   │   ├── download.cpython-35.pyc
│   │   │   │   │   │   ├── exceptions.cpython-35.pyc
│   │   │   │   │   │   ├── index.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── locations.cpython-35.pyc
│   │   │   │   │   │   ├── __main__.cpython-35.pyc
│   │   │   │   │   │   ├── pep425tags.cpython-35.pyc
│   │   │   │   │   │   ├── status_codes.cpython-35.pyc
│   │   │   │   │   │   ├── wheel.cpython-35.pyc
│   │   │   │   │   ├── req
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── req_file.cpython-35.pyc
│   │   │   │   │   │   │   ├── req_install.cpython-35.pyc
│   │   │   │   │   │   │   ├── req_set.cpython-35.pyc
│   │   │   │   │   │   │   ├── req_uninstall.cpython-35.pyc
│   │   │   │   │   │   ├── req_file.py
│   │   │   │   │   │   ├── req_install.py
│   │   │   │   │   │   ├── req_set.py
│   │   │   │   │   │   ├── req_uninstall.py
│   │   │   │   │   ├── status_codes.py
│   │   │   │   │   ├── utils
│   │   │   │   │   │   ├── appdirs.py
│   │   │   │   │   │   ├── build.py
│   │   │   │   │   │   ├── deprecation.py
│   │   │   │   │   │   ├── encoding.py
│   │   │   │   │   │   ├── filesystem.py
│   │   │   │   │   │   ├── glibc.py
│   │   │   │   │   │   ├── hashes.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── logging.py
│   │   │   │   │   │   ├── outdated.py
│   │   │   │   │   │   ├── packaging.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── appdirs.cpython-35.pyc
│   │   │   │   │   │   │   ├── build.cpython-35.pyc
│   │   │   │   │   │   │   ├── deprecation.cpython-35.pyc
│   │   │   │   │   │   │   ├── encoding.cpython-35.pyc
│   │   │   │   │   │   │   ├── filesystem.cpython-35.pyc
│   │   │   │   │   │   │   ├── glibc.cpython-35.pyc
│   │   │   │   │   │   │   ├── hashes.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── logging.cpython-35.pyc
│   │   │   │   │   │   │   ├── outdated.cpython-35.pyc
│   │   │   │   │   │   │   ├── packaging.cpython-35.pyc
│   │   │   │   │   │   │   ├── setuptools_build.cpython-35.pyc
│   │   │   │   │   │   │   ├── ui.cpython-35.pyc
│   │   │   │   │   │   ├── setuptools_build.py
│   │   │   │   │   │   ├── ui.py
│   │   │   │   │   ├── vcs
│   │   │   │   │   │   ├── bazaar.py
│   │   │   │   │   │   ├── git.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── mercurial.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── bazaar.cpython-35.pyc
│   │   │   │   │   │   │   ├── git.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── mercurial.cpython-35.pyc
│   │   │   │   │   │   │   ├── subversion.cpython-35.pyc
│   │   │   │   │   │   ├── subversion.py
│   │   │   │   │   ├── _vendor
│   │   │   │   │   │   ├── appdirs.py
│   │   │   │   │   │   ├── cachecontrol
│   │   │   │   │   │   │   ├── adapter.py
│   │   │   │   │   │   │   ├── cache.py
│   │   │   │   │   │   │   ├── caches
│   │   │   │   │   │   │   │   ├── file_cache.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── file_cache.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── redis_cache.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── redis_cache.py
│   │   │   │   │   │   │   ├── _cmd.py
│   │   │   │   │   │   │   ├── compat.py
│   │   │   │   │   │   │   ├── controller.py
│   │   │   │   │   │   │   ├── filewrapper.py
│   │   │   │   │   │   │   ├── heuristics.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── adapter.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── cache.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _cmd.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── controller.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── filewrapper.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── heuristics.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── serialize.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── wrapper.cpython-35.pyc
│   │   │   │   │   │   │   ├── serialize.py
│   │   │   │   │   │   │   ├── wrapper.py
│   │   │   │   │   │   ├── colorama
│   │   │   │   │   │   │   ├── ansi.py
│   │   │   │   │   │   │   ├── ansitowin32.py
│   │   │   │   │   │   │   ├── initialise.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── ansi.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── ansitowin32.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── initialise.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── win32.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── winterm.cpython-35.pyc
│   │   │   │   │   │   │   ├── win32.py
│   │   │   │   │   │   │   ├── winterm.py
│   │   │   │   │   │   ├── distlib
│   │   │   │   │   │   │   ├── _backport
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── misc.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── misc.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── shutil.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── sysconfig.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── tarfile.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── shutil.py
│   │   │   │   │   │   │   │   ├── sysconfig.cfg
│   │   │   │   │   │   │   │   ├── sysconfig.py
│   │   │   │   │   │   │   │   ├── tarfile.py
│   │   │   │   │   │   │   ├── compat.py
│   │   │   │   │   │   │   ├── database.py
│   │   │   │   │   │   │   ├── index.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── locators.py
│   │   │   │   │   │   │   ├── manifest.py
│   │   │   │   │   │   │   ├── markers.py
│   │   │   │   │   │   │   ├── metadata.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── database.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── index.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── locators.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── manifest.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── markers.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── metadata.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── resources.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── scripts.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── util.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── version.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── wheel.cpython-35.pyc
│   │   │   │   │   │   │   ├── resources.py
│   │   │   │   │   │   │   ├── scripts.py
│   │   │   │   │   │   │   ├── t32.exe
│   │   │   │   │   │   │   ├── t64.exe
│   │   │   │   │   │   │   ├── util.py
│   │   │   │   │   │   │   ├── version.py
│   │   │   │   │   │   │   ├── w32.exe
│   │   │   │   │   │   │   ├── w64.exe
│   │   │   │   │   │   │   ├── wheel.py
│   │   │   │   │   │   ├── distro.py
│   │   │   │   │   │   ├── html5lib
│   │   │   │   │   │   │   ├── constants.py
│   │   │   │   │   │   │   ├── filters
│   │   │   │   │   │   │   │   ├── alphabeticalattributes.py
│   │   │   │   │   │   │   │   ├── base.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── inject_meta_charset.py
│   │   │   │   │   │   │   │   ├── lint.py
│   │   │   │   │   │   │   │   ├── optionaltags.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── alphabeticalattributes.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── base.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── inject_meta_charset.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── lint.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── optionaltags.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── sanitizer.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── whitespace.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── sanitizer.py
│   │   │   │   │   │   │   │   ├── whitespace.py
│   │   │   │   │   │   │   ├── html5parser.py
│   │   │   │   │   │   │   ├── _ihatexml.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── _inputstream.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── constants.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── html5parser.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _ihatexml.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _inputstream.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── serializer.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _tokenizer.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _utils.cpython-35.pyc
│   │   │   │   │   │   │   ├── serializer.py
│   │   │   │   │   │   │   ├── _tokenizer.py
│   │   │   │   │   │   │   ├── treeadapters
│   │   │   │   │   │   │   │   ├── genshi.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── genshi.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── sax.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── sax.py
│   │   │   │   │   │   │   ├── treebuilders
│   │   │   │   │   │   │   │   ├── base.py
│   │   │   │   │   │   │   │   ├── dom.py
│   │   │   │   │   │   │   │   ├── etree_lxml.py
│   │   │   │   │   │   │   │   ├── etree.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── base.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── dom.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── etree.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── etree_lxml.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── treewalkers
│   │   │   │   │   │   │   │   ├── base.py
│   │   │   │   │   │   │   │   ├── dom.py
│   │   │   │   │   │   │   │   ├── etree_lxml.py
│   │   │   │   │   │   │   │   ├── etree.py
│   │   │   │   │   │   │   │   ├── genshi.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── base.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── dom.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── etree.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── etree_lxml.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── genshi.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── _trie
│   │   │   │   │   │   │   │   ├── _base.py
│   │   │   │   │   │   │   │   ├── datrie.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── _base.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── datrie.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── py.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── py.py
│   │   │   │   │   │   │   ├── _utils.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── ipaddress.py
│   │   │   │   │   │   ├── lockfile
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── linklockfile.py
│   │   │   │   │   │   │   ├── mkdirlockfile.py
│   │   │   │   │   │   │   ├── pidlockfile.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── linklockfile.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── mkdirlockfile.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── pidlockfile.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── sqlitelockfile.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── symlinklockfile.cpython-35.pyc
│   │   │   │   │   │   │   ├── sqlitelockfile.py
│   │   │   │   │   │   │   ├── symlinklockfile.py
│   │   │   │   │   │   ├── ordereddict.py
│   │   │   │   │   │   ├── packaging
│   │   │   │   │   │   │   ├── __about__.py
│   │   │   │   │   │   │   ├── _compat.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── markers.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── __about__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _compat.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── markers.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── requirements.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── specifiers.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _structures.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── utils.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── version.cpython-35.pyc
│   │   │   │   │   │   │   ├── requirements.py
│   │   │   │   │   │   │   ├── specifiers.py
│   │   │   │   │   │   │   ├── _structures.py
│   │   │   │   │   │   │   ├── utils.py
│   │   │   │   │   │   │   ├── version.py
│   │   │   │   │   │   ├── pkg_resources
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── progress
│   │   │   │   │   │   │   ├── bar.py
│   │   │   │   │   │   │   ├── counter.py
│   │   │   │   │   │   │   ├── helpers.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── bar.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── counter.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── helpers.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── spinner.cpython-35.pyc
│   │   │   │   │   │   │   ├── spinner.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── appdirs.cpython-35.pyc
│   │   │   │   │   │   │   ├── distro.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── ipaddress.cpython-35.pyc
│   │   │   │   │   │   │   ├── ordereddict.cpython-35.pyc
│   │   │   │   │   │   │   ├── pyparsing.cpython-35.pyc
│   │   │   │   │   │   │   ├── retrying.cpython-35.pyc
│   │   │   │   │   │   │   ├── re-vendor.cpython-35.pyc
│   │   │   │   │   │   │   ├── six.cpython-35.pyc
│   │   │   │   │   │   ├── pyparsing.py
│   │   │   │   │   │   ├── requests
│   │   │   │   │   │   │   ├── adapters.py
│   │   │   │   │   │   │   ├── api.py
│   │   │   │   │   │   │   ├── auth.py
│   │   │   │   │   │   │   ├── cacert.pem
│   │   │   │   │   │   │   ├── certs.py
│   │   │   │   │   │   │   ├── compat.py
│   │   │   │   │   │   │   ├── cookies.py
│   │   │   │   │   │   │   ├── exceptions.py
│   │   │   │   │   │   │   ├── hooks.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── models.py
│   │   │   │   │   │   │   ├── packages
│   │   │   │   │   │   │   │   ├── chardet
│   │   │   │   │   │   │   │   │   ├── big5freq.py
│   │   │   │   │   │   │   │   │   ├── big5prober.py
│   │   │   │   │   │   │   │   │   ├── chardetect.py
│   │   │   │   │   │   │   │   │   ├── chardistribution.py
│   │   │   │   │   │   │   │   │   ├── charsetgroupprober.py
│   │   │   │   │   │   │   │   │   ├── charsetprober.py
│   │   │   │   │   │   │   │   │   ├── codingstatemachine.py
│   │   │   │   │   │   │   │   │   ├── compat.py
│   │   │   │   │   │   │   │   │   ├── constants.py
│   │   │   │   │   │   │   │   │   ├── cp949prober.py
│   │   │   │   │   │   │   │   │   ├── escprober.py
│   │   │   │   │   │   │   │   │   ├── escsm.py
│   │   │   │   │   │   │   │   │   ├── eucjpprober.py
│   │   │   │   │   │   │   │   │   ├── euckrfreq.py
│   │   │   │   │   │   │   │   │   ├── euckrprober.py
│   │   │   │   │   │   │   │   │   ├── euctwfreq.py
│   │   │   │   │   │   │   │   │   ├── euctwprober.py
│   │   │   │   │   │   │   │   │   ├── gb2312freq.py
│   │   │   │   │   │   │   │   │   ├── gb2312prober.py
│   │   │   │   │   │   │   │   │   ├── hebrewprober.py
│   │   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   │   ├── jisfreq.py
│   │   │   │   │   │   │   │   │   ├── jpcntx.py
│   │   │   │   │   │   │   │   │   ├── langbulgarianmodel.py
│   │   │   │   │   │   │   │   │   ├── langcyrillicmodel.py
│   │   │   │   │   │   │   │   │   ├── langgreekmodel.py
│   │   │   │   │   │   │   │   │   ├── langhebrewmodel.py
│   │   │   │   │   │   │   │   │   ├── langhungarianmodel.py
│   │   │   │   │   │   │   │   │   ├── langthaimodel.py
│   │   │   │   │   │   │   │   │   ├── latin1prober.py
│   │   │   │   │   │   │   │   │   ├── mbcharsetprober.py
│   │   │   │   │   │   │   │   │   ├── mbcsgroupprober.py
│   │   │   │   │   │   │   │   │   ├── mbcssm.py
│   │   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   │   ├── big5freq.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── big5prober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── chardetect.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── chardistribution.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── charsetgroupprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── charsetprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── codingstatemachine.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── constants.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── cp949prober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── escprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── escsm.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── eucjpprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── euckrfreq.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── euckrprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── euctwfreq.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── euctwprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── gb2312freq.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── gb2312prober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── hebrewprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── jisfreq.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── jpcntx.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── langbulgarianmodel.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── langcyrillicmodel.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── langgreekmodel.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── langhebrewmodel.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── langhungarianmodel.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── langthaimodel.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── latin1prober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── mbcharsetprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── mbcsgroupprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── mbcssm.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── sbcharsetprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── sbcsgroupprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── sjisprober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── universaldetector.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── utf8prober.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── sbcharsetprober.py
│   │   │   │   │   │   │   │   │   ├── sbcsgroupprober.py
│   │   │   │   │   │   │   │   │   ├── sjisprober.py
│   │   │   │   │   │   │   │   │   ├── universaldetector.py
│   │   │   │   │   │   │   │   │   ├── utf8prober.py
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── urllib3
│   │   │   │   │   │   │   │   │   ├── _collections.py
│   │   │   │   │   │   │   │   │   ├── connectionpool.py
│   │   │   │   │   │   │   │   │   ├── connection.py
│   │   │   │   │   │   │   │   │   ├── contrib
│   │   │   │   │   │   │   │   │   │   ├── appengine.py
│   │   │   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   │   │   ├── ntlmpool.py
│   │   │   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   │   │   ├── appengine.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── ntlmpool.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── pyopenssl.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── socks.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── pyopenssl.py
│   │   │   │   │   │   │   │   │   │   ├── socks.py
│   │   │   │   │   │   │   │   │   ├── exceptions.py
│   │   │   │   │   │   │   │   │   ├── fields.py
│   │   │   │   │   │   │   │   │   ├── filepost.py
│   │   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   │   ├── packages
│   │   │   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   │   │   ├── ordered_dict.py
│   │   │   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── ordered_dict.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── six.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── six.py
│   │   │   │   │   │   │   │   │   │   ├── ssl_match_hostname
│   │   │   │   │   │   │   │   │   │   │   ├── _implementation.py
│   │   │   │   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   │   │   │   ├── _implementation.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── poolmanager.py
│   │   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   │   ├── _collections.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── connection.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── connectionpool.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── exceptions.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── fields.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── filepost.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── poolmanager.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── request.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── response.cpython-35.pyc
│   │   │   │   │   │   │   │   │   ├── request.py
│   │   │   │   │   │   │   │   │   ├── response.py
│   │   │   │   │   │   │   │   │   ├── util
│   │   │   │   │   │   │   │   │   │   ├── connection.py
│   │   │   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   │   │   │   ├── connection.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── request.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── response.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── retry.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── ssl_.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── timeout.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   │   ├── url.cpython-35.pyc
│   │   │   │   │   │   │   │   │   │   ├── request.py
│   │   │   │   │   │   │   │   │   │   ├── response.py
│   │   │   │   │   │   │   │   │   │   ├── retry.py
│   │   │   │   │   │   │   │   │   │   ├── ssl_.py
│   │   │   │   │   │   │   │   │   │   ├── timeout.py
│   │   │   │   │   │   │   │   │   │   ├── url.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── adapters.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── api.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── auth.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── certs.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── cookies.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── exceptions.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── hooks.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── models.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── sessions.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── status_codes.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── structures.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── utils.cpython-35.pyc
│   │   │   │   │   │   │   ├── sessions.py
│   │   │   │   │   │   │   ├── status_codes.py
│   │   │   │   │   │   │   ├── structures.py
│   │   │   │   │   │   │   ├── utils.py
│   │   │   │   │   │   ├── retrying.py
│   │   │   │   │   │   ├── re-vendor.py
│   │   │   │   │   │   ├── six.py
│   │   │   │   │   │   ├── webencodings
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── labels.py
│   │   │   │   │   │   │   ├── mklabels.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── labels.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── mklabels.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── tests.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── x_user_defined.cpython-35.pyc
│   │   │   │   │   │   │   ├── tests.py
│   │   │   │   │   │   │   ├── x_user_defined.py
│   │   │   │   │   ├── wheel.py
│   │   │   │   ├── pip-9.0.1.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── entry_points.txt
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   │   │   │   ├── pkg_resources
│   │   │   │   │   ├── extern
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── _vendor
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── packaging
│   │   │   │   │   │   │   ├── __about__.py
│   │   │   │   │   │   │   ├── _compat.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── markers.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── __about__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _compat.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── markers.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── requirements.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── specifiers.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── _structures.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── utils.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── version.cpython-35.pyc
│   │   │   │   │   │   │   ├── requirements.py
│   │   │   │   │   │   │   ├── specifiers.py
│   │   │   │   │   │   │   ├── _structures.py
│   │   │   │   │   │   │   ├── utils.py
│   │   │   │   │   │   │   ├── version.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── pyparsing.cpython-35.pyc
│   │   │   │   │   │   │   ├── six.cpython-35.pyc
│   │   │   │   │   │   ├── pyparsing.py
│   │   │   │   │   │   ├── six.py
│   │   │   │   ├── pkg_resources-0.0.0.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── WHEEL
│   │   │   │   ├── __pycache__
│   │   │   │   │   ├── easy_install.cpython-35.pyc
│   │   │   │   ├── requests
│   │   │   │   │   ├── adapters.py
│   │   │   │   │   ├── api.py
│   │   │   │   │   ├── auth.py
│   │   │   │   │   ├── certs.py
│   │   │   │   │   ├── compat.py
│   │   │   │   │   ├── cookies.py
│   │   │   │   │   ├── exceptions.py
│   │   │   │   │   ├── help.py
│   │   │   │   │   ├── hooks.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _internal_utils.py
│   │   │   │   │   ├── models.py
│   │   │   │   │   ├── packages.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── adapters.cpython-35.pyc
│   │   │   │   │   │   ├── api.cpython-35.pyc
│   │   │   │   │   │   ├── auth.cpython-35.pyc
│   │   │   │   │   │   ├── certs.cpython-35.pyc
│   │   │   │   │   │   ├── compat.cpython-35.pyc
│   │   │   │   │   │   ├── cookies.cpython-35.pyc
│   │   │   │   │   │   ├── exceptions.cpython-35.pyc
│   │   │   │   │   │   ├── help.cpython-35.pyc
│   │   │   │   │   │   ├── hooks.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── _internal_utils.cpython-35.pyc
│   │   │   │   │   │   ├── models.cpython-35.pyc
│   │   │   │   │   │   ├── packages.cpython-35.pyc
│   │   │   │   │   │   ├── sessions.cpython-35.pyc
│   │   │   │   │   │   ├── status_codes.cpython-35.pyc
│   │   │   │   │   │   ├── structures.cpython-35.pyc
│   │   │   │   │   │   ├── utils.cpython-35.pyc
│   │   │   │   │   │   ├── __version__.cpython-35.pyc
│   │   │   │   │   ├── sessions.py
│   │   │   │   │   ├── status_codes.py
│   │   │   │   │   ├── structures.py
│   │   │   │   │   ├── utils.py
│   │   │   │   │   ├── __version__.py
│   │   │   │   ├── requests-2.18.2.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   │   │   │   ├── setuptools
│   │   │   │   │   ├── archive_util.py
│   │   │   │   │   ├── command
│   │   │   │   │   │   ├── alias.py
│   │   │   │   │   │   ├── bdist_egg.py
│   │   │   │   │   │   ├── bdist_rpm.py
│   │   │   │   │   │   ├── bdist_wininst.py
│   │   │   │   │   │   ├── build_ext.py
│   │   │   │   │   │   ├── build_py.py
│   │   │   │   │   │   ├── develop.py
│   │   │   │   │   │   ├── easy_install.py
│   │   │   │   │   │   ├── egg_info.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── install_egg_info.py
│   │   │   │   │   │   ├── install_lib.py
│   │   │   │   │   │   ├── install.py
│   │   │   │   │   │   ├── install_scripts.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── alias.cpython-35.pyc
│   │   │   │   │   │   │   ├── bdist_egg.cpython-35.pyc
│   │   │   │   │   │   │   ├── bdist_rpm.cpython-35.pyc
│   │   │   │   │   │   │   ├── bdist_wininst.cpython-35.pyc
│   │   │   │   │   │   │   ├── build_ext.cpython-35.pyc
│   │   │   │   │   │   │   ├── build_py.cpython-35.pyc
│   │   │   │   │   │   │   ├── develop.cpython-35.pyc
│   │   │   │   │   │   │   ├── easy_install.cpython-35.pyc
│   │   │   │   │   │   │   ├── egg_info.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── install.cpython-35.pyc
│   │   │   │   │   │   │   ├── install_egg_info.cpython-35.pyc
│   │   │   │   │   │   │   ├── install_lib.cpython-35.pyc
│   │   │   │   │   │   │   ├── install_scripts.cpython-35.pyc
│   │   │   │   │   │   │   ├── register.cpython-35.pyc
│   │   │   │   │   │   │   ├── rotate.cpython-35.pyc
│   │   │   │   │   │   │   ├── saveopts.cpython-35.pyc
│   │   │   │   │   │   │   ├── sdist.cpython-35.pyc
│   │   │   │   │   │   │   ├── setopt.cpython-35.pyc
│   │   │   │   │   │   │   ├── test.cpython-35.pyc
│   │   │   │   │   │   │   ├── upload.cpython-35.pyc
│   │   │   │   │   │   │   ├── upload_docs.cpython-35.pyc
│   │   │   │   │   │   ├── register.py
│   │   │   │   │   │   ├── rotate.py
│   │   │   │   │   │   ├── saveopts.py
│   │   │   │   │   │   ├── sdist.py
│   │   │   │   │   │   ├── setopt.py
│   │   │   │   │   │   ├── test.py
│   │   │   │   │   │   ├── upload_docs.py
│   │   │   │   │   │   ├── upload.py
│   │   │   │   │   ├── depends.py
│   │   │   │   │   ├── dist.py
│   │   │   │   │   ├── extension.py
│   │   │   │   │   ├── extern
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── launch.py
│   │   │   │   │   ├── lib2to3_ex.py
│   │   │   │   │   ├── msvc9_support.py
│   │   │   │   │   ├── package_index.py
│   │   │   │   │   ├── py26compat.py
│   │   │   │   │   ├── py27compat.py
│   │   │   │   │   ├── py31compat.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── archive_util.cpython-35.pyc
│   │   │   │   │   │   ├── depends.cpython-35.pyc
│   │   │   │   │   │   ├── dist.cpython-35.pyc
│   │   │   │   │   │   ├── extension.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── launch.cpython-35.pyc
│   │   │   │   │   │   ├── lib2to3_ex.cpython-35.pyc
│   │   │   │   │   │   ├── msvc9_support.cpython-35.pyc
│   │   │   │   │   │   ├── package_index.cpython-35.pyc
│   │   │   │   │   │   ├── py26compat.cpython-35.pyc
│   │   │   │   │   │   ├── py27compat.cpython-35.pyc
│   │   │   │   │   │   ├── py31compat.cpython-35.pyc
│   │   │   │   │   │   ├── sandbox.cpython-35.pyc
│   │   │   │   │   │   ├── site-patch.cpython-35.pyc
│   │   │   │   │   │   ├── ssl_support.cpython-35.pyc
│   │   │   │   │   │   ├── unicode_utils.cpython-35.pyc
│   │   │   │   │   │   ├── utils.cpython-35.pyc
│   │   │   │   │   │   ├── version.cpython-35.pyc
│   │   │   │   │   │   ├── windows_support.cpython-35.pyc
│   │   │   │   │   ├── sandbox.py
│   │   │   │   │   ├── script
│   │   │   │   │   ├── (dev).tmpl
│   │   │   │   │   ├── script.tmpl
│   │   │   │   │   ├── site-patch.py
│   │   │   │   │   ├── ssl_support.py
│   │   │   │   │   ├── unicode_utils.py
│   │   │   │   │   ├── utils.py
│   │   │   │   │   ├── version.py
│   │   │   │   │   ├── windows_support.py
│   │   │   │   ├── setuptools-20.7.0.dist-info
│   │   │   │   │   ├── dependency_links.txt
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── entry_points.txt
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   │   │   │   │   ├── zip-safe
│   │   │   │   ├── urllib3
│   │   │   │   │   ├── _collections.py
│   │   │   │   │   ├── connectionpool.py
│   │   │   │   │   ├── connection.py
│   │   │   │   │   ├── contrib
│   │   │   │   │   │   ├── appengine.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── ntlmpool.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── appengine.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── ntlmpool.cpython-35.pyc
│   │   │   │   │   │   │   ├── pyopenssl.cpython-35.pyc
│   │   │   │   │   │   │   ├── securetransport.cpython-35.pyc
│   │   │   │   │   │   │   ├── socks.cpython-35.pyc
│   │   │   │   │   │   ├── pyopenssl.py
│   │   │   │   │   │   ├── _securetransport
│   │   │   │   │   │   │   ├── bindings.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── low_level.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── bindings.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── low_level.cpython-35.pyc
│   │   │   │   │   │   ├── securetransport.py
│   │   │   │   │   │   ├── socks.py
│   │   │   │   │   ├── exceptions.py
│   │   │   │   │   ├── fields.py
│   │   │   │   │   ├── filepost.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── packages
│   │   │   │   │   │   ├── backports
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── makefile.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── makefile.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── ordered_dict.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── ordered_dict.cpython-35.pyc
│   │   │   │   │   │   │   ├── six.cpython-35.pyc
│   │   │   │   │   │   ├── six.py
│   │   │   │   │   │   ├── ssl_match_hostname
│   │   │   │   │   │   │   ├── _implementation.py
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   │   ├── _implementation.cpython-35.pyc
│   │   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   ├── poolmanager.py
│   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   ├── _collections.cpython-35.pyc
│   │   │   │   │   │   ├── connection.cpython-35.pyc
│   │   │   │   │   │   ├── connectionpool.cpython-35.pyc
│   │   │   │   │   │   ├── exceptions.cpython-35.pyc
│   │   │   │   │   │   ├── fields.cpython-35.pyc
│   │   │   │   │   │   ├── filepost.cpython-35.pyc
│   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   ├── poolmanager.cpython-35.pyc
│   │   │   │   │   │   ├── request.cpython-35.pyc
│   │   │   │   │   │   ├── response.cpython-35.pyc
│   │   │   │   │   ├── request.py
│   │   │   │   │   ├── response.py
│   │   │   │   │   ├── util
│   │   │   │   │   │   ├── connection.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __pycache__
│   │   │   │   │   │   │   ├── connection.cpython-35.pyc
│   │   │   │   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   │   │   │   ├── request.cpython-35.pyc
│   │   │   │   │   │   │   ├── response.cpython-35.pyc
│   │   │   │   │   │   │   ├── retry.cpython-35.pyc
│   │   │   │   │   │   │   ├── selectors.cpython-35.pyc
│   │   │   │   │   │   │   ├── ssl_.cpython-35.pyc
│   │   │   │   │   │   │   ├── timeout.cpython-35.pyc
│   │   │   │   │   │   │   ├── url.cpython-35.pyc
│   │   │   │   │   │   │   ├── wait.cpython-35.pyc
│   │   │   │   │   │   ├── request.py
│   │   │   │   │   │   ├── response.py
│   │   │   │   │   │   ├── retry.py
│   │   │   │   │   │   ├── selectors.py
│   │   │   │   │   │   ├── ssl_.py
│   │   │   │   │   │   ├── timeout.py
│   │   │   │   │   │   ├── url.py
│   │   │   │   │   │   ├── wait.py
│   │   │   │   ├── urllib3-1.22.dist-info
│   │   │   │   │   ├── DESCRIPTION.rst
│   │   │   │   │   ├── INSTALLER
│   │   │   │   │   ├── METADATA
│   │   │   │   │   ├── metadata.json
│   │   │   │   │   ├── RECORD
│   │   │   │   │   ├── top_level.txt
│   │   │   │   │   ├── WHEEL
│   ├── pip.conf
│   ├── pip-selfcheck.json
│   ├── pyvenv.cfg
│   ├── share
│   │   ├── python-wheels
│   │   │   ├── CacheControl-0.11.5-py2.py3-none-any.whl
│   │   │   ├── chardet-2.3.0-py2.py3-none-any.whl
│   │   │   ├── colorama-0.3.7-py2.py3-none-any.whl
│   │   │   ├── distlib-0.2.2-py2.py3-none-any.whl
│   │   │   ├── html5lib-0.999-py2.py3-none-any.whl
│   │   │   ├── ipaddress-0.0.0-py2.py3-none-any.whl
│   │   │   ├── lockfile-0.12.2-py2.py3-none-any.whl
│   │   │   ├── packaging-16.6-py2.py3-none-any.whl
│   │   │   ├── pip-8.1.1-py2.py3-none-any.whl
│   │   │   ├── pkg_resources-0.0.0-py2.py3-none-any.whl
│   │   │   ├── progress-1.2-py2.py3-none-any.whl
│   │   │   ├── pyparsing-2.0.3-py2.py3-none-any.whl
│   │   │   ├── requests-2.9.1-py2.py3-none-any.whl
│   │   │   ├── retrying-1.3.3-py2.py3-none-any.whl
│   │   │   ├── setuptools-20.7.0-py2.py3-none-any.whl
│   │   │   ├── six-1.10.0-py2.py3-none-any.whl
│   │   │   ├── urllib3-1.13.1-py2.py3-none-any.whl
│   │   │   ├── wheel-0.29.0-py2.py3-none-any.whl
├── README.md
├── requirements_py.txt
├── src
│   ├── helpers.js
│   ├── ns.json
│   ├── serve.py
│   ├── XMLReqs
│   │   ├── getCPEpartNumber.xml
│   │   ├── getCPEsByManagedGroup.xml
│   │   ├── getCPEVolumes.xml
│   │   ├── getElementPerformance.xml
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
│   ├── setup_for_py3.sh
│   ├── setup_for_py3_win.sh
│   ├── sitemap.md
│   ├── updatereadme.sh
│   ├── writemap.sh
│   ├── WSDL
│   │   ├── cpeService.xml
│   │   ├── elementsInformationService.xml
│   │   ├── multiCastService.xml
│   │   ├── qosService.xml
```
