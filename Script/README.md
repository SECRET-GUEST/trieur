[![Download AKOUN trieur](https://img.shields.io/sourceforge/dt/trieur.svg)](https://sourceforge.net/projects/trieur/files/latest/download)
Trieur version 1.0.3 | Python version 3.11.1 | π«π· | For every OS but run better on Windows 

```
ββββββββββββββββ ββββββββββββββ   ββββββββββ    βββββββββββ  βββββββββββ
βββββββββββββββββββββββββββββββ   βββββββββββ   ββββββββββββββββββββββββ
   βββ   βββββββββββββββββ  βββ   βββββββββββ   ββββββ   ββββββ ββββββ  
   βββ   βββββββββββββββββ  βββ   βββββββββββ   ββββββ   ββββββ ββββββ  
   βββ   βββ  ββββββββββββββββββββββββββ  ββββββββββββββββββ βββββββββββ
   βββ   βββ  ββββββββββββββ βββββββ βββ  βββββββββββββββββ  βββββββββββ
```

# Instructions :

Ce "logiciel" permet le tri de votre liste, vous pouvez Γ©galement tΓ©lΓ©charger une version portable/executable par simple clic ici : https://sourceforge.net/projects/trieur/files/

Vous pouvez crΓ©er vous meme l'executable depuis le fichier python, il vous suffira d'installer pyinstaller et python pour crΓ©er un executable, voici la marche Γ  suivre:

- [ ] TΓ©lΓ©chargez python 3.11.1 depuis ce lien : https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe

- [ ] Ouvrez votre CMD en administrateur et entrez la commande suivante ;

```
pip install pyinstaller
```

Une fois l'installation faites, vous avez 2 possibilitΓ©s, mais avant toute chose, vΓ©rifiez qu'il n'y a pas d'espaces dans le nom de vos fichier a compiler, sinon vous aurez des erreurs.

Vous pouvez modifier le fichier ruby ".spec", qui devra se situer Γ  la racine des fichiers/dossiers que vous dΓ©sirez compiler, en rajoutant vos propres chemins.

Puis naviguez avec votre cmd et la commande `cd` la ou se trouve le fichier "AKOUN_trieur_v1.0.0.spec" en utilisant la commande


```
pyinstaller AKOUN_trieur_v1.0.0.spec 
```

Par ailleurs, je vous recommande d'utiliser les paths absolu ( `\\` entre chaque parties du chemin, par exemple `c:\\path\\test.py`)

Ou alors vous pouvez le faire directement dans le cmd (en remplacant par vos paths) : 

```
pyinstaller --onefile --icon="...\tireur.ico" --add-data "...\Beta 7\*;ico" --add-data "...\html\*;html" --add-data "...\css\*;css"--noconsole trieur_v1.0.0.spec.py
```

Explications :

`--onefile` : crΓ©e un exΓ©cutable unique qui inclut toutes les dΓ©pendances.

`--icon=icone.ico` : spΓ©cifie l'icΓ΄ne Γ  utiliser pour l'exΓ©cutable (remplacez icone.ico par le chemin de votre fichier d'icΓ΄ne).

`--add-data` "chemin\\vers\\fichier\*;nom_du_dossier" : ajoute des fichiers externes nΓ©cessaires au programme. Le chemin vers le fichier et le nom du dossier dans lequel le fichier sera extrait doivent Γͺtre sΓ©parΓ©s par un point-virgule (;). Vous pouvez ajouter plusieurs fichiers en les sΓ©parant par des points-virgules, ou tout les fichiers du dossier concernΓ© en ajoutant \* Γ  la fin.

`script.py` : spΓ©cifie le nom de votre script Python.

`--noconsole` : masque la console lors de l'exΓ©cution de l'exΓ©cutable.

Assurez-vous de remplacer les parties en italique par les noms de vos fichiers et dossiers. Notez Γ©galement que le chemin doit Γͺtre spΓ©cifiΓ© en fonction du systΓ¨me d'exploitation sur lequel vous travaillez.

AprΓ¨s avoir exΓ©cutΓ© cette commande, vous devriez avoir un exΓ©cutable unique qui inclut toutes les dΓ©pendances, des fichiers externes et une icΓ΄ne personnalisΓ©e, et qui ne montre pas la console lors de l'exΓ©cution.
