[![Download AKOUN trieur](https://img.shields.io/sourceforge/dt/trieur.svg)](https://sourceforge.net/projects/trieur/files/latest/download)
Trieur version 1.0.1 | Python version 3.11.1 | 🇫🇷 | For every OS but run better on Windows 
```
██╗     ██╗███████╗████████╗███████╗███████╗
██║     ██║██╔════╝╚══██╔══╝██╔════╝██╔════╝
██║     ██║███████╗   ██║   █████╗  ███████╗
██║     ██║╚════██║   ██║   ██╔══╝  ╚════██║
███████╗██║███████║   ██║   ███████╗███████║
╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚══════╝
                                            
```



# Améliore la gestion de vos oeuvres d'art informatisée !

Ce logiciel permet aux artistes cotés AKOUN, tels que Nathacha , artiste peintre de l'abstraction https://www.artnathacha.com/ , à créer plus rapidement une liste de prix relative à leur cotation pour leurs oeuvres (ou à des fins éducatives). Il permet également de manipuler ces listes ainsi que les fichiers, dans le but de les trier, manipuler plus facilement.

Il permet également de renommer par lot d'images, d'ajouter ou d'y retirer des mots réccurents, mais aussi de créer des tableaux excel pour une comptabilité plus rapide,une meilleure gestion des stocks. 

**Notez qu'il demande l'ouverture d'un dossier, mais qu'il traite le contenu de tout les sous-dossiers présents à l'interieur, donc pensez à faire une copie de vos fichiers avant de les manipuler afin d'éviter une perte de donnée !**

ⁿᵒᵗᵉ *Un bon anti-malware vous donnera toujours un faux positif pour le fichier .exe puisqu'il n'est pas signé, cependant vous avez le code et j'ai meme écris une notice sur comment compiler le programme vous meme.*

[![Download AKOUN trieur](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/trieur/files/latest/download)


Voici un apercus du logiciel (Version 0.9.9.9999999) : 


![global](https://user-images.githubusercontent.com/92639080/222796734-14c65748-d69a-421f-8ce5-9613ffb8b987.png)

# Contenu et utilisation

IMPORTANT : Pour commencer, veuillez noter que ce logiciel va modifier directement TOUT les fichiers présents dans TOUT les dossiers et sous dossiers du dossier ouvert, pensez à faire une copie de vos dossier avant toute chose pour limiter les risques de perte de données !

## 1. Supprimer des mots des noms
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


## 2. Renommer les images avec la cote AKOUN

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


## 3. Ajout de texte dans les noms

Cette fonction vous permet d'ajouter un filigrane, pour certaines raisons les symboles autre que les espaces ne sont pas autorisés.
par exemple vous pouvez donné une indication pour votre site ; art nathacha com.


ⁿᵒᵗᵉ *Ce nouveu texte viendra accompagné d'une `,` le précédent, par conséquent lors de la prochaine fonction il sera pris en compte comme étant une nouvelle catégorie.

## 4. Créer une liste

Cette fonction va lister toute vos images présente dans tout les dossiers et sous dossier du répertoire que vous avez ouvert, cette liste sera au format .csvn qui est un format excel lu par google drive par exemple, mais vous pouvez également l'ouvrir sous forme de texte en changeant l'extension de fichier en .txt, ou autre.

Vous aurez une option pour créer une liste regroupant tout les dossiers et sous-dossiers, mais également la possibilité de créer une liste dans chaque sous-dossiers.

ⁿᵒᵗᵉ *Lorsque vous créer une liste, si une liste du meme nom est présente dans le dossier, ses informations seront totalement remplacées par les nouvelles, il est possible de faire en sorte de les ajouter plutot que de les supprimer en remplacant le `w` dans le code python par `a`, a la ligne correspondant à l'enregistrement des fichiers, je peux également faire parraitre ca sous forme de bouton au besoin, n'hésitez pas à demander cette fonction.*

## 5. Renommer selon une suite

Ce bouton permet de renommer toute les images contenues dans un dossier choisi, **AINSI QUE** toute celles présente dans les sous-dossiers inclus dans ce dernier. Le renommage se fera selon une suite 1.jpg 2.png 3........

ⁿᵒᵗᵉ *Initialement cette fonction étaie prévue pour pouvoir remplacer les noms plus facilement via une liste, ou plus exactement un tableau `.csv`, le tout exécuté par l'appuie d'un 6eme bouton, mais je n'ai pas réussi avec python à convertir l'encodage des listes pour chaque type d'os, par conséquent cette fonction est en stanby pour le moment, pareil si vous en avez vraiment besoin, je reste apte à l'implémenter*





Ci dessous vous avez un tutoriel en anglais sur comment lancer ou créer un executable par vous meme : 

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
(where `script.pyw` is obviously the name of what you've downloaded)


# For microsoft users;

Because this script is made by pyinstaller it could be detected as a malware.

Here are possibilities to run the script; 

## 1. Run by simple click on APPLICATION.exe

The .exe file is a portable version made for microsoft users with pyinstaller, you can download only this file and nothing else.


## 2. Run with Python

`Python script` is directory with the original script for python 3.11. 

In case you have a lower version you may have to download module imported not included with your version. 
Just read the first lines of the script in Alexandria with a notepad or whatever to find what's missing.

If you would like to run with python **YOU WILL NEED THE IMAGE .png PLACED IN THE SAME DIRECTORY OF THE RUNNING SCRIPT**.

Also you can add a w to the extension (like `script.pyw`). It means `windowed mode`, to launch the python script without the CMD but it's still a common python file.


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

- `--onefile` :creates a single executable that includes all dependencies.

- `--icon=icon.ico` :specifies the icon to use for the executable (replace icon.ico with the path to your icon file).

- `--add-data "path/to/file;folder_name"` :

adds external files required by the program. The path to the file and the name of the folder in which the file will be extracted should be separated by a semicolon `;`. You can add multiple files by separating them with semicolons.

- ` script.py`: specifies the name of your Python script.

- ` --noconsole` : hides the console when the executable is run.


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

- [ ] Rename the `new_file.txt` by `script.bat` then just click on and it will run the progra

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

