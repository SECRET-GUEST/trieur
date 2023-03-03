# EN COURS DE DEVELOPPEMENT, pertes de temps à cause de problèmes personnels, je met les versions executables dés que j'aurai fini de travaillé l'HTML.


Trieur version 1.0.0 | Python version 3.11.1 | 🇫🇷 | Optimal avec windows 11 [![Download AKOUN trieur](https://img.shields.io/sourceforge/dt/trieur.svg)](https://sourceforge.net/projects/trieur/files/latest/download)
```
██╗     ██╗███████╗████████╗███████╗███████╗
██║     ██║██╔════╝╚══██╔══╝██╔════╝██╔════╝
██║     ██║███████╗   ██║   █████╗  ███████╗
██║     ██║╚════██║   ██║   ██╔══╝  ╚════██║
███████╗██║███████║   ██║   ███████╗███████║
╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚══════╝
                                            
```



# Présentation : 

Comme dit dans l'énnoncé, ce logiciel permet aux artistes cotés AKOUN tels que Nathacha , artiste peintre de l'abstraction https://www.artnathacha.com/ , à créer plus rapidement une liste de prix relative à leu cotation pour leurs oeuvres (ou à des fins éducatives). Il permet également de manipuler ces listes ainsi que les fichiers, dans le but de les trier, manipuler plus facilement.

ⁿᵒᵗᵉ *Un bon anti-malware vous donnera toujours un faux positif pour le fichier .exe puisqu'il n'est pas signé, cependant vous avez le code et j'ai meme écris une notice sur comment compiler le programme vous meme.*

[![Download AKOUN trieur](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/trieur/files/latest/download)


## Changements à venir :

- [ ] Correction du nom de chaque images présentes dans tout le dossier, incluant celles présentes dans les sous dossiers.
- [ ] Interface visuelle soignée qui marquera la fin de la beta.



Voici un apercus du logiciel (Version beta 7) : 

![Capture d'écran 2023-03-02 105345](https://user-images.githubusercontent.com/92639080/222394444-8ae8bd33-033c-4cda-ac67-db52cfc8d8f8.png)


# Contenu et utilisation:

IMPORTANT : Pour commencer, veuillez noter que ce logiciel va modifier directement TOUT les fichiers présents dans TOUT les dossiers et sous dossiers du dossier ouvert, pensez à faire une copie de vos dossier avant toute chose pour limiter les risques de perte de données !

## 1. Supprimer des mots des noms; 

Ce bouton permet la suppression d'expressions régulières des noms des images, par exemple si vous ne souhaitez pas de "," ou un mot en particulier, vous pouvez simplement l'écrire en ajoutant un nouveau mot a supprimé. Ce n'est pas grave si vous laissez des cases vides, utilisez des espaces des symboles ou autre, il n'y a aucune limitation.

Par ailleurs, si vous etes familier avec Python, vous pouvez également rentrer du code dans les cases destiné à "regex", la librairie "re" qui est utilisé dans ce programme pour supprimer des patterns d'expressions.

Par exemple, imaginons le cas ou vous avez à supprimer des prix du nom de vos fichiers, vous pouvez utiliser: 

```
\d+(?:[,.]\d{1,2})?\s*(?i)((?<=\s)|(?<=\d)(?=\s*x)|$)(euros?|eur|euro|e)(?=\s|$)
```
* \d+ : correspond à une suite de chiffres d'une longueur quelconque (au moins un chiffre).
(?:[,.]\d{1,2})? : correspond à un point ou une virgule suivi de deux chiffres décimaux, éventuellement présents (l'expression est facultative grâce au ?).

* \s* : correspond à zéro ou plusieurs caractères d'espacement (espaces, tabulations, etc.).

* (?i) : active le mode insensible à la casse, ce qui permet de matcher indifféremment les majuscules et les minuscules.

* ((?<=\s)|(?<=\d)(?=\s*x)|$) : utilise des assertions pour limiter la correspondance à certains cas précis :

 - (?<=\s) : correspond à une position qui suit immédiatement un caractère d'espacement.

 - (?<=\d)(?=\s*x) : correspond à une position qui suit immédiatement un chiffre, et qui est suivie immédiatement par un caractère "x" précédé ou non d'espaces.

 -  $ : correspond à la fin de la chaîne.

* (euros?|eur|euro|e) : correspond à l'une des chaînes de caractères "euro", "euros", "eur" ou "e".

* (?=\s|$) : correspond à une position qui précède immédiatement un caractère d'espacement ou la fin de la chaîne.

## 2. Renommer les images

Ce bouton permet de renommer toute les images contenues dans un dossier choisi, **AINSI QUE** toute celles présente dans les sous-dossiers inclus dans ce dernier. Le renommage se fera selon une suite 1 2 3 4 5 ...

ⁿᵒᵗᵉ *Il est recommandé d'utiliser la fonction de renommage sur une copie de votre dossier afin d'éviter les erreurs, par exemple si vous l'utilisez sur un ordinateur windows, sur des fichiers déja numérotés, les fichiers seront renommés dans cet ordre : 1 10 11 110 111111 2 3 4 .... ce qui peut entrainer pas mal d'erreurs (merci microsoft).*

ⁿᵒᵗᵉ *Un correcteur est à venir, dans l'idéal j'aimerai qu'il supprime toutes données superflue des listes et qu'il corrige la grammaire, il est déja en cours de fabrication, mais pour le moment il est seulement capable de retirer les valeurs "type" 30x40x32cm des listes ainsi que d'autres données plus personnelles, il n'est pas encore inclut dans le logiciel.*

## 3. Chercher la liste

Cette fonction permet de simplement chercher sur quelle liste vous allez travailler

## 4. Cote Akoun

Ici vous devez, comme indiquer, entrer votre cote AKOUN.

## 5. GO!

L'algorithme va trier toutes les données de votre liste si ces dernières sont au bon format. Il créera si besoin de nouveaux dossiers au nom du type de l'oeuvre, ainsi que des listes à l'interieur contenant la liste propre avec le prix des oeuvres.

ⁿᵒᵗᵉ *A venir : apres avoir effectué son tri, le programme assignera à vos images numérotées, le nom correspondant au premier numéro de la liste*

Si vous désirez écrire vous meme ou réécrire les données présentes, voici comment vous devrez procéder :

numero | type d'oeuvre | longueur x hauteur x profondeur | nom de l'oeuvre

+ Par exemple :

- [ ] 1 3D 300 200 0 le petit charles

- [ ] 2 numerique 200 50 1 jean-luc

- [ ] 3 pastel 600 400 10 internet vapor wave 404

...

Voici un exemple d'utilisation du logiciel pour un dossier contenant des oeuvres numérique (Version : beta 3);

![beta2](https://user-images.githubusercontent.com/92639080/216796498-58d8baf0-892f-4680-a1ce-fe1a1936abd2.jpg)

ⁿᵒᵗᵉ *Le logiciel est capable de taiter une liste contenant plusieurs types de dossiers, il triera et rangera les données dans des dossiers/des listes existantes ou non, sans effacer celles qui s'y trouvent déja.*

Il est important de noter que la profondeur est particulière ; 

- [ ] Donner 1 en profondeur pour vos oeuvres produites sur un support tel que le papier, cela annulera la prise en compte de la profondeur dans le calcul de la cote, mais la variable pourra tout de meme etre réutilisée plus tards si besoin.

- [ ] Donner 0 en profondeur aura le meme resultat que si vous donneriez 1, j'ai conservé le 0 pour mieux classer les oeuvres de type numériques.

- [ ] Donner n'importe quelle autre valeur la rendra éffective dans le calcul, arrondissez à l'unité pour éviter les erreurs.

**ʳᵉᵐᵃʳᑫᵘᵉ Le *type* de votre liste NE DEVRA CONTENIR QU'UN SEUL MOT !! Et il ne devra pas contenir de caractère spéciaux tels que "é" ou "+", cela doit rester le plus neutre possible**, c'est tout simplement plus rapide comme ca lors de la prise de notes et de l'écriture du programme.

Les noms de dossiers et des listes seront attribués en fonction du nom du **type** .



```
___ _  _ ___ ____ ____ _ ____ _    
 |  |  |  |  |  | |__/ | |__| |    
 |  |__|  |  |__| |  \ | |  | |___ 
                                   
```

Here a tutorial explaning different ways to run the files :


# For **MAC** & **Linux** users :

Since this script is designed for Windows users, you should probably first improve the code.

However here is the procedure to run the script:

* [ MAC ] ; https://macosx-faq.com/how-to-run-python-script/
* [ LINUX ] ; open a terminal then cd until the script and type

```
python script.pyw
```
(where "script.pyw" is obviously the name of what you've downloaded)


# For microsoft users;

Because this script is made by pyinstaller it could be detected as a malware.

Here are possibilities to run the script; 

## 1. Run by simple click on APPLICATION.exe

The .exe file is a portable version made for microsoft users with pyinstaller, you can download only this file and nothing else.


## 2. Run with Python

"Python script" is directory with the original script for python 3.11. 

In case you have a lower version you may have to download module imported not included with your version. 
Just read the first lines of the script in Alexandria with a notepad or whatever to find what's missing.

If you would like to run with python **YOU WILL NEED THE IMAGE .png PLACED IN THE SAME DIRECTORY OF THE RUNNING SCRIPT**.

Also you can add a w to the extension (like "script.pyw"). It means "windowed mode", to launch the python script without the CMD but it's still a common python file.


## 3. Compile the script by yourself 

### Instructions 

To create your own executable from the python file, you will need to install pyinstaller and python. 

Here are the steps you should follow:

* Download python 3.11.1

Don't forget to add it to your path with the installer or in variables environment ( so reboot your PC after the installation ), here is the link : https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe

* Open your CMD as an administrator and type the following command:

```
python -m pip install pyinstaller
```

* Once the installation is complete, type the following command in your cmd window, replacing the file paths with your own:

```
pyinstaller --onefile --icon="...YOUR PATH.../YOUR ICON.ico" --add-data "...YOUR PATH.../ico;ico" --noconsole test.py

```

Here are the explanations of the different options:

- [ ] --onefile

 creates a single executable that includes all dependencies.

- [ ] --icon=icon.ico

specifies the icon to use for the executable (replace icon.ico with the path to your icon file).

- [ ] --add-data "path/to/file;folder_name"

adds external files required by the program. The path to the file and the name of the folder in which the file will be extracted should be separated by a semicolon (;). You can add multiple files by separating them with semicolons.

- [ ] script.py

specifies the name of your Python script.

- [ ] --noconsole

hides the console when the executable is run.


Make sure to replace the snipped parts with the names of your files and folders. Also note that the path should be specified based on the operating system you are working on.

After running this command, you should have a single executable that includes all dependencies, external files, and a custom icon, and does not show the console when running.

Alternatively you can also :

## 4. Create a batch file to run 

- [ ] Create a text file

- [ ] In the text file type and write (and change/ complete the path, first is for python, 2nd is for script.py);

```
C:\YOUR PATH TO PYTHON \python.exe" "C:\ **YOUR PATH TO THE SCRIPT** \script.pyw"
```

If Python is in path, you can just ; 

```
python "C:\ **YOUR PATH TO THE SCRIPT** \script.pyw"
```

- [ ] Rename the "new_file.txt" by "script.bat" then just click on and it will run the progra

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

