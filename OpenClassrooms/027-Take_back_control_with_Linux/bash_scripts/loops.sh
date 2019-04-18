#!/bin/bash

while [ -z $response ] || [ $response != 'yes' ]
do
    read -p 'Please say yes : ' response
done


for file in `ls`
do
    echo "File found: $file"
done