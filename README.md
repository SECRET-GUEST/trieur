[![Download AKOUN trieur](https://img.shields.io/sourceforge/dt/trieur.svg)](https://sourceforge.net/projects/trieur/files/latest/download)
Trieur version 1.0.3 | Python version 3.11.1 | 🇫🇷 | For every OS but run better on Windows 
```
████████╗██████╗ ██╗███████╗██╗   ██╗██████╗      █████╗ ██╗  ██╗ ██████╗ ██╗   ██╗███╗   ██╗
╚══██╔══╝██╔══██╗██║██╔════╝██║   ██║██╔══██╗    ██╔══██╗██║ ██╔╝██╔═══██╗██║   ██║████╗  ██║
   ██║   ██████╔╝██║█████╗  ██║   ██║██████╔╝    ███████║█████╔╝ ██║   ██║██║   ██║██╔██╗ ██║
   ██║   ██╔══██╗██║██╔══╝  ██║   ██║██╔══██╗    ██╔══██║██╔═██╗ ██║   ██║██║   ██║██║╚██╗██║
   ██║   ██║  ██║██║███████╗╚██████╔╝██║  ██║    ██║  ██║██║  ██╗╚██████╔╝╚██████╔╝██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
                                                                                             
                                            
```


# Améliore la gestion de vos oeuvres d'art informatisée !

Ce logiciel permet aux artistes cotés AKOUN, tels que Nathacha , artiste peintre de l'abstraction https://www.artnathacha.com/ , à créer plus rapidement une liste de prix relative à leur cotation pour leurs oeuvres (ou à des fins éducatives). Il permet également de manipuler ces listes ainsi que les fichiers, dans le but de les trier, manipuler plus facilement.

Il permet également de renommer par lot d'images, d'ajouter ou d'y retirer des mots réccurents, mais aussi de créer des tableaux excel pour une comptabilité plus rapide,une meilleure gestion des stocks. 

**Notez qu'il demande l'ouverture d'un dossier, mais qu'il traite le contenu de tout les sous-dossiers présents à l'interieur, donc pensez à faire une copie de vos fichiers avant de les manipuler afin d'éviter une perte de donnée !**

ⁿᵒᵗᵉ *Un bon anti-malware vous donnera toujours un faux positif pour le fichier .exe puisqu'il n'est pas signé, cependant vous avez le code et j'ai meme écris une notice sur comment compiler le programme vous meme.*

[![Download AKOUN trieur](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/trieur/files/latest/download)


# En cours de developpement : 

* Fonction de clic automatique
* Corrections de bugs
* Ajout d'un menu
* Optimisation du code
* Amélioration de l'interface visuelle
* Creation de l'application pour tablette/smartphone (Android et Apple)
* Diversifier les possibilité de listes, txt, pdf...
* Themes reglable pour l'application
* Incorporation de listes de mots personnels pour la génération de noms aléatoire


Voici un apercu du logiciel (Version 0.9.9.9999999) : 


![global](https://user-images.githubusercontent.com/92639080/222796734-14c65748-d69a-421f-8ce5-9613ffb8b987.png)

# Contenu et utilisation

IMPORTANT : Pour commencer, veuillez noter que ce logiciel va modifier directement TOUT les fichiers présents dans TOUT les dossiers et sous dossiers du dossier ouvert, pensez à faire une copie de vos dossier avant toute chose pour limiter les risques de perte de données !

ⁿᵒᵗᵉ *Le logiciel génère un fichier errors.log ainsi qu'un fichier config.ini à la racine du repertoire ou il aura été lancé, à chaque fois qu'il le sera. Vous pouvez supprimez ces fichiers sans soucis, ils ne servent qu'a retenir vos preferences et à afficher les possibles erreurs rencontrée.*

## 1. D4rk/l1ght mode
Bon, je pense pas vraiment avoir à présenter ce mode, mais dans le cas ou vous viviez dans une grotte jusqu'à maintenant, ce boutton permet d'afficher le thème coloré du logiciel selon mode souhaité par l'utilisateur, dark pour gagner en confort durant la nuit, ou pour les personnes ayant les yeux plus sensibles et inversement. 

## 2. Tout en un
Permet de travailler plus rapidement en lançant automatiquement une à une les fonctions principales de cette liste.

**Attention** : Une fois le dossier choisi, il n'y a pas de possibilité de retour en arrière jusqu'à que l'ensemble du programme se soit exécuté.

 Voici la liste dans l'ordre des fonctions qui se lanceront via ce mode, et ainsi qu'un bref résumé des methodes qui seront également décrites plus tard :

   1. Choix du dossier contenant les images à retoucher, incluant l'ensemble des fichiers présents dans les dossiers / sous-dossiers du dossiers concernés.
 
   2. Supprimer des mots des noms des images.

   3. Renommer avec ou sans le prix via la cote AKOUN, en ajoutant des "," délimitant chaques parties du nom afin de formater les images plus éfficacement pour des mots-clés ou leur inclusion dans un tableur.

   4. Ajout d'un filigrane, plus exactement de mots entre l'extension et le reste du texte de l'image(qui pourront également faire office de catégorie dans les futurs tableaux).
    
   5. Créer une liste reprenant le nom des images, et l'enregistre au format .csv, ouvrable avec n'importe quel éditeur de texte, avec Google Drive ou tout simplement Excel. 
 

## 3. Supprimer des mots des noms
Ce bouton permet la suppression d'expressions régulières des noms des images, par exemple si vous ne souhaitez pas de `,` ou un mot en particulier, vous pouvez simplement l'écrire en ajoutant un nouveau mot a supprimé. Ce n'est pas grave si vous laissez des cases vides, utilisez des espaces des symboles ou autre, il n'y a aucune limitation.

Par ailleurs, si vous etes familier avec Python, vous pouvez également rentrer du code dans les cases destiné à `regex`, la librairie `re` qui est utilisé dans ce programme pour supprimer des patterns d'expressions.

Par exemple, imaginons le cas ou vous avez à supprimer des prix du nom de vos fichiers, vous pouvez utiliser: 

```
\d+(?:[,.]\d{1,2})?\s*(?i)((?<=\s)|(?<=\d)(?=\s*x)|$)(euros?|eur|euro|e)(?=\s|$)
```
1. `\d+` : correspond à une suite de chiffres d'une longueur quelconque (au moins un chiffre).

2. `(?:[,.]\d{1,2})?` : correspond à un point ou une virgule suivi de deux chiffres décimaux, éventuellement présents (l'expression est facultative grâce au `?`).

3. `\s*` : correspond à zéro ou plusieurs caractères d'espacement (espaces, tabulations, etc.).

4. `(?i)` : active le mode insensible à la casse, ce qui permet de matcher indifféremment les majuscules et les minuscules.

5. `((?<=\s)|(?<=\d)(?=\s*x)|$)` : utilise des assertions pour limiter la correspondance à certains cas précis :

    - `(?<=\s)` : correspond à une position qui suit immédiatement un caractère d'espacement.

    - `(?<=\d)(?=\s*x)` : correspond à une position qui suit immédiatement un chiffre, et qui est suivie immédiatement par un caractère `x` précédé ou non d'espaces.

    -  `$` : correspond à la fin de la chaîne.

6. `(euros?|eur|euro|e)` : correspond à l'une des chaînes de caractères `euro`, `euros`, `eur` ou `e`.

7. `(?=\s|$)` : correspond à une position qui précède immédiatement un caractère d'espacement ou la fin de la chaîne.


## 4. Renommer les images avec la cote AKOUN

Ce bouton vous permet globalement de renommer toute les images présentes dans les dossiers et sous-dossiers du dossier sélectionné, voici ses fonctions :

1. Pour commencer il va récupérer les données de taille présent dans les noms, si il n'y en a pas, il calculera automatiquement la taille de l'image en fonction des métadonnées de pixels, et de résolution des images. 

     - Si les pixels par pouces (la résolution) n'est pas renseignée, il appliquera un ratio pour une image avec une résolution de 300dpi par défaut. 

     - Si pour une raison quelconque il n'y a pas de tailles définies dans les métadonnées de l'image, apres un message d'erreur, il appliquera un ratio de base : 1cm = environ 37 pixels, il n'est pas conseillé de garder cette taille  car elle ne sera pas forcément correcte.

     - Si les images n'ont pas de profondeur (c'est a dire de 1, ou de 0), il ne prendra pas en compte la profondeur dans le calcul du prix via la cote akoun.

ⁿᵒᵗᵉ *Pour les images possedant une taille il faut qu'elle soit au format `00x00cm` ou `00x00x00cm`, afin que la detection de taille s'effectue*

2. Une fois la taille trouvée il va essayer de la formater correctement, puis il ajoutera un prix défini par la cote AKOUN qu'il vous sera demandé d'entrer.

Le prix est défini selon ce calcul : 

```
Prix = ((Longueur x hauteur x profondeur ) x Cote Akoun)/3250
```

ⁿᵒᵗᵉ *Si vous n'entrez pas de cote AKOUN, le nouveau nom ne contiendra aucun prix*

3. Pour finir le logiciel attribuera un nouveau nom contenant toute les informations, avec chaque catégories séparées par des `,`. J'ai jugé cette délimitation utile pour plusieurs raisons : 
 
   - Le nom est plus facile à lire.
   - Cela aide pour le référencement dans les grandes bases de données d'images présente dans les moteur de recherche.
   - Mais plus important encore, cela permet de créer facilement des listes ou des tableaux avec des catégories pour vos images.


## 5. Ajout de texte dans les noms

Cette fonction vous permet d'ajouter un filigrane, pour certaines raisons les symboles autre que les espaces ne sont pas autorisés.
par exemple vous pouvez donné une indication pour votre site ; art nathacha com.


ⁿᵒᵗᵉ *Ce nouveu texte viendra accompagné d'une `,` le précédent, par conséquent lors de la prochaine fonction il sera pris en compte comme étant une nouvelle catégorie.

## 6. Créer une liste

Cette fonction va lister toute vos images présente dans tout les dossiers et sous dossier du répertoire que vous avez ouvert, cette liste sera au format .csvn qui est un format excel lu par google drive par exemple, mais vous pouvez également l'ouvrir sous forme de texte en changeant l'extension de fichier en .txt, ou autre.

Vous aurez une option pour créer une liste regroupant tout les dossiers et sous-dossiers, mais également la possibilité de créer une liste dans chaque sous-dossiers.

ⁿᵒᵗᵉ *Lorsque vous créer une liste, si une liste du meme nom est présente dans le dossier, ses informations seront totalement remplacées par les nouvelles, il est possible de faire en sorte de les ajouter plutot que de les supprimer en remplacant le `w` dans le code python par `a`, a la ligne correspondant à l'enregistrement des fichiers, je peux également faire parraitre ca sous forme de bouton au besoin, n'hésitez pas à demander cette fonction.*

## 7. Tout renommer aléatoirement 
Cette fonction génère des noms aléatoires pour chaque images présentes dans les sous-dossiers ou dossiers d'un répertoire choisis au préalable.


## 8. Remplacement de mots dans les noms
Tout est dit dans le titre, cette fonction remplace les mots présents dans les noms par ceux que vous souhaitez, il vous suffira de lire les instructions, d'entrer les mots dans les bonnes cases puis de cliquer sur le boutton "remplacer les mots".


## 9. Renommer selon une suite

Ce bouton permet de renommer toute les images contenues dans un dossier choisi, **AINSI QUE** toute celles présente dans les sous-dossiers inclus dans ce dernier. Le renommage se fera selon une suite 1.jpg 2.png 3........

ⁿᵒᵗᵉ *Initialement cette fonction étaie prévue pour pouvoir remplacer les noms plus facilement via une liste, ou plus exactement un tableau `.csv`, le tout exécuté par l'appuie d'un 6eme bouton, mais je n'ai pas réussi avec python à convertir l'encodage des listes pour chaque type d'os, par conséquent cette fonction est en stanby pour le moment, pareil si vous en avez vraiment besoin, je reste apte à l'implémenter*





Ci dessous vous avez un tutoriel en anglais sur comment lancer ou créer un executable par vous meme : 

```
___ _  _ ___ ____ ____ _ ____ _    
 |  |  |  |  |  | |__/ | |__| |    
 |  |__|  |  |__| |  \ | |  | |___ 
                                   
```

Voici un tutoriel expliquant les différentes façons d'exécuter les fichiers :


# Pour les utilisateurs de **MAC** & **Linux** :

Comme ce script est conçu pour les utilisateurs de Windows, vous devriez probablement commencer par améliorer le code.

Voici cependant la procédure à suivre pour exécuter le script :

* [ MAC ] ; https://macosx-faq.com/how-to-run-python-script/
* [ LINUX ] ; ouvrir un terminal puis `cd` jusqu'au script et taper :

```
python script.pyw
```
(où `script.pyw` est évidemment le nom de ce que vous avez téléchargé)


# Pour les utilisateurs microsoft;

Comme ce script est créé par pyinstaller, il pourrait être détecté comme un logiciel malveillant puisque non signé, mais il n'en est rien, de toute manières vous avez le code.

Voici les possibilités d'exécuter le script ; 

## 1. En cliquant simplement sur l( APPLICATION.exe

Le fichier `.exe` est une version portable faite pour les utilisateurs de Microsoft avec pyinstaller, vous ne pouvez télécharger que ce fichier et rien d'autre.

## 2. Lancer avec Python

`Script` est un répertoire contenant le script original pour python 3.11. 

Si vous avez une version inférieure, vous devrez peut-être télécharger des modules importés qui ne sont pas inclus dans votre version. 

Il suffit de lire les premières lignes du script sous l'installation avec un editeur de texte (visual studio code, ...) ou autre pour trouver ce qui manque.

Si vous souhaitez utiliser python **Vous aurez besoin de l'image `.png` placée dans le dossier `ico`**.

Vous pouvez également ajouter un `w` à l'extension (comme `script.pyw`). Cela signifie `windowed mode`, pour lancer le script python sans le CMD mais c'est toujours un fichier python commun.


## 3. Compiler le script vous meme

### Instructions 

Pour créer votre propre exécutable à partir du fichier python, vous devez installer pyinstaller et python. 

Voici les étapes à suivre :

* Télécharger python 3.11.1

N'oubliez pas de l'ajouter à votre chemin d'accès avec l'installeur ou dans l'environnement des variables ( donc redémarrez votre PC après l'installation ), voici le lien : https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe

* Ouvrez votre CMD en tant qu'administrateur et tapez la commande suivante :

```
python -m pip install pyinstaller
```

* Une fois l'installation terminée, tapez la commande suivante dans votre fenêtre cmd, en remplaçant les chemins d'accès aux fichiers par les vôtres :

```
pyinstaller --onefile --icon="...YOUR PATH.../YOUR ICON.ico" --add-data "...YOUR PATH.../ico;ico" --noconsole test.py

```

Voici l'explication des différentes options :

- `--onefile` : crée un seul exécutable qui inclut toutes les dépendances.

- `--icon=icon.ico` : spécifie l'icône à utiliser pour l'exécutable (remplacez icon.ico par le chemin vers votre fichier d'icône).

- `--add-data "path/to/file;folder_name"` :

ajoute les fichiers externes requis par le programme. Le chemin d'accès au fichier et le nom du dossier dans lequel le fichier sera extrait doivent être séparés par un point-virgule `;`. Vous pouvez ajouter plusieurs fichiers en les séparant par des points-virgules.

- ` script.py` : spécifie le nom de votre script Python.

- ` --noconsole` : cache la console lorsque l'exécutable est lancé.

Veillez à remplacer les parties coupées par les noms de vos fichiers et dossiers. Notez également que le chemin d'accès doit être spécifié en fonction du système d'exploitation sur lequel vous travaillez.

Après avoir exécuté cette commande, vous devriez avoir un seul exécutable qui inclut toutes les dépendances, les fichiers externes et une icône personnalisée, et qui n'affiche pas la console lors de l'exécution.

Vous pouvez également :

## 4. Créer un fichier batch à exécuter 

- [ ] Créer un fichier texte

- [ ] Dans le fichier texte, tapez et écrivez (et changez/complétez le chemin, le premier est pour python, le second pour script.py) ;

```
C:\YOUR PATH TO PYTHON \python.exe" "C:\ **YOUR PATH TO THE SCRIPT** \script.pyw"
```

Si Python est dans le chemin, vous pouvez simplement ; 

```
python "C:\ **YOUR PATH TO THE SCRIPT** \script.pyw"
```

- [ ] Renommez le `new_file.txt` par `script.bat` puis cliquez simplement sur et le programme s'exécutera.

```
     _ ._  _ , _ ._            _ ._  _ , _ ._    _ ._  _ , _ ._      _ ._  _ , _ .__  _ , _ ._   ._  _ , _ ._   _ , _ ._   .---.  _ ._   _ , _ .__  _ , _ ._   ._  _ , _ ._      _ ._  _ , _ .__  _ , _ . .---<__. \ _
   (_ ' ( `  )_  .__)        (_ ' ( `  )_  .__ (_ ' ( `  )_  .__)  (_ '    ___   ._( `  )_  .__)  ( `  )_  .__)   )_  .__)/     \(_ ' (    )_  ._( `  )_  .__)  ( `  )_  .__)  (_ ' ( `  )_  ._( `` )_  . `---._  \ \ \
 ( (  (    )   `)  ) _)    ( (  (    )   `)  ) (  (    )   `)  ) _ (  (   (o o) )     )   `)  ) _    )   `)  ) _    `)  ) \.@-@./(  (    )   `)     )   `)  ) _    )   `)  ) _ (  (    )   `)         `) ` ),----`- `.))  
(__ (_   (_ . _) _) ,__)  (__ (_   (_ . _) _) _ (_   (_ . _) _) ,__ (_   (  V  ) _) (_ . _) _) ,_  (_ . _) _) ,_ . _) _) ,/`\_/`\ (_   (  . _) _) (_ . _) _) ,_  (_ . _) _) ,__ (_   (_ . _) _) (__. _) _)/ ,--.   )  |
    `~~`\ ' . /`~~`           `~~`\ ' . /`~~`   `~~`\ ' . /`~~`     `~~`/--m-m- ~~`\ ' . /`~~`   `\ ' . /`~~`  `\ ' . /  //  _  \\ ``\ '  . /`~~`\ ' . /`~~`   `\ ' . /`~~`     `~~`\ ' . /`~~`\ ' . /`~~/_/    >     |
         ;   ;                     ;   ;             ;   ;               ;   ;      ;   ;          ;   ;         ;   ;  | \     )|_   ;    ;      ;   ;          ;   ;               ;   ;      ;   ;    |,\__-'      |
         /   \                     /   \             /   \               /   \      /   \          /   \         /   \ /`\_`>  <_/ \  /    \      /   \          /   \               /   \      /   \     \__         \
________/_ __ \___________________/_ __ \___________/_ __ \______ __ ___/_ __ \____/_ __ \________/_ __ \_______/_ __ \\__/'---'\__/_/_  __ \____/_ __ \________/_ __ \_____ _______/_ __ \____/_ __ \____ __\___      )
```

