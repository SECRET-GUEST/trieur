[![Download AKOUN trieur](https://img.shields.io/sourceforge/dt/trieur.svg)](https://sourceforge.net/projects/trieur/files/latest/download)
Trieur version 1.0.3 | Python version 3.11.1 | π«π· | For every OS but run better on Windows 
```
ββββββββββββββββ ββββββββββββββ   ββββββββββ      ββββββ βββ  βββ βββββββ βββ   βββββββ   βββ
βββββββββββββββββββββββββββββββ   βββββββββββ    βββββββββββ ββββββββββββββββ   ββββββββ  βββ
   βββ   βββββββββββββββββ  βββ   βββββββββββ    βββββββββββββββ βββ   ββββββ   βββββββββ βββ
   βββ   βββββββββββββββββ  βββ   βββββββββββ    βββββββββββββββ βββ   ββββββ   βββββββββββββ
   βββ   βββ  ββββββββββββββββββββββββββ  βββ    βββ  ββββββ  ββββββββββββββββββββββββ ββββββ
   βββ   βββ  ββββββββββββββ βββββββ βββ  βββ    βββ  ββββββ  βββ βββββββ  βββββββ βββ  βββββ
                                                                                             
                                            
```


# AmΓ©liore la gestion de vos oeuvres d'art informatisΓ©e !

Ce logiciel permet aux artistes cotΓ©s AKOUN, tels que Nathacha , artiste peintre de l'abstraction https://www.artnathacha.com/ , Γ  crΓ©er plus rapidement une liste de prix relative Γ  leur cotation pour leurs oeuvres (ou Γ  des fins Γ©ducatives). Il permet Γ©galement de manipuler ces listes ainsi que les fichiers, dans le but de les trier, manipuler plus facilement.

Il permet Γ©galement de renommer par lot d'images, d'ajouter ou d'y retirer des mots rΓ©ccurents, mais aussi de crΓ©er des tableaux excel pour une comptabilitΓ© plus rapide,une meilleure gestion des stocks. 

**Notez qu'il demande l'ouverture d'un dossier, mais qu'il traite le contenu de tout les sous-dossiers prΓ©sents Γ  l'interieur, donc pensez Γ  faire une copie de vos fichiers avant de les manipuler afin d'Γ©viter une perte de donnΓ©e !**

βΏα΅α΅α΅ *Un bon anti-malware vous donnera toujours un faux positif pour le fichier .exe puisqu'il n'est pas signΓ©, cependant vous avez le code et j'ai meme Γ©cris une notice sur comment compiler le programme vous meme.*

[![Download AKOUN trieur](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/trieur/files/latest/download)


# En cours de developpement : 

Les diffΓ©rentes sujes dΓ©crits dans cette liste ne sont prΓ©sent qu'Γ  titre informatif, la liste ne sera ni exhaustive, ni dΓ©finitive, ou encore inΓ©luctable.

* Fonction de clic automatique
* Corrections de bugs
* Ajout d'un menu
* Optimisation du code
* AmΓ©lioration de l'interface visuelle
* Creation de l'application pour tablette/smartphone (Android et Apple)
* Diversifier les possibilitΓ© de listes, txt, pdf...
* Themes reglable pour l'application
* Incorporation de listes de mots personnels pour la gΓ©nΓ©ration de noms alΓ©atoire
* Fonction pour hoisir le type de mΓ©dia ciblΓ© (autre que les images)
* Fonction pour renommer par d'autres moyen de tri, par exemple "modifier le", par "type",...
* Fonction pour convertir des types de fichiers en d'autres type Γ  l'aide d'FFMPEG

Voici un apercu du logiciel (Version 0.9.9.9999999) : 


![global](https://user-images.githubusercontent.com/92639080/222796734-14c65748-d69a-421f-8ce5-9613ffb8b987.png)

# Contenu et utilisation

IMPORTANT : Pour commencer, veuillez noter que ce logiciel va modifier directement TOUT les fichiers prΓ©sents dans TOUT les dossiers et sous dossiers du dossier ouvert, pensez Γ  faire une copie de vos dossier avant toute chose pour limiter les risques de perte de donnΓ©es !

βΏα΅α΅α΅ *Le logiciel gΓ©nΓ¨re un fichier errors.log ainsi qu'un fichier config.ini Γ  la racine du repertoire ou il aura Γ©tΓ© lancΓ©, Γ  chaque fois qu'il le sera. Vous pouvez supprimez ces fichiers sans soucis, ils ne servent qu'a retenir vos preferences et Γ  afficher les possibles erreurs rencontrΓ©e.*

## 1. D4rk/l1ght mode
Bon, je pense pas vraiment avoir Γ  prΓ©senter ce mode, mais dans le cas ou vous viviez dans une grotte jusqu'Γ  maintenant, ce boutton permet d'afficher le thΓ¨me colorΓ© du logiciel selon mode souhaitΓ© par l'utilisateur, dark pour gagner en confort durant la nuit, ou pour les personnes ayant les yeux plus sensibles et inversement. 

## 2. Tout en un
Permet de travailler plus rapidement en lanΓ§ant automatiquement une Γ  une les fonctions principales de cette liste.

**Attention** : Une fois le dossier choisi, il n'y a pas de possibilitΓ© de retour en arriΓ¨re jusqu'Γ  que l'ensemble du programme se soit exΓ©cutΓ©.

 Voici la liste dans l'ordre des fonctions qui se lanceront via ce mode, et ainsi qu'un bref rΓ©sumΓ© des methodes qui seront Γ©galement dΓ©crites plus tard :

   1. Choix du dossier contenant les images Γ  retoucher, incluant l'ensemble des fichiers prΓ©sents dans les dossiers / sous-dossiers du dossiers concernΓ©s.
 
   2. Supprimer des mots des noms des images.

   3. Renommer avec ou sans le prix via la cote AKOUN, en ajoutant des "," dΓ©limitant chaques parties du nom afin de formater les images plus Γ©fficacement pour des mots-clΓ©s ou leur inclusion dans un tableur.

   4. Ajout d'un filigrane, plus exactement de mots entre l'extension et le reste du texte de l'image(qui pourront Γ©galement faire office de catΓ©gorie dans les futurs tableaux).
    
   5. CrΓ©er une liste reprenant le nom des images, et l'enregistre au format .csv, ouvrable avec n'importe quel Γ©diteur de texte, avec Google Drive ou tout simplement Excel. 
 

## 3. Supprimer des mots des noms
Ce bouton permet la suppression d'expressions rΓ©guliΓ¨res des noms des images, par exemple si vous ne souhaitez pas de `,` ou un mot en particulier, vous pouvez simplement l'Γ©crire en ajoutant un nouveau mot a supprimΓ©. Ce n'est pas grave si vous laissez des cases vides, utilisez des espaces des symboles ou autre, il n'y a aucune limitation.

Par ailleurs, si vous etes familier avec Python, vous pouvez Γ©galement rentrer du code dans les cases destinΓ© Γ  `regex`, la librairie `re` qui est utilisΓ© dans ce programme pour supprimer des patterns d'expressions.

Par exemple, imaginons le cas ou vous avez Γ  supprimer des prix du nom de vos fichiers, vous pouvez utiliser: 

```
\d+(?:[,.]\d{1,2})?\s*(?i)((?<=\s)|(?<=\d)(?=\s*x)|$)(euros?|eur|euro|e)(?=\s|$)
```
1. `\d+` : correspond Γ  une suite de chiffres d'une longueur quelconque (au moins un chiffre).

2. `(?:[,.]\d{1,2})?` : correspond Γ  un point ou une virgule suivi de deux chiffres dΓ©cimaux, Γ©ventuellement prΓ©sents (l'expression est facultative grΓ’ce au `?`).

3. `\s*` : correspond Γ  zΓ©ro ou plusieurs caractΓ¨res d'espacement (espaces, tabulations, etc.).

4. `(?i)` : active le mode insensible Γ  la casse, ce qui permet de matcher indiffΓ©remment les majuscules et les minuscules.

5. `((?<=\s)|(?<=\d)(?=\s*x)|$)` : utilise des assertions pour limiter la correspondance Γ  certains cas prΓ©cis :

    - `(?<=\s)` : correspond Γ  une position qui suit immΓ©diatement un caractΓ¨re d'espacement.

    - `(?<=\d)(?=\s*x)` : correspond Γ  une position qui suit immΓ©diatement un chiffre, et qui est suivie immΓ©diatement par un caractΓ¨re `x` prΓ©cΓ©dΓ© ou non d'espaces.

    -  `$` : correspond Γ  la fin de la chaΓ?ne.

6. `(euros?|eur|euro|e)` : correspond Γ  l'une des chaΓ?nes de caractΓ¨res `euro`, `euros`, `eur` ou `e`.

7. `(?=\s|$)` : correspond Γ  une position qui prΓ©cΓ¨de immΓ©diatement un caractΓ¨re d'espacement ou la fin de la chaΓ?ne.


## 4. Renommer les images avec la cote AKOUN

Ce bouton vous permet globalement de renommer toute les images prΓ©sentes dans les dossiers et sous-dossiers du dossier sΓ©lectionnΓ©, voici ses fonctions :

1. Pour commencer il va rΓ©cupΓ©rer les donnΓ©es de taille prΓ©sent dans les noms, si il n'y en a pas, il calculera automatiquement la taille de l'image en fonction des mΓ©tadonnΓ©es de pixels, et de rΓ©solution des images. 

     - Si les pixels par pouces (la rΓ©solution) n'est pas renseignΓ©e, il appliquera un ratio pour une image avec une rΓ©solution de 300dpi par dΓ©faut. 

     - Si pour une raison quelconque il n'y a pas de tailles dΓ©finies dans les mΓ©tadonnΓ©es de l'image, apres un message d'erreur, il appliquera un ratio de base : 1cm = environ 37 pixels, il n'est pas conseillΓ© de garder cette taille  car elle ne sera pas forcΓ©ment correcte.

     - Si les images n'ont pas de profondeur (c'est a dire de 1, ou de 0), il ne prendra pas en compte la profondeur dans le calcul du prix via la cote akoun.

βΏα΅α΅α΅ *Pour les images possedant une taille il faut qu'elle soit au format `00x00cm` ou `00x00x00cm`, afin que la detection de taille s'effectue*

2. Une fois la taille trouvΓ©e il va essayer de la formater correctement, puis il ajoutera un prix dΓ©fini par la cote AKOUN qu'il vous sera demandΓ© d'entrer.

Le prix est dΓ©fini selon ce calcul : 

```
Prix = ((Longueur x hauteur x profondeur ) x Cote Akoun)/3250
```

βΏα΅α΅α΅ *Si vous n'entrez pas de cote AKOUN, le nouveau nom ne contiendra aucun prix*

3. Pour finir le logiciel attribuera un nouveau nom contenant toute les informations, avec chaque catΓ©gories sΓ©parΓ©es par des `,`. J'ai jugΓ© cette dΓ©limitation utile pour plusieurs raisons : 
 
   - Le nom est plus facile Γ  lire.
   - Cela aide pour le rΓ©fΓ©rencement dans les grandes bases de donnΓ©es d'images prΓ©sente dans les moteur de recherche.
   - Mais plus important encore, cela permet de crΓ©er facilement des listes ou des tableaux avec des catΓ©gories pour vos images.


## 5. Ajout de texte dans les noms

Cette fonction vous permet d'ajouter un filigrane, pour certaines raisons les symboles autre que les espaces ne sont pas autorisΓ©s.
par exemple vous pouvez donnΓ© une indication pour votre site ; art nathacha com.


βΏα΅α΅α΅ *Ce nouveu texte viendra accompagnΓ© d'une `,` le prΓ©cΓ©dent, par consΓ©quent lors de la prochaine fonction il sera pris en compte comme Γ©tant une nouvelle catΓ©gorie.

## 6. CrΓ©er une liste

Cette fonction va lister toute vos images prΓ©sente dans tout les dossiers et sous dossier du rΓ©pertoire que vous avez ouvert, cette liste sera au format .csvn qui est un format excel lu par google drive par exemple, mais vous pouvez Γ©galement l'ouvrir sous forme de texte en changeant l'extension de fichier en .txt, ou autre.

Vous aurez une option pour crΓ©er une liste regroupant tout les dossiers et sous-dossiers, mais Γ©galement la possibilitΓ© de crΓ©er une liste dans chaque sous-dossiers.

βΏα΅α΅α΅ *Lorsque vous crΓ©er une liste, si une liste du meme nom est prΓ©sente dans le dossier, ses informations seront totalement remplacΓ©es par les nouvelles, il est possible de faire en sorte de les ajouter plutot que de les supprimer en remplacant le `w` dans le code python par `a`, a la ligne correspondant Γ  l'enregistrement des fichiers, je peux Γ©galement faire parraitre ca sous forme de bouton au besoin, n'hΓ©sitez pas Γ  demander cette fonction.*

## 7. Tout renommer alΓ©atoirement 
Cette fonction gΓ©nΓ¨re des noms alΓ©atoires pour chaque images prΓ©sentes dans les sous-dossiers ou dossiers d'un rΓ©pertoire choisis au prΓ©alable.


## 8. Remplacement de mots dans les noms
Tout est dit dans le titre, cette fonction remplace les mots prΓ©sents dans les noms par ceux que vous souhaitez, il vous suffira de lire les instructions, d'entrer les mots dans les bonnes cases puis de cliquer sur le boutton "remplacer les mots".


## 9. Renommer selon une suite

Ce bouton permet de renommer toute les images contenues dans un dossier choisi, **AINSI QUE** toute celles prΓ©sente dans les sous-dossiers inclus dans ce dernier. Le renommage se fera selon une suite 1.jpg 2.png 3........

βΏα΅α΅α΅ *Initialement cette fonction Γ©taie prΓ©vue pour pouvoir remplacer les noms plus facilement via une liste, ou plus exactement un tableau `.csv`, le tout exΓ©cutΓ© par l'appuie d'un 6eme bouton, mais je n'ai pas rΓ©ussi avec python Γ  convertir l'encodage des listes pour chaque type d'os, par consΓ©quent cette fonction est en stanby pour le moment, pareil si vous en avez vraiment besoin, je reste apte Γ  l'implΓ©menter*





Ci dessous vous avez un tutoriel en anglais sur comment lancer ou crΓ©er un executable par vous meme : 

```
___ _  _ ___ ____ ____ _ ____ _    
 |  |  |  |  |  | |__/ | |__| |    
 |  |__|  |  |__| |  \ | |  | |___ 
                                   
```

Voici un tutoriel expliquant les diffΓ©rentes faΓ§ons d'exΓ©cuter les fichiers :


# Pour les utilisateurs de **MAC** & **Linux** :

Comme ce script est conΓ§u pour les utilisateurs de Windows, vous devriez probablement commencer par amΓ©liorer le code.

Voici cependant la procΓ©dure Γ  suivre pour exΓ©cuter le script :

* [ MAC ] ; https://macosx-faq.com/how-to-run-python-script/
* [ LINUX ] ; ouvrir un terminal puis `cd` jusqu'au script et taper :

```
python script.pyw
```
(oΓΉ `script.pyw` est Γ©videmment le nom de ce que vous avez tΓ©lΓ©chargΓ©)


# Pour les utilisateurs microsoft;

Comme ce script est crΓ©Γ© par pyinstaller, il pourrait Γͺtre dΓ©tectΓ© comme un logiciel malveillant puisque non signΓ©, mais il n'en est rien, de toute maniΓ¨res vous avez le code.

Voici les possibilitΓ©s d'exΓ©cuter le script ; 

## 1. En cliquant simplement sur l( APPLICATION.exe

Le fichier `.exe` est une version portable faite pour les utilisateurs de Microsoft avec pyinstaller, vous ne pouvez tΓ©lΓ©charger que ce fichier et rien d'autre.

## 2. Lancer avec Python

`Script` est un rΓ©pertoire contenant le script original pour python 3.11. 

Si vous avez une version infΓ©rieure, vous devrez peut-Γͺtre tΓ©lΓ©charger des modules importΓ©s qui ne sont pas inclus dans votre version. 

Il suffit de lire les premiΓ¨res lignes du script sous l'installation avec un editeur de texte (visual studio code, ...) ou autre pour trouver ce qui manque.

Si vous souhaitez utiliser python **Vous aurez besoin de l'image `.png` placΓ©e dans le dossier `ico`**.

Vous pouvez Γ©galement ajouter un `w` Γ  l'extension (comme `script.pyw`). Cela signifie `windowed mode`, pour lancer le script python sans le CMD mais c'est toujours un fichier python commun.


## 3. Compiler le script vous meme

### Instructions 

Pour crΓ©er votre propre exΓ©cutable Γ  partir du fichier python, vous devez installer pyinstaller et python. 

Voici les Γ©tapes Γ  suivre :

* TΓ©lΓ©charger python 3.11.1

N'oubliez pas de l'ajouter Γ  votre chemin d'accΓ¨s avec l'installeur ou dans l'environnement des variables ( donc redΓ©marrez votre PC aprΓ¨s l'installation ), voici le lien : https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe

* Ouvrez votre CMD en tant qu'administrateur et tapez la commande suivante :

```
python -m pip install pyinstaller
```

* Une fois l'installation terminΓ©e, tapez la commande suivante dans votre fenΓͺtre cmd, en remplaΓ§ant les chemins d'accΓ¨s aux fichiers par les vΓ΄tres :

```
pyinstaller --onefile --icon="...YOUR PATH.../YOUR ICON.ico" --add-data "...YOUR PATH.../ico;ico" --noconsole test.py

```

Voici l'explication des diffΓ©rentes options :

- `--onefile` : crΓ©e un seul exΓ©cutable qui inclut toutes les dΓ©pendances.

- `--icon=icon.ico` : spΓ©cifie l'icΓ΄ne Γ  utiliser pour l'exΓ©cutable (remplacez icon.ico par le chemin vers votre fichier d'icΓ΄ne).

- `--add-data "path/to/file;folder_name"` :

ajoute les fichiers externes requis par le programme. Le chemin d'accΓ¨s au fichier et le nom du dossier dans lequel le fichier sera extrait doivent Γͺtre sΓ©parΓ©s par un point-virgule `;`. Vous pouvez ajouter plusieurs fichiers en les sΓ©parant par des points-virgules.

- ` script.py` : spΓ©cifie le nom de votre script Python.

- ` --noconsole` : cache la console lorsque l'exΓ©cutable est lancΓ©.

Veillez Γ  remplacer les parties coupΓ©es par les noms de vos fichiers et dossiers. Notez Γ©galement que le chemin d'accΓ¨s doit Γͺtre spΓ©cifiΓ© en fonction du systΓ¨me d'exploitation sur lequel vous travaillez.

AprΓ¨s avoir exΓ©cutΓ© cette commande, vous devriez avoir un seul exΓ©cutable qui inclut toutes les dΓ©pendances, les fichiers externes et une icΓ΄ne personnalisΓ©e, et qui n'affiche pas la console lors de l'exΓ©cution.

Vous pouvez Γ©galement :

## 4. CrΓ©er un fichier batch Γ  exΓ©cuter 

- [ ] CrΓ©er un fichier texte

- [ ] Dans le fichier texte, tapez et Γ©crivez (et changez/complΓ©tez le chemin, le premier est pour python, le second pour script.py) ;

```
C:\YOUR PATH TO PYTHON \python.exe" "C:\ **YOUR PATH TO THE SCRIPT** \script.pyw"
```

Si Python est dans le chemin, vous pouvez simplement ; 

```
python "C:\ **YOUR PATH TO THE SCRIPT** \script.pyw"
```

- [ ] Renommez le `new_file.txt` par `script.bat` puis cliquez simplement sur et le programme s'exΓ©cutera.

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

