from PyQt5.QtWidgets import QWidget, QMainWindow
from PySide6.QtCore import Slot, Signal

from ui_note import Ui_Form


class note_Widget(QMainWindow, Ui_Form):
    def __init__(self):
        super(note_Widget, self).__init__()
        self.setupUi(self)

        self.id = 0
        self.title = ""
        self.text = ""
        self.date = ""

    def set(self):
        self.NoteTitle_7.setPlainText(self.title)
        self.NoteText_7.setPlainText(self.text)
        self.DateText_6.setPlainText(str(self.date))

