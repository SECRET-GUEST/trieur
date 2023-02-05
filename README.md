Trieur version beta 2 | Python version 3.11.1 | 🇫🇷 | Optimal avec windows 10 [![Download AKOUN trieur](https://img.shields.io/sourceforge/dt/trieur.svg)](https://sourceforge.net/projects/trieur/files/latest/download)
```
██╗     ██╗███████╗████████╗███████╗███████╗
██║     ██║██╔════╝╚══██╔══╝██╔════╝██╔════╝
██║     ██║███████╗   ██║   █████╗  ███████╗
██║     ██║╚════██║   ██║   ██╔══╝  ╚════██║
███████╗██║███████║   ██║   ███████╗███████║
╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚══════╝
                                            
```



# Présentation : 

Comme dit dans l'énnoncé, ce programme très spécifique sert aux artistes cotés AKOUN tels que Nathacha , artiste peintre de l'abstraction https://www.artnathacha.com/ , à créer plus rapidement une liste de prix relative à leu cotation pour leurs oeuvres. (ou à des fins éducatives).

ⁿᵒᵗᵉ Un bon anti-malware vous donnera toujours un faux positif pour le fichier .exe puisqu'il n'est pas signé, cependant vous avez le code et j'ai meme écris une notice sur comment compiler le programme vous meme.

[![Download AKOUN trieur](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/trieur/files/latest/download)

## Contenu :

Ce repertoire contient plusieurs éléments, le premier étant un fichier .bat, il suffit de le télécharger et de cliquer dessus pour qu'il fasse une liste de tout ce qui se trouve dans le répertoire ou il a été éxécuté.

Les autres fichiers sont des programmes récupérant les éléments de la liste ligne par lignes, si les informatiions sont correctement écrites dans l'ordre décris plus bas, elles seront acheminées vers de nouveaux dossiers (ou ceux déja existant), venant completer de nouvelles listes, ou en créer de nouvelles.

ⁿᵒᵗᵉ Il est désormais possible de créer des listes directement grace au logiciel.

Pour cela, il suffit de sélectionner le dossier contenant les images, désigner si les oeuvres sont numériques ou non, le programmes supprimera alors TOUT les caractères spéciaux directement dans le noms des images originales, puis établira une liste de ces dernière qui pourra directement etre utilisée pour la suite si les données inscrite sont correcte.

Pour que les données soient correcte, il faut impérativement que le dossier sélectionner soit écrit en un seul mot, par exemple il faudra remplacer "art numérique" par "numérique", sinon vous aurez un message d'erreur.

Voici comment la liste doit etre écrite:


+ Nom : 

liste.txt

+ Contenu :

numero | type d'oeuvre | longueur x largeur x profondeur | nom de l'oeuvre

+ Par exemple :

- [ ] 1 3D 300 200 0 le petit charles

- [ ] 2 numerique 200 50 1 jean-luc

- [ ] 3 pastel 600 400 10 internet vapor wave 404

...

Voici un exemple d'utilisation du logiciel pour un dossier contenant des oeuvres numérique ;

![beta2](https://user-images.githubusercontent.com/92639080/216796498-58d8baf0-892f-4680-a1ce-fe1a1936abd2.jpg)

ⁿᵒᵗᵉ Le logiciel est capable de taiter une liste contenant plusieurs types de dossiers, il triera et rangera les données dans des dossiers/des listes existantes ou non, sans effacer celles qui s'y trouvent déja.

Il est important de noter que la profondeur est particulière ; 

- [ ] Donner 1 en profondeur pour vos oeuvres produites sur un support tel que le papier, cela annulera la prise en compte de la profondeur dans le calcul de la cote, mais la variable pourra tout de meme etre réutilisée plus tards si besoin.

- [ ] Donner 0 en profondeur aura le meme resultat que si vous donneriez 1, j'ai conservé le 0 pour mieux classer les oeuvres de type numériques.

- [ ] Donner n'importe quelle autre valeur la rendra éffective dans le calcul, arrondissez à l'unité pour éviter les erreurs.

**ʳᵉᵐᵃʳᑫᵘᵉ Le *type* de votre liste NE DEVRA CONTENIR QU'UN SEUL MOT !! Et il ne devra pas contenir de caractère spéciaux tels que "é" ou "+", cela doit rester le plus neutre possible**, c'est tout simplement plus rapide comme ca lors de la prise de notes et de l'écriture du programme.

Les noms de dossiers et des listes seront attribués en fonction du nom du **type** .

