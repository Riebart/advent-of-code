#!/bin/bash

(cat - | \
    sed 's/^$/_/' | \
    tr -d '\n' | \
    tr '_' '\n'
    echo) | \
    while read line
    do
        echo "$line" | \
            fold -w 1 | \
            sort | \
            uniq | \
            wc -l
    done | \
    paste -sd '+' | bc
