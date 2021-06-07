# Covid19Modeler
# Description

L’année 2020 et 2021 sont marquées par la progression du COVID 19. Afin d’informer la population sénégalaise, chaque jour un communiqué de presse est diffusé en ligne par le Ministère de la Santé et de l’Action Sociale du Sénégal.
Un groupe de scientifique désireux de regrouper et analyser ces données pour la compréhension de sa diffusion dans le territoire sénégalais engage un groupe de développeurs pour concevoir et développer une solution permettant de modéliser son évolution spatiale et temporelle.
La solution envisagée est un système intégré devant répondre au cahier des charges fonctionnelles qui suit.
Il est présenté ici sous la forme de l’architecture du système ainsi que des fonctionnalités attendues par l’utilisateur. On trouvera ainsi dans la description des modules attendues et la présentation des fonctionnalités / différents usages possibles.

### Contenu du projet

--DataAcquisition
Utilisant les sources de données officielles, ce module permettra de :
• télécharger des fichiers pdfs et/ou des images des communiqués officiels du ministère de la santé dans un répertoire local
• parcourir , extraire et agréger au fur et à mesure des téléchargements des fichiers, les données qu’elles contiennent pour les stocker dans des fichiers mensuels (Json ou fichiers XML en fonction du besoin de l’utilisateur ) respectant la hiérarchie suivante :
o Année-Mois //NomDuFichier
▪ Date1 : NbTest, Nb nouveaux Cas , Nb Cas contacts, Nb Cas Communautaires, Nb Guéris, Nb Décès, NomFichierSource, DateHeureExtraction
• Localité : NomLocalité , NbCas
Rqe : il vous est possible de proposer des champs supplémentaires en cohérence avec l’objectif du projet
Sources de données officielles à considérer :
- Sur twitter en image : https://twitter.com/MinisteredelaS1
- Sur son site internet en document pdf : http://www.sante.gouv.sn/actualites

### DataLoader

Ce module permet le chargement des données téléchargées vers un serveur de base de données relationnelles en ligne. Ainsi dans ce module, l’utilisateur peut voir la liste des fichiers obtenus dans le module précédent et parcourir leur arborescence et prévisualiser les données . Grâce à des cases à cocher sur les différents jours, il lui est loisible de sélectionner les dates à importer vers le SGBD. Il peut décider si les données seront chargées par lot et en mode transactionnel ou pas. Dans ce dernier cas il doit avoir la possibilité de valider à la fin du processus les données importées, ou bien annuler tout le processus bien que les données soient déjà sur le serveur et ainsi les effacer.
En cas de duplication de données, il lui est proposé d’écraser les nouvelles données ou ignorer les nouvelles données.
Le chargement des données devant être intelligent, chaque localité doit être associée dans la base de données au niveau administratif lui correspondant (commune, département, région, ville , etc.), afin de supporter le fait que les communiqués dans le temps aient changé de format et ne comportent pas toujours les mêmes localités.

### DataExplorer

En considérant les données issues du module précédent, le présent devra permettre de :
- Consulter sur une carte géographique l’évolution journalière du nombre de cas des régions du sénégal grâce à une barre temporelle.
- Sur le clique dans une région, de fournir une fenêtre flottante avec la répartition des types de cas de la région et un bouton détail. Le bouton détails donnera une vue comprenant :
o La courbe temporelle d’évolution des cas de la région,
o la carte de ses départements avec le dénombrement des cas leurs correspondants
- Télécharger en format image PNG la carte affichée ( nationale ou régionale) , pour une date choisie
- Télécharger en format SQL /CSV les données affichées par la carte en cours

### Evolution Analyzer
Grace aux données du système ce module permet d’interpréter partiellement l’évolution du Covid 19 sur le territoire en générant un graphe de flux spatio/temporel. Ce graphe est une représentation du chemin pris potentiellement par le covid pour se propager entre les régions.


