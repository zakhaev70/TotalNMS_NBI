home='..'
if [[ $# -ge 1 ]]; then
    home=$1;
fi
cat $home/tools/readmetxt.md > $home/README.md;
source $home/tools/writemap.sh;  #runs important part, without output to console
cat $home/tools/sitemap.md >> $home/README.md;
