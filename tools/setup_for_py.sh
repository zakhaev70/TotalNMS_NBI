### Installs all Python 3 requirements ###
#Check before running, make sure it won't cause any issues
sudo apt-get install python3;  #comment out if not on Linux or permission errors
python3 -m venv __pyvenv__;
source __pyvenv__/bin/activate;  #specific to bash, check docs for more
pip install -r requirements_py.txt
