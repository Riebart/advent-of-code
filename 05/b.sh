#!/bin/bash

seats=$(cat - | tr 'FBLR' '0101' | paste -sd ';')
seat_ids=$(bc <<< "ibase=2; $seats" | sort -n)
comm -3 <(seq $(echo "$seat_ids" | head -n1) $(echo "$seat_ids" | tail -n1)) <(echo "$seat_ids")
