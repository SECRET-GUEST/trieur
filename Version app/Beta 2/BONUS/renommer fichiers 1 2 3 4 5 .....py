import os

# On importe le chemin de notre dossier
path = ' C:/ VOTRE / CHEMIN / ICI '

# On définit le chemin pour tout les fichiers du dossier SI il y en a
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

i = 1 #On commence le compte avec le premier fichier

for file in files:

    old_file = os.path.join(path, file) #On ajoute le chemin du fichier
    extension = os.path.splitext(file)[1] #on stock l'extension dans une variable
    new_file = os.path.join(path, str(i) + extension) #On enregistre le chemin du premier et on lui assigne la valeur de i, puis on ajoute son extension
    os.rename(old_file, new_file) #On renomme l'ancien fichier par le nouveau
    i += 1 # Puis on recommence jusqu'à avoir fait tout les fichiers.
