Bonjour,

Ce zip contient le dossier analytics issu du d�p�t Github.

J'ai supprim� les classes inutiles:
 - UserVisitCountBolt
 - PageVisitCountBolt

Ci-dessous quelques explications sur la fa�on dont ont �t� trait�es les demandes 
de l'�nonc� (num�rot�es de [1] � [8]).

##########################################
  ENONCE
------------------------------------------
Objectif

Dans cette activit�, vous allez modifier la topologie analytics vue dans les chapitres 
pr�c�dents (et disponible sur Github) pour r�colter des statistiques par page et par utilisateur.

Votre mission est de cr�er un bolt nomm� UserPageVisitCount [1]
qui va afficher en continu dans la console le nombre de visites r�alis�es [2]
dans la derni�re heure [3],
par page et par utilisateur [4],
toutes les trente secondes [5].

Ce bolt sera connect� au spout page-visits avec l'identifiant user-page-visit-counts.[6]

Ce bolt ne devra pas conserver de donn�es en m�moire entre deux appels � sa m�thode execute(), 
par exemple sous la forme d'attributs. [7]

Attention ! Il faut que les statistiques affich�es soient correctes, m�me lorsque le bolt est 
ex�cut� de mani�re distribu�e sur plusieurs workers en m�me temps. [8]
------------------------------------------

##########################################
  EXPLICATIONS DE MON TRAVAIL

[1] est r�alis�e par la cr�ation de la classe UserPageVisitCount et son instanciation 
dans App.java, ligne 20: new UserPageVisitCount(...) 

[2] est r�alis�e dans UserPageVisitCount.java des lignes 52 � 63.

[3] est r�alis�e par l'utilisation d'une fen�tre glissante dans UserPageVisitCount.java, ligne 16: extends BaseWindowedBolt
dont la largeur est sp�cifi�e en millisecondes (1h soit 60*60*1000ms) dans App.java, ligne 22: BaseWindowedBolt.Duration.of(1000*60*60)

[4] est r�alis�e par l'utilisation d'une hashmap (Utilisateur, hashmap(Page, Nombre de visites) ), 
dans UserPageVisitCount.java, ligne 33: HashMap<Integer,HashMap<String,Integer>> userPageVisitCounts = new HashMap<Integer,HashMap<String,Integer>>();

[5] est r�alis�e par l'utilisation d'une fen�tre glissante dans UserPageVisitCount.java, ligne 16: extends BaseWindowedBolt
et sp�cifi� en millisecondes (30s soit 30*1000ms) dans App.java, ligne 23: BaseWindowedBolt.Duration.of(1000*30).

[6] est r�alis�e dans la d�claration du builder dans App.java, ligne 26: .fieldsGrouping("page-visits", new Fields("url","userId"));

[7] est r�alis�e par l'utilisation de la hashmap cit�e en [4] � l'int�rieur de l'impl�mentation de la m�thode execute() de UserPageVisitCount.java. 
Cette hashmap est donc d�truite et recr��e � chaque appel de execute().

[8] est r�alis�e en utilisant le champs constitu� du couple (Page,Utilisateur) pour distribuer les info sur 
les diff�rents workers, dans App.java, ligne 26: .fieldsGrouping("page-visits", new Fields("url","userId"));

------------------------------------------

##########################################

J'esp�re que ces explications auront �t� suffisamment claires pour vous faciliter le travail.

L'ex�cution dans l'environnement eclipse a produit les r�sultats attendus.

Merci pour votre temps consacr� � cette correction. 

