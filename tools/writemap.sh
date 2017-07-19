function writemap() {
    outfile=sitemap.md;
    if [[ $# -ge 1 ]]; then
        outfile=$1/$outfile;
    fi
    echo "\`\`\`" > $outfile;
    echo ".TotalNMS_NBI" >> $outfile;
    
    function wmrec() {
        local dir=".";
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
                    wmrec $dir/$filename "${tab}";
                fi
            fi
        done
        IFS=$SAVEIFS;
    }

    wmrec;
    echo "\`\`\`" >> $outfile;
}

if [[ $0 == *writemap.sh ]]; then
    writemap ..;
    echo "Map written to ${outfile}:";
    cat $outfile;
fi

