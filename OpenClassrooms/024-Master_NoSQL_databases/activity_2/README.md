# Activité 2 - Visualisation avec Kibana

Quelques éléments d'explications sur le diagramme joint :
* Il s'agit d'un graphe de type "Vertical Bar"
* Pour les "Metrics", le Y-Axis choisi correspond à une agrégation de type "Count", avec un label personnalisé "Percentage" et un mode "Percentage" également
* Pour les buckets :
  * le X-Axis est un "Date Histogram" sur le champ "fields.release_date", avec un intervalle personnalisé de "10y"
  * un bucket supplémentaire de type "Split Series" a été créé, avec une agrégation de type "range" sur le champ "fields.rating" et des plages de valeurs avec des pas de 0.5