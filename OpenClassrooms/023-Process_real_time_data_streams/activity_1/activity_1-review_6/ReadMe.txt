Bonjour,

Afin de faciliter la correction, j'ai rappel� dans le fichier environnement.sh les lignes de commande � executer pour lancer kafka et zookeeper.

Comme demand� dans l'�nonc�,

 - get-stations.py a �t� modifi� pour :
    - �mettre un message dans le topic empty-stations d�s qu'une station devient vide (alors qu'elle n'�tait pas vide auparavant).
    - �mettre un message dans le topic empty-stations d�s qu'une station n'est plus vide (alors qu'elle �tait vide auparavant).

 - monitor-empty-stations.py a �t� modifi� pour:
    - afficher dans la console un message d�s qu'une station devient vide (alors qu'elle n'�tait pas vide auparavant)
        - l'adresse de la station,
        - la ville de la station,
        - le nombre de stations vides dans la ville.

Nota 1: Ce second script n'affiche pas de message quand une station n'est plus vide, car ce n'est pas demand�.

Nota 2: Il faut veiller � ce que le nombre de stations vides affich� par le script monitor-empty-stations.py soit correct
 m�me lorsque le topic empty-stations aura plusieurs partitions. Pour cela, le message envoy� utilise comme clef le nom de la ville.
Ainsi, toutes les stations d'une m�me ville seront affect�es � une m�me partition.

Nota 3: Concernant le nombre de stations vides de la ville, le code pr�sent� correspond au cas o� d�s le lancement on suppose 
qu'aucune station n'est vide. Pour prendre en compte le fait que des stations peuvent �tre vides d�s le lancement, il faudrait 
envoyer l'information pour toutes les villes � l'initialisation. Ce cas de figure n'�tant pas explicitement cit� dans l'�nonc�,
je pars du principe que c'est une complication hors du sujet.

Nota 4: N'oubliez pas de mettre votre propre API dans le get-stations.py

Merci pour votre travail de correction.