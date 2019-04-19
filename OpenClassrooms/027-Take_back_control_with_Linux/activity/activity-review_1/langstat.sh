#!/bin/bash

: '
Auteur  : Alexis Gardet
Date    : 09/04/2019
Version : 2.0

Ce script a été réalisé dans le cadre du cours "Reprenez le controle à l aide de Linux", disponible à l addresse "https://openclassrooms.com/fr/courses/43538-reprenez-le-controle-a-laide-de-linux".

L exercice est en deux parties:
 1) Analyser le fichier dico.txt et compter le nombre de mot dont chaque lettre de l alphabet apparait. (Obligatoire)
 2) Integrer un 2ème paramètre qui modifie le fonctionnement ou l affichage du script. (Facultatif)

 Comme 2ème parametre, l utilisateur peut entrer son prénom et le script va compter le nombre d occurence des lettres qui le composent et afficher le total sous l intituler "Score de nom"

Exemples d utilisation et de sorties:
    1) ./langstat.sh dico.txt
    output* => 
        200000 - C
        199999 - Z
        199998 - A
        ...

    2) ./langstat.sh dico.txt Alexis
    output* =>
        200000 - A
        200000 - L
        200000 - E
        200000 - X
        200000 - I
        200000 - S
        Votre score de nom est de : 12000000

* = chiffres de démonstration
'

#Set lettersArray
lettersArray=(A B C D E F G H I J K L M N O P Q R S T U V W X Y Z)
#Get the lettersArray length
nbrLetters=${#lettersArray[@]}
#Create an empty associative array
declare -A lettersOccurences=()

#new function "getOccurence"
#Synopsis: This function get the number of occurence for a given letter
#Details: This function takes 2 parameters
#   $1: Name of the file to be read
#   $2: The letter it must count
#It will then read line by line the file while counting how many lines contains the letter in $2
#
getOccurence () { #param1=file & param2=letter
    #reset the count variable to 0
    let "nbrOfOccurence=0"
    #Read every line of the file
    while read line; do
        #if line contains the letter
        if [[ $line =~ .*$2.* ]];
        then
            #Increment the count variable
            let "nbrOfOccurence++"
        fi
    done <$1
}

#Check if 1st parameter is correct (file name + exists file) and 2nd isn't present
if [ -e "$1" ] && [ -z "$2" ];
then
   #Foreach letter in lettersArray
    for (( i=0; i<nbrLetters; i++ ))
    do
        #getOccurence file letter
        getOccurence $1 ${lettersArray[$i]}
        #store the number of occurence with the letter as key in the associative array
        lettersOccurences["${lettersArray[$i]}"]=$nbrOfOccurence
    done
    #Display the associative array
    for k in "${!lettersOccurences[@]}"
    do
        echo "${lettersOccurences[$k]} - $k"
    done | sort -nr #Sort the array output to have the highest number first
#Else if the 2nd parameter is supplied
elif [ -e "$1" ] && [ -n "$2" ];
then
    scoreName=0 #set the score of the name to 0
    #read the $2 char by char
    while IFS= read -rn1 c; do
        #call the getOccurence for current letter in $c
        #But only if $c isn't empty AND is in alphabet
        if [ "$c" != "" ] && [[ "$c" == [a-zA-Z] ]];
        then
            getOccurence $1 ${c^^}
            #Display the number of occurence + associated letter
            echo "$nbrOfOccurence - ${c^^}"
            let scoreName+=$nbrOfOccurence
        fi
    done <<< $2
    #Show the score of the name
    echo "Votre score de nom est de : $scoreName"
fi