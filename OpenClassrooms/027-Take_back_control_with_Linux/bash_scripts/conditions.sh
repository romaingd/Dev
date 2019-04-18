#!/bin/bash

read -p 'Enter a file name: ' file

if [ ! $# -ge 1 ] && [ -f $file ]
then
    if [ -e $file ]
    then
        echo 'This file exists'
    else
        echo 'This file does not exist'
    fi
else
    echo 'This is not a file!'
fi

if [ -z $file ]
then
    echo "You didn't enter a name!"
fi