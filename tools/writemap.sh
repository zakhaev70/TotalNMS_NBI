outfile="sitemap.md";

function writemap() {
    local dir="..";
    local tab="├── ";
    if [[ $# -ge 1 ]]; then
        dir=$1;
    fi
    if [[ $# -ge 2 ]]; then
        tab="│   "$2;
    fi
    
    SAVEIFS=$IFS;
    IFS=$(echo -en "\n\b");
    for f in `ls -A $dir`; do
        filename=$( basename "${f}" );
        if [[ $filename != ".git" ]]; then
            echo "${tab}${filename}" >> $outfile;
            if [ -d $dir/$filename ]; then
                writemap $dir/$filename "${tab}";
            fi
        fi
    done
    IFS=$SAVEIFS;
}

echo "\`\`\`" > $outfile;
echo ".TotalNMS_NBI" >> $outfile;
writemap;
echo "\`\`\`" >> $outfile;

if [[ $0 == *writemap.sh ]]; then
    echo "Output written to ${outfile}:";
    cat $outfile;
fi

