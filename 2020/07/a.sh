#1/bin/bash

input=$(cat -)
# total=""

initial_bag="$1"
bags="${initial_bag}"
bags=$(echo -e "${bags}\n${bags}" | sort | uniq | grep -v "^$")
echo "$bags" | wc -l
echo "$bags"

for i in {1..5}
do
    new_bags=$(echo "$input" | grep -E "^.+(`paste -sd '|' <<< "$bags"`)" | sed 's/^\(.*\) bags contain.*$/\1/' | sort | uniq)
    if [ "$new_bags" == "" ]
    then
        break
    fi

    bags=$(echo -e "${bags}\n${new_bags}" | sort | uniq | grep -v "^$")
    echo "$new_bags" | wc -l
    echo "$bags"
done

echo "$bags" | grep -cv "$initial_bag"
