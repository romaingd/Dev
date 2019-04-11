Bonjour,

Afin de faciliter la correction, j'ai rappelé dans le fichier environnement.sh les lignes de commande à executer pour lancer kafka et zookeeper.

Comme demandé dans l'énoncé,

 - get-stations.py a été modifié pour :
    - émettre un message dans le topic empty-stations dès qu'une station devient vide (alors qu'elle n'était pas vide auparavant).
    - émettre un message dans le topic empty-stations dès qu'une station n'est plus vide (alors qu'elle était vide auparavant).

 - monitor-empty-stations.py a été modifié pour:
    - afficher dans la console un message dès qu'une station devient vide (alors qu'elle n'était pas vide auparavant)
        - l'adresse de la station,
        - la ville de la station,
        - le nombre de stations vides dans la ville.

Nota 1: Ce second script n'affiche pas de message quand une station n'est plus vide, car ce n'est pas demandé.

Nota 2: Il faut veiller à ce que le nombre de stations vides affiché par le script monitor-empty-stations.py soit correct
 même lorsque le topic empty-stations aura plusieurs partitions. Pour cela, le message envoyé utilise comme clef le nom de la ville.
Ainsi, toutes les stations d'une même ville seront affectées à une même partition.

Nota 3: Concernant le nombre de stations vides de la ville, le code présenté correspond au cas où dès le lancement on suppose 
qu'aucune station n'est vide. Pour prendre en compte le fait que des stations peuvent être vides dès le lancement, il faudrait 
envoyer l'information pour toutes les villes à l'initialisation. Ce cas de figure n'étant pas explicitement cité dans l'énoncé,
je pars du principe que c'est une complication hors du sujet.

Nota 4: N'oubliez pas de mettre votre propre API dans le get-stations.py

Merci pour votre travail de correction.