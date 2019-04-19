#!/bin/bash

#Verification s'il y a des paramètres dont le dictionnaire

if [ $# -ne 0 ];then

#verification qu'il y a bien un fichier( dictionnaire en l'occurence

	if [ -e $1 ]
	then
#Boucle qui parcours l'alphabet et on recherche pour chaque lettre grace à grep le nombre de répétition de chaque lettre, avec le pipe on récupère la sortie du for et on trie avec sort dans l'ordre décroissant

		for letter in {A..Z};do
			echo "`grep -ic $letter $1` - $letter "
		done | sort -nr

#On vérifie s'il y a un ou plusieurs paramètre suplémentaire
		if [ $# -ge 2 ]
		then
#On recherche le nombre de fois où est présente cette partie de mot dans le dictionnaire et on demande à l'utilisateur s'il souhaite les afficher

			echo "cette partie de mot est présente : `grep -ic $2 $1` fois"
			read -p 'voulez vous les afficher ? (O/N)' reponse
			until [ $reponse = "O" ] || [ $reponse = "N" ]
			do
				read -p 'voulez vous les afficher ? (O/N)' reponse
			done
			if [ $reponse = "O" ];then 
				grep -i $2 $1
			fi
		fi 
	else 
	echo "vous n'avez pas mis de dictionnaire en paramètre"
	fi
else
	echo "vous n'avez mis aucun parametre"
fi
