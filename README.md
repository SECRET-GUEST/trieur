Python version 3.11.1 | Optimal avec windows 10
```
██╗     ██╗███████╗████████╗███████╗███████╗
██║     ██║██╔════╝╚══██╔══╝██╔════╝██╔════╝
██║     ██║███████╗   ██║   █████╗  ███████╗
██║     ██║╚════██║   ██║   ██╔══╝  ╚════██║
███████╗██║███████║   ██║   ███████╗███████║
╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚══════╝
                                            
```

![trieur](https://user-images.githubusercontent.com/92639080/213414052-e6f980b0-02f0-4785-af57-be51a2e5984f.png)


# Présentation : 

Comme dit dans l'énnoncé, ce programme très spécifique sert aux artistes cotés AKOUN tels que Nathacha , artiste peintre de l'abstraction https://www.artnathacha.com/ , à créer plus rapidement une liste de prix relative à leu cotation pour leurs oeuvres. (ou à des fins éducatives)

## Contenu :

Ce repertoire contient plusieurs éléments, le premier étant un fichier .bat, il suffit de le télécharger et de cliquer dessus pour qu'il fasse une liste de tout ce qui se trouve dans le répertoire ou il a été éxécuté.

Les autres fichiers sont des programmes récupérant les éléments de la liste ligne par lignes, si les informatiions sont correctement écrites dans l'ordre décris plus bas, elles seront acheminées vers de nouveaux dossiers (ou ceux déja existant), venant completer de nouvelles listes, ou en créer de nouvelles.

Voici comment la liste doit etre écrite:

+ Nom : 

liste.txt

+ Contenu :

numero | type d'oeuvre | longueur x largeur x profondeur | nom de l'oeuvre

+ Par exemple :

- [ ] 1 3D 300 200 0 le petit charles

- [ ] 2 numerique 200 50 1 jean-luc

- [ ] 3 pastel 600 400 10 internet vapor wave 404

- [ ] 4 3D 50 20 52 100% giro

...

Le résultat apparaitra donc comme celui ci ;

![screenshot](https://user-images.githubusercontent.com/92639080/213278592-8f9156e8-7d56-40b8-a6d1-0ffe466edfe2.png)


Il est important de noter que la profondeur est particulière ; 

- [ ] Donner 1 en profondeur pour vos oeuvres produites sur un support tel que le papier, cela annulera la prise en compte de la profondeur dans le calcul de la cote, mais la variable pourra tout de meme etre réutilisée plus tards si besoin.

- [ ] Donner 0 en profondeur aura le meme resultat que si vous donneriez 1, j'ai conservé le 0 pour mieux classer les oeuvres de type numériques.

- [ ] Donner n'importe quelle autre valeur la rendra éffective dans le calcul, arrondissez à l'unité pour éviter les erreurs.

**ʳᵉᵐᵃʳᑫᵘᵉ Le *type* de votre liste NE DEVRA CONTENIR QU'UN SEUL MOT !! Et il ne devra pas contenir de caractère spéciaux tels que "é" ou "+", cela doit rester le plus neutre possible**, c'est tout simplement plus rapide comme ca lors de la prise de notes et de l'écriture du programme.

Les noms de dossiers et des listes seront attribués en fonction du nom du **type** .


## Avenir de l'application 

Peu de changements sont à prévoir, étant un outil hyper spécifique et probablement peu utile, je compte tout de meme créer une application executable pour mac android Iphone et bien entendu windows.

Je rajouterai un moyen de modifier la valeur de la cote par l'interface visuelle, une fenetre un peu plus ergonomique, ainsi qu'un peu de frontend.

Bien entendu ces perspectives d'évolution pourraient changer avec le temps en fonction de mes besoins ou des votres.

