Version : beta 1.0.0 | Python version 3.11.1 | FR | For every OS but run better on Windows

```
████████╗██████╗ ██╗███████╗██╗   ██╗██████╗    ███████╗██╗  ██╗███████╗
╚══██╔══╝██╔══██╗██║██╔════╝██║   ██║██╔══██╗   ██╔════╝╚██╗██╔╝██╔════╝
   ██║   ██████╔╝██║█████╗  ██║   ██║██████╔╝   █████╗   ╚███╔╝ █████╗  
   ██║   ██╔══██╗██║██╔══╝  ██║   ██║██╔══██╗   ██╔══╝   ██╔██╗ ██╔══╝  
   ██║   ██║  ██║██║███████╗╚██████╔╝██║  ██║██╗███████╗██╔╝ ██╗███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
```

# Instructions :

Ce "logiciel" permet le tri de votre liste, vous pouvez également télécharger une version portable/executable par simple clic ici : https://sourceforge.net/projects/trieur/files/

Vous pouvez créer vous meme l'executable depuis le fichier python, il vous suffira d'installer pyinstaller et python pour créer un executable, voici la marche à suivre:

- [ ] Téléchargez python 3.11.1 depuis ce lien : https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe

- [ ] Ouvrez votre CMD en administrateur et entrez la commande suivante ;

```
pip install pyinstaller
```

Une fois l'installation faites, vous n'avez plus qu'à taper dans votre cmd (en remplacant par vos paths) : 

```
pyinstaller --onefile --icon="...\tireur.ico" --add-data "...\Beta 7\*;ico" --add-data "...\html\*;html" --add-data "...\css\*;css"--noconsole test.py
```

Explications :

--onefile : crée un exécutable unique qui inclut toutes les dépendances.

--icon=icone.ico : spécifie l'icône à utiliser pour l'exécutable (remplacez icone.ico par le chemin de votre fichier d'icône).

--add-data "chemin\vers\fichier\*;nom_du_dossier" : ajoute des fichiers externes nécessaires au programme. Le chemin vers le fichier et le nom du dossier dans lequel le fichier sera extrait doivent être séparés par un point-virgule (;). Vous pouvez ajouter plusieurs fichiers en les séparant par des points-virgules, ou tout les fichiers du dossier concerné en ajoutant \* à la fin.

script.py : spécifie le nom de votre script Python.

--noconsole : masque la console lors de l'exécution de l'exécutable.

Assurez-vous de remplacer les parties en italique par les noms de vos fichiers et dossiers. Notez également que le chemin doit être spécifié en fonction du système d'exploitation sur lequel vous travaillez.

Après avoir exécuté cette commande, vous devriez avoir un exécutable unique qui inclut toutes les dépendances, des fichiers externes et une icône personnalisée, et qui ne montre pas la console lors de l'exécution.
