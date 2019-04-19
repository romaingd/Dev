#!/bin/bash

file=$1


# Check that the first argument is an actual file
if [ ! -z $file ]
then
    if [ -e $file ]
    then
        if [ ! -f $file ]
        then
            echo "This is a directory, not a file"
            exit 1
        fi
    else
        echo "This file does not exist"
        exit 1
    fi
else
    echo "Please pass a file name as argument"
    exit 1
fi


# Take the second parameter into account: if asked to, consider only vowels
letter_set=( {A..Z} )
n=26
if [ ! -z $2 ]
then
    if [ $2 = '--only_vowels' ]
    then
        letter_set=('A' 'E' 'I' 'O' 'U' 'Y')
        n=6
    else
        echo "Unrecognized option"
        exit 1
    fi
fi


# Fill the array
stats_array=()
for ((i=0; i<n; i++))
do
    stats_array[i]=`grep -o ${letter_set[i]} $file | wc -l`
done


# Save the results in a temporary file
results_file="results.txt"
i=0
for ((i=0; i<n; i++))
do
    echo ${stats_array[i]} " - " "${letter_set[i]}" >> $results_file
done


# Output the sorted results and delete the temporary result file
# Sort by numerical value (-n), reversed ('-r')
cat $results_file | sort -nr
rm $results_file
