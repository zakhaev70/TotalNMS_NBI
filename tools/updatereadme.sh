### Updates requirements_py.txt ###
source __pyvenv__/bin/activate  #comment out if you wish
pip freeze -l > requirements_py.txt

### Updates README.md with new text and sitemap ###
home='..'
if [[ $# -ge 1 ]]; then
    home=$1;
fi
cat $home/tools/readmetxt.md > $home/README.md;
source $home/tools/writemap.sh;
writemap $home/tools  #runs important part, without output to console
cat $home/tools/sitemap.md >> $home/README.md;
