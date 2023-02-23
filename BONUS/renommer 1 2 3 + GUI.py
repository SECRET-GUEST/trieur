
###################################################################################################################################################
# Ce programme est a meme de renommer toute les images d'un dossier choisis, ainsi que toute celles incluses dans les sous dossiers de ce dernier #
###################################################################################################################################################


import os,sys
from PyQt5.QtWidgets import QApplication,QPushButton, QMainWindow, QFileDialog, QVBoxLayout, QWidget, QLabel


class ImageRenamer( QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setWindowTitle("Image Renamer")
        self.setFixedSize(200,100) #La taille Longueur, hauteur
        self.setStyleSheet("background-color: #1c1c1c; color: white;")
        self.folder = ""

#Un boutton pour permettre de renommer les images de tout les dossiers et sous dossiers d'un dossier selectionné
        self.renamer = QPushButton("Renommer images", self)
        f_renamer = self.renamer.font()
        f_renamer.setPointSize(16)
        self.renamer.setFont(f_renamer)
        self.renamer.setStyleSheet("background-color: yellow; color: black;")
        self.renamer.clicked.connect(self.rename)

#Un label pour indiquer le dossier choisis
        self.label = QLabel('Pas de dossier choisi', self)



#On place nos éléments dans une colone verticale, un layout
        layout = QVBoxLayout()

        layout.addSpacing(10) # On espace les éléments dans la grille
        layout.addWidget(self.renamer)
        layout.addSpacing(10) # On espace les éléments dans la grille
        layout.addWidget(self.label)

#On centralise les widgets, les éléments que l'on a créé dans notre grille
        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
#On finit par afficher la fenetre
        self.show()



#Notre fonction pour renommer
    def rename(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        folder = QFileDialog.getExistingDirectory(self, "Select a folder", options=options)

        if folder:
            self.folder = folder
            self.label.setText(self.folder)

        if self.folder == "":
            return

        #On recherche dans TOUT les dossiers et sous-dossiers
        for subdir, dirs, files in os.walk(self.folder):

            counter = 1

            for filename in files:
                extension = os.path.splitext(filename)[1].lower()

                #Si un dossier contient une image possedant une extension contenue dans la liste établie par GPT-3 (merci encore OpenAI)

                if extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".ico", ".tif", ".tiff", ".psd", ".ai", ".webp", ".heic", ".eps", ".raw", ".nef", ".cr2", ".crw", ".orf", ".sr2", ".srw", ".pef", ".dng", ".x3f", ".raf", ".arw", ".rw2", ".mrw", ".mef", ".nrw", ".dcr", ".kdc", ".mos", ".fff", ".3fr", ".erf", ".png", ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", ".mj2", ".hdr", ".exr", ".dpx", ".cin", ".r3d", ".ari", ".mxf", ".gpr", ".cinemadng", ".cr3", ".heif", ".heics", ".heif", ".avif"]:
                    new_name = str(counter) + extension

                    #On rajoute +1 au compteur qui sera également son nom
                    counter += 1
                
                #puis on remplace l'ancien nom par le nouveau
                    old = os.path.join(subdir, filename)
                    new = os.path.join(subdir, new_name)

                    os.rename(old, new)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    renaming = ImageRenamer()
    sys.exit(app.exec_())
