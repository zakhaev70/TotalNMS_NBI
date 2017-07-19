SAVEIFS=$IFS;  #by convention, use \n as breaks
IFS=$(echo -en "\n\b");

function contains() {  #checks if pattern match in file
    a=( $( cat $1 ) );
    s=$2;
    for x in ${a[@]}; do
        if [[ $s == $x ]]; then
            return 0;
        fi
    done
    return 1;
}

function writemap() {
    outfile=sitemap.md;
    gitignore=../.gitignore;
    if [[ $# -ge 1 ]]; then
        outfile=$1/$outfile;
        gitignore=$1/$gitignore;
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
    
        for f in `ls -A $dir`; do
            filename=$( basename "${f}" );
            if ! $( contains $gitignore $filename ); then
                echo "${tab}${filename}" >> $outfile;
                if [ -d $dir/$filename ]; then
                    wmrec $dir/$filename "${tab}";
                fi
            fi
        done
    }

    wmrec;
    echo "\`\`\`" >> $outfile;
}

if [[ $0 == *writemap.sh ]]; then
    writemap $( dirname $0 );
    echo "Map written to ${outfile}:";
    cat $outfile;
fi

IFS=$SAVEIFS;  
