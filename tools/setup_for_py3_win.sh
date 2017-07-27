### Installs all Python 3 requirements on Windows ###
#Check before running, make sure it won't cause any issues
python -m venv __pyvenv__;
. __pyvenv__/Scripts/activate; #specific to bash, check docs for more
pip install --upgrade pip;
pip install -r requirements_py.txt;
pip install requests;  #we know it is required, so just in case previous line gives error
