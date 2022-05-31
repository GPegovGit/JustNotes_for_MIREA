
from firebase import *

from main import *
from main import MainWindow
from ui_main import *


class UIFunctions(MainWindow):

    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # MINIMIZE
        self.line_button.clicked.connect(lambda: self.showMinimized())

        self.Close_button.clicked.connect(lambda: self.fullClose())
        self.Settings_button.clicked.connect(lambda: self.show_login())
        self.Close_button.clicked.connect(db.close)

        self.AddCollection.clicked.connect(
             lambda: self.addNote(0)
        )

        self.Callendar_button.clicked.connect(lambda: self.addNote(1))





