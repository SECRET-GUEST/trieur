Trieur version beta 5 | Python version 3.11.1 | 🇫🇷 | Optimal avec windows 11 [![Download AKOUN trieur](https://img.shields.io/sourceforge/dt/trieur.svg)](https://sourceforge.net/projects/trieur/files/latest/download)
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

# Contenu et utilisation:


## 1. Bouton de création d'une liste; 

ce dernier permet de sélectionner un dossier. Ceci fait, il prendra en compte tout les fichiers images contenus dans ce dossier ainsi que dans les sous-dossiers, et établira des listes de ces dernières informations dans chaque dossiers, avec une liste principale contenant toute les données de chaque listes additionnées.

ⁿᵒᵗᵉ *Vous pouvez ajouter des données de tailles, telles que 50x40x35cm ou 09x01cm "longueur"x"hauteur"x"profondeur"cm. le formatage doit se faire sans majuscules, sans espaces, et avec un cm a la fin, un programme viendra corriger vos fautes d'innatention mais il n'est pas infaillible, donc essayez d'éviter les erreurs.*


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

Voici un exemple d'utilisation du logiciel pour un dossier contenant des oeuvres numérique ;

![beta2](https://user-images.githubusercontent.com/92639080/216796498-58d8baf0-892f-4680-a1ce-fe1a1936abd2.jpg)

ⁿᵒᵗᵉ *Le logiciel est capable de taiter une liste contenant plusieurs types de dossiers, il triera et rangera les données dans des dossiers/des listes existantes ou non, sans effacer celles qui s'y trouvent déja.*

Il est important de noter que la profondeur est particulière ; 

- [ ] Donner 1 en profondeur pour vos oeuvres produites sur un support tel que le papier, cela annulera la prise en compte de la profondeur dans le calcul de la cote, mais la variable pourra tout de meme etre réutilisée plus tards si besoin.

- [ ] Donner 0 en profondeur aura le meme resultat que si vous donneriez 1, j'ai conservé le 0 pour mieux classer les oeuvres de type numériques.

- [ ] Donner n'importe quelle autre valeur la rendra éffective dans le calcul, arrondissez à l'unité pour éviter les erreurs.

**ʳᵉᵐᵃʳᑫᵘᵉ Le *type* de votre liste NE DEVRA CONTENIR QU'UN SEUL MOT !! Et il ne devra pas contenir de caractère spéciaux tels que "é" ou "+", cela doit rester le plus neutre possible**, c'est tout simplement plus rapide comme ca lors de la prise de notes et de l'écriture du programme.

Les noms de dossiers et des listes seront attribués en fonction du nom du **type** .

