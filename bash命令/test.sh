#!/bin/sh
for i in {0..500}
    do
        if [[ i%7 -eq 0 ]];then
            echo $i
        fi
    done

cat $1 | awk '{print $2}' | sort | uniq -c | sort | grep -v 1