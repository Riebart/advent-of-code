#!/bin/bash

cat - | \
    sed 's/^$/XXX/' | \
    tr ' \n' ',' | \
    sed 's/XXX/\n/g' | \
    sed 's/^,*/{"/;s/,*$/"}/;s/\([,:]\)/"\1"/g' | \
    jq --slurp \
    'map(select(keys | contains(["byr","iyr","eyr","hgt","hcl","ecl","pid"]))) | length'
