#!/bin/bash

input=$(cat -)

echo "$input" | grep -nE "(jmp|nop)" | cut -d':' -f1 | \
while read line
do
    echo "$input" | \
    sed "${line}s/nop/jmp/;${line}s/jmp/nop/" | \
        python3 a.py && echo "SUCCESS"
done | \
    grep -B1 "SUCCESS" | \
    head -n1
