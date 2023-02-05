import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QLineEdit, QScrollArea, QTextEdit
from PyQt5.QtGui import QIntValidator, QIcon
from PyQt5.QtCore import Qt


class trieur(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setFixedSize(200,300)
        self.setWindowTitle("TRI")
        self.setWindowIcon(QIcon(r"ico\trieur.png"))
        self.setStyleSheet("background-color: #1c1c1c; color: white;")
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint, True)

        self.list = QPushButton("Liste.txt", self)
        f_list = self.list.font()
        f_list.setPointSize(16)
        self.list.setFont(f_list)
        self.list.setStyleSheet("background-color: yellow; color: black;")
        self.list.move(50, 20)
        self.list.clicked.connect(self.openFile)

        self.cote = QLabel(self)
        self.cote.setText("COTE AKOUN :")
        self.cote.setStyleSheet("color: white;") 
        f_cote = self.cote.font()
        f_cote.setPointSize(11)
        self.cote.setFont(f_cote)
        self.cote.move(50, 66)
        
        
        self.cote_akoun = QLineEdit(self)
        f_cote_akoun = self.cote_akoun.font()
        f_cote_akoun.setPointSize(18)
        self.cote_akoun.setFont(f_cote_akoun)
        self.cote_akoun.setStyleSheet("color: white;")  
        self.cote_akoun.setValidator(QIntValidator()) 
        self.cote_akoun.move(50, 100)

        self.launch = QPushButton("Valider", self)
        f_launch = self.launch.font()
        f_launch.setPointSize(18)
        self.launch.setFont(f_launch)
        self.launch.setStyleSheet("background-color: yellow; color: black;")
        self.launch.move(50, 150)
        self.launch.clicked.connect(self.validation)


        self.scroller = QScrollArea(self)
        self.scroller.setWidgetResizable(True)
        self.scroller.setFixedSize(180, 100)
        self.scroller.move(10, 200)
        self.scroller.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        self.message = QTextEdit(self.scroller)
        self.message.setText(
                                                                                                                                "<br>"
            "<center>TUTORIEL :</center> "
                                                                                                                                "<br><br>"
            "Si ce tutoriel n'est pas assez ergonomique pour vous, "
                                                                                                                                "<br>"
            "vous pouuvez toujours copier le texte en utilisant les touches ctrl+A"
                                                                                                                                "<br>"
            "puis coller le texte dans un autre document, un bloc note par exemple,"
                                                                                                                                "<br>"
            "ou tout simplement lire le README.md disponnible la ou vous avez télécharger ce programme"    
                                                                                                                                "<br><br>"
            "Notez que les dossiers / listes seront créées à l'emplacement ou vous lancerez le programme."  
                                                                                                                                "<br>" 
            "Si les dossiers ou des listes au meme nom que le type d'oeuvre existent déja,"
                                                                                                                                "<br>" 
            "les données viendront s'y ajouter sans rien supprimer "                                                                                                                               
                                                                                                                                "<br><br><br>"
            "<center>Utilisation :</center> "
                                                                                                                                "<br><br>"
            "Utilisez le bouton liste.txt pour rechercher votre liste à trier au format.txt "
                                                                                                                                "<br><br>"
            "Le format de votre liste doit ressembler à ca :  "
                                                                                                                                "<br><br>"
            "1 3D 300 200 0 le petit charles   "                                  
                                                                                                                                "<br>"
            "2 numerique 200 50 1 jean-luc "
                                                                                                                                "<br>"
            ". . . " 
                                                                                                                                "<br><br>"
            "soit avec un esapace entre chaques valeurs, <b> sans caractères spéciaux (é, /, ...)</b>: "
                                                                                                                                "<br><br><br>"
            "1.Le numero"
                                                                                                                                "<br><br>"
            "2.Le type d'oeuvre <b>EN UN SEUL MOT</b>"
                                                                                                                                "<br><br>"  
            "3.La longueur"
                                                                                                                                "<br><br>"
            "4.La largeur"
                                                                                                                                "<br><br>"
            "5.La profondeur, <b>mettez 1 ou 0 pour une oeuvre papier ou numérique</b>"
                                                                                                                                "<br><br>"
            "6.Le titre de l'oeuvre"
                                                                                                                                "<br><br><br>"
            "Maintenant, inscrivez votre cote AKOUN. "
                                                                                                                                "<br><br><br>"
            "Enfin, Appuyez sur le bouton valider pour lancer un tri automatique des données"
            )

        self.message.setStyleSheet("color: white;") 
        f_tuto = self.message.font()
        f_tuto.setPointSize(14)
        self.message.setFont(f_tuto)
        self.message.setStyleSheet("background-color : #404040; color : white; border: 1px solid black;")
        self.message.setReadOnly(True)

        self.scroller.setWidget(self.message)



#On finit par afficher la fenetre
        self.show()
        

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "Ouvrir votre liste", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            self.fileName = fileName


    def validation(self):
            self.akoun  = int(self.cote_akoun.text())
        
            if hasattr(self, 'fileName'):
                with open(self.fileName, "r") as f:
                    lines = f.readlines()
                data = {}
                for line in lines:
                    elements = line.split()
                    num = elements[0]
                    data[num] = {}
                    data[num]["type"] = elements[1]
                    data[num]["longueur"] = int(elements[2])
                    data[num]["largeur"] = int(elements[3])
                    data[num]["profondeur"] = int(elements[4])
                    data[num]["nom"] = " ".join(elements[5:])
         
                    if elements[4] in ["0","1"]:            
                        with open(f"{data[num]['type']}/{data[num]['type']}.txt","a") as f: 

                            f.write(f"{num} {data[num]['type']} {data[num]['nom']} {data[num]['longueur']}cm x {data[num]['largeur']}cm  {data[num]['prix']} €  \n") 
                            path = os.path.dirname(os.path.abspath(__file__))
                            os.startfile(path)
                    else :
                        with open(f"{data[num]['type']}/{data[num]['type']}.txt", "a") as f:
                            f.write(f"{num} {data[num]['type']} {data[num]['nom']} {data[num]['longueur']}cm x {data[num]['largeur']}cm x {data[num]['profondeur']}cm {data[num]['prix']} € \n")
                            path = os.path.dirname(os.path.abspath(__file__))
                            os.startfile(path)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = trieur()
    sys.exit(app.exec_())
