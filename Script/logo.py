import sys
from PyQt5.QtCore import Qt, QProcess, QTimer, QEventLoop
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen
from main import trieur

class ClickableSplashScreen(QSplashScreen):
    def mousePressEvent(self, event):
        event.accept()


app = QApplication(sys.argv)

# Chemin vers le fichier de logo
logo_path = "ico/Trieur.svg"

# Création du SplashScreen
splash_pix = QPixmap(logo_path)
splash = ClickableSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
splash.setMask(splash_pix.mask())
splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
splash.setAttribute(Qt.WA_QuitOnClose, False)  # Désactive la fermeture par clic sur la fenêtre
splash.show()

# Lancement de votre application en arrière-plan
process = QProcess(trieur)
process.setProcessChannelMode(QProcess.MergedChannels) 
process.start()

# Fermeture du SplashScreen après 3 secondes
QTimer.singleShot(3000, splash.close)

# Attendre que le processus soit terminé
loop = QEventLoop()
process.finished.connect(loop.quit)
loop.exec_()

# Lancement de l'application
sys.exit(app.exec_())
