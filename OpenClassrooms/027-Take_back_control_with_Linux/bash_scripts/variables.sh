#!/bin/bash

message=`pwd`
echo "Working directory: $message"
echo 'With simple quotes: $message'
echo -e "\n"

read -p 'Please enter your name and surname: ' surname name
echo "Hi $surname $name!"

let "a = 5"
let "b = 2"
let "c = a + b"
echo $c
echo -e "\n"

echo "Your running script $0 with $# parameter(s)"
echo "The first parameter is $1"
echo -e "\n"

tableau=('value0', 'value1', 'value2')
tableau[5]='value5'
echo ${tableau[5]}
