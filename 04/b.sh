#!/bin/bash

cat - | \
    sed 's/^$/XXX/' | \
    tr ' \n' ',' | \
    sed 's/XXX/\n/g' | \
    sed 's/^,*/{"/;s/,*$/"}/;s/\([,:]\)/"\1"/g' | \
    jq --slurp \
    'map(select(keys |
        contains(["byr","iyr","eyr","hgt","hcl","ecl","pid"]))) |
    map(select(
        (.byr | tonumber | (. >= 1920 and . <= 2002)) and
        (.iyr | tonumber | (. >= 2010 and . <= 2020)) and
        (.eyr | tonumber | (. >= 2020 and . <= 2030)) and
        (.ecl as $ecl |
            ["amb","blu","brn","gry","grn","hzl","oth"] | contains([$ecl])) and
        (.hcl | test("^#[a-f0-9]{6}$")) and
        (.pid | test("^[0-9]{9}$")) and
        (.hgt |
            if endswith("in")
            then
                (.[:-2] | tonumber | (.>=59 and .<=76))
            else
                if endswith("cm") then
                    (.[:-2] | tonumber | (.>=150 and .<=193))
                else
                    false
                end
            end)
        )) | length'
