#!/bin/bash

seats=$(cat - | tr 'FBLR' '0101' | paste -sd ';')
seat_ids=$(bc <<< "ibase=2; $seats" | sort -n)
echo "$seat_ids" | tail -n1
