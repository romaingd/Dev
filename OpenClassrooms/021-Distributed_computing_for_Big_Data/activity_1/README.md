# Réalisez des calculs distribués sur des données massives - Activité

## Notes de reproducibilité

Le code a été exécuté en utilisant Hadoop 3.2.0, avec Hadoop Streaming et Python 3.6.7.

Pour chaque mission, la procédure à suivre pour reproduire les résultats est la suivante, après avoir démarré Hadoop :
~~~sh
./setup_input.sh
./run.sh
~~~

Les détails d'éxécution et de chaînage des différentes tâches sont disponibles dans le fichier `run.sh`.


<br>


## Mission 1 - TF-IDF

Liste des 20 mots ayant la plus forte pondération TF-IDF:

* Dans `callwild`:
  1. 'buck' 0.01826073801694697
  2. 'dogs' 0.005985464127777062
  3. 'thornton' 0.005173875771468307
  4. 'spitz' 0.0032970776975043137
  5. 'sled' 0.0031956291529657197
  6. 'francois' 0.003043456336157828
  7. 'trail' 0.002079695163041182
  8. 'john' 0.002028970890771885
  9. 'perrault' 0.001978246618502588
  10. 'hal' 0.001876798073963994
  11. 'team' 0.0017246252571561024
  12. 'sol' 0.0014710038958096168
  13. 'ice' 0.0014202796235403196
  14. 'leks' 0.0014202796235403196
  15. 'traces' 0.0014202796235403196
  16. 'dave' 0.0012681068067324282
  17. 'mates' 0.0011159339899245368
  18. 'mercedes' 0.0010652097176552396
  19. 'dawson' 0.0010144854453859426
  20. 'whip' 0.0010144854453859426

* Dans `defoe-robinson-103.txt`:
  1. 'friday' 0.0034838140731251323
  2. 'thoughts' 0.0020902884438750795
  3. 'board' 0.001337031346983159
  4. 'corn' 0.0011675485001824768
  5. 'voyage' 0.001111054217915583
  6. 'powder' 0.0010357285082263907
  7. 'providence' 0.0010357285082263907
  8. 'labor' 0.0009792342259594966
  9. 'deliverance' 0.0008662456614257086
  10. 'coast' 0.0007909199517365166
  11. 'england' 0.0007720885243142184
  12. 'sail' 0.0007720885243142184
  13. 'goat' 0.0006779313872027285
  14. 'storm' 0.0006590999597804305
  15. 'brazils' 0.0006402685323581324
  16. 'purpose' 0.0006402685323581324
  17. 'dreadful' 0.0006214371049358344
  18. 'fired' 0.0006214371049358344
  19. 'habitation' 0.0006214371049358344
  20. 'round' 0.0006214371049358344

<br>

Structure -> 3 tâches MapReduce utilisées :
1. **WordCount** :
   * Mapper : `WordCountMapper`
     * Squelette : Pré-traite les mots - Associe à chaque mot le doc_ID (ici nom du fichier) - Émet le couple (clef, valeur)
     * Clef : (mot, doc_ID)
     * Valeur : 1
   * Reducer : `WordCountReducer`
     * Squelette : Effectue un WordCount standard pour chaque clef récupérée
     * Clef : (mot, doc_ID)
     * Valeur : wordcount
2. **WordPerDoc** :
   * Mapper : `WordPerDocMapper`
     * Squelette : Change la clef pour grouper par fichier dans le Reducer - Émet le couple (clef, valeur)
     * Clef : doc_ID
     * Valeur : (mot, wordcount)
   * Reducer : `WordPerDocReducer`
     * Squelette : Effectue un total du nombre de mots pour chaque fichier
     * Clef : (mot, doc_ID)
     * Valeur : (wordcount, wordperdoc)
3. **TF-IDF** :
   * Mapper : `TFIDFMapper`
     * Squelette : Calcule le terme `tf` pour chaque couple (mot, doc_ID) - Émet le couple (clef, valeur)
     * Clef : mot
     * Valeur : (doc_ID, tf)
   * Reducer : `TFIDFReducer`
     * Squelette : Calcule le terme `df` pour chaque mot - Calcule la pondération finale tf-idf
     * Clef : (mot, doc_ID)
     * Valeur : tf-idf


<br>


## Mission 2 - PageRank

Liste des 20 noeuds ayant le plus fort page rank :
  1. 1 - http://www.imdb.com
  2. 7830 - http://affiliates.allposters.com/link/redirect.asp?aid=445601&parentaid=445601
  3. 218 - http://www.amazon.com/exec/obidos/redirect-home/internetmoviedat
  4. 681 - http://www.google.com
  5. 6680 - http://www.knightridder.com
  6. 1980 - http://www.gannett.com
  7. 76 - http://www.signs.movies.com
  8. 7252 - http://www.mac.com
  9. 2727 - http://www.dealtime.com
  10. 5792 - http://www.cninewsonline.com
  11. 1797 - http://dmoz.org/about.html
  12. 5990 - http://www.aei-potsdam.mpg.de/~werner
  13. 5221 - http://www.Flora2000.com/online_florist.asp
  14. 116 - http://www.localmovies.com
  15. 49 - http://www.fandango.com
  16. 3565 - http://www.getwild.com
  17. 12 - http://world.std.com/~reinhold/mathmovies.html
  18. 4230 - http://docs.yahoo.com/info/terms
  19. 3633 - http://dailynews.yahoo.com
  20. 184 - http://www.formovies.com


Structure -> 5 tâches MapReduce utilisées (input : `adj_list`) :
1. **Première itération** :
   * Mapper : `PageRankFirstMapper`
     * Squelette : Isole le noeud `i` considéré, et les liens sortants - Émet (cas 1)la contribution de `i` au page rank pour chaque lien sortant `j` (pour grouper par noeud dans le Reducer) - Émet également les liens partant de `i` (cas 2)
     * Cas 1 :
       * Clef : `j`
       * Valeur : contribution de `i` au page rank de `j` (cf. code)
     * Cas 2 :
       * Clef : `i`
       * Valeur : liste de liens partant de `i`
   * Reducer : `PageRankEarlyReducer`
     * Squelette : Isole le noeud `i` considéré - Reconstruit la liste de liens partant de `i`, ainsi que la contribution de chacun au page rank de `i` à cette itération - Calcule le page rank de `i` à cette itération en prenant en compte la téléportation - Émet la contribution de `i` au page rank pour chaque lien sortant `j` - Émet également les liens partant de `i`
     * Cas 1 :
       * Clef : `j`
       * Valeur : contribution de `i` au page rank de `j` (cf. code)
     * Cas 2 :
       * Clef : `i`
       * Valeur : liste de liens partant de `i`
2. **Seconde itération** :
   * Mapper : `PageRankSubsequentMapper`
     * Squelette : Ne fait rien, répète simplement l'entrée
     * Clef : voir Reducer précédent
     * Valeur : voir Reducer précédent
   * Reducer : `PageRankEarlyReducer` - Voir 1. pour les détails
3. **Troisième itération** : Identique à 2.
4. **Quatrième itération** : Identique à 2.
5. **Cinquième itération** :
   * Mapper : `PageRankSubsequentMapper`
     * Squelette : Ne fait rien, répète simplement l'entrée
     * Clef : voir Reducer précédent
     * Valeur : voir Reducer précédent
   * Reducer : `PageRankLastReducer`
     * Squelette : Isole le noeud `i` considéré - Reconstruit la liste de liens partant de `i`, ainsi que la contribution de chacun au page rank de `i` à cette itération - Calcule le page rank de `i` à cette itération en prenant en compte la téléportation - Émet le page rank final de `i`
     * Clef : `i`
     * Valeur : page rank de `i`
