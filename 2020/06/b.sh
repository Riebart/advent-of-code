#!/bin/bash

(cat - | \
    sed 's/^$/_/' | \
    tr '\n_' ',\n' | \
    sed 's/^,//;s/,$//'
    echo) | \
    while read family
    do
        num_members=$(echo "$family" | tr ',' '\n' | wc -l)
        echo "$family" | \
            fold -w 1 | \
            sort | \
            uniq -c | \
            grep -c "^ *$num_members"
    done | \
    paste -sd '+' | bc
