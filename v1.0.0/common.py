import os
import re
import sys
import csv
import logging
import configparser

from PIL import Image
from unidecode import unidecode

from PyQt5.QtCore import Qt, QFile, QTextStream, QTimer
from PyQt5.QtGui import QPainter, QColor, QIcon
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QLineEdit, QCheckBox, QVBoxLayout,
                             QWidget, QMessageBox, QTextBrowser, QStyleFactory, QDialog,QSizePolicy, qApp)
from PyQt5.QtWebEngineWidgets import QWebEngineView
