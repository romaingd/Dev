# Créez et interrogez votre base de données MongoDB

## Questions et commandes associées

1. Importez le jeu de données tour-pedia.json dans une base de données “tourPedia” avec une collection “paris”

~~~shell
mongoimport --db tourPedia --collection paris ./tourPedia_paris.json --port 27017
~~~

<br>

1. Filtrez les lieux par type “accommodation” et service “blanchisserie”

~~~js
db.paris.find({
    "category": "accommodation",
    "services": "blanchisserie"
});
~~~

<br>

3. Projetez les adresses des lieux de type "accommodation"

~~~js
db.paris.find({
    "category": "accommodation"
},
{
    "location.address": 1
});
~~~

<br>

4. Filtrez les listes de commentaires (reviews) des lieux, pour lesquelles au moins un commentaire (reviews) est écrit en anglais (en) et a une note (rating) supérieure ou égale à 3

~~~js
db.paris.find({
    "reviews": {
        $elemMatch: {
            "language": "en",
            "rating": {$gte: 3}
        }
    }
});
~~~

<br>

5. Groupez les lieux par catégorie et comptez les

~~~js
db.paris.aggregate( [
    { $group: {
        "_id": "$category",
        "count": {$sum: 1}
    }}
]);
~~~

<br>

6. Créez un pipeline d’agrégation pour les lieux de catégorie "accommodation", et donnez le nombre de lieux par valeur de "services"

~~~js
db.paris.aggregate( [
    { $match: {
        "category": "accommodation"
    }},
    { $group: {
        "_id": "$services",
        "count": {$sum: 1}
    }}
]);
~~~