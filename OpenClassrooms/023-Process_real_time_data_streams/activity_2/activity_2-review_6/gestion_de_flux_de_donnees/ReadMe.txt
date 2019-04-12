Bonjour,

Ce zip contient le dossier analytics issu du dépôt Github.

J'ai supprimé les classes inutiles:
 - UserVisitCountBolt
 - PageVisitCountBolt

Ci-dessous quelques explications sur la façon dont ont été traitées les demandes 
de l'énoncé (numérotées de [1] à [8]).

##########################################
  ENONCE
------------------------------------------
Objectif

Dans cette activité, vous allez modifier la topologie analytics vue dans les chapitres 
précédents (et disponible sur Github) pour récolter des statistiques par page et par utilisateur.

Votre mission est de créer un bolt nommé UserPageVisitCount [1]
qui va afficher en continu dans la console le nombre de visites réalisées [2]
dans la dernière heure [3],
par page et par utilisateur [4],
toutes les trente secondes [5].

Ce bolt sera connecté au spout page-visits avec l'identifiant user-page-visit-counts.[6]

Ce bolt ne devra pas conserver de données en mémoire entre deux appels à sa méthode execute(), 
par exemple sous la forme d'attributs. [7]

Attention ! Il faut que les statistiques affichées soient correctes, même lorsque le bolt est 
exécuté de manière distribuée sur plusieurs workers en même temps. [8]
------------------------------------------

##########################################
  EXPLICATIONS DE MON TRAVAIL

[1] est réalisée par la création de la classe UserPageVisitCount et son instanciation 
dans App.java, ligne 20: new UserPageVisitCount(...) 

[2] est réalisée dans UserPageVisitCount.java des lignes 52 à 63.

[3] est réalisée par l'utilisation d'une fenêtre glissante dans UserPageVisitCount.java, ligne 16: extends BaseWindowedBolt
dont la largeur est spécifiée en millisecondes (1h soit 60*60*1000ms) dans App.java, ligne 22: BaseWindowedBolt.Duration.of(1000*60*60)

[4] est réalisée par l'utilisation d'une hashmap (Utilisateur, hashmap(Page, Nombre de visites) ), 
dans UserPageVisitCount.java, ligne 33: HashMap<Integer,HashMap<String,Integer>> userPageVisitCounts = new HashMap<Integer,HashMap<String,Integer>>();

[5] est réalisée par l'utilisation d'une fenêtre glissante dans UserPageVisitCount.java, ligne 16: extends BaseWindowedBolt
et spécifié en millisecondes (30s soit 30*1000ms) dans App.java, ligne 23: BaseWindowedBolt.Duration.of(1000*30).

[6] est réalisée dans la déclaration du builder dans App.java, ligne 26: .fieldsGrouping("page-visits", new Fields("url","userId"));

[7] est réalisée par l'utilisation de la hashmap citée en [4] à l'intérieur de l'implémentation de la méthode execute() de UserPageVisitCount.java. 
Cette hashmap est donc détruite et recréée à chaque appel de execute().

[8] est réalisée en utilisant le champs constitué du couple (Page,Utilisateur) pour distribuer les info sur 
les différents workers, dans App.java, ligne 26: .fieldsGrouping("page-visits", new Fields("url","userId"));

------------------------------------------

##########################################

J'espère que ces explications auront été suffisamment claires pour vous faciliter le travail.

L'exécution dans l'environnement eclipse a produit les résultats attendus.

Merci pour votre temps consacré à cette correction. 

