import sqlite3
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

from ui_main import Ui_MainWindow
from ui_functions import *
from ui_autorization import *
from firebase import *
import sqlite3 as sl
from datetime import datetime
from PySide6.QtCore import Slot
from noteWidget import note_Widget
from database import *
from NoteClass import *


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)

		self.counter_id: int = 0

		# MOVE WINDOW
		def moveWindow(event):
			# IF LEFT CLICK MOVE WINDOW
			if event.buttons() == Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.dragPos)
				self.dragPos = event.globalPos()
				event.accept()

		# SET TITLE BAR
		self.frame_4.mouseMoveEvent = moveWindow

		# ==> SET UI DEFINITIONS
		UIFunctions.uiDefinitions(self)

		status = 0

	def addNote(self, status):
		if user.login is None:
			self.lineEdit.setText("")
			self.lineEdit_2.setText("")
			self.lineEdit_2.setPlaceholderText("You need to log in")
			return

		def delNote():
			delN(notes[num].id)
			delNoteFB(notes[num].id, user.login)
			notes[num].deleteLater()

		match status:
			case 0:
				print(self.counter_id)
				myTitle = self.lineEdit.text()
				myText = self.lineEdit_2.text()
				username = user.login
				nDate = (datetime.date(datetime.now()))
				addN(self.counter_id, myTitle, myText, str(nDate))
				num = self.counter_id
				notes.append(note_Widget())  # self.counter_id, parent=self)
				notes[self.counter_id].setFixedHeight(70)
				notes[self.counter_id].id = self.counter_id
				notes[self.counter_id].title = myTitle
				notes[self.counter_id].text = myText
				notes[self.counter_id].date = nDate
				notes[self.counter_id].checkBox_3.stateChanged.connect(lambda: delNote())
				notes[self.counter_id].set()
				self.verticalLayout.addWidget(notes[self.counter_id])
				addNoteFB(str(nDate), self.counter_id, myText, myTitle, username)
				self.counter_id += 1
				print(self.counter_id)

			case 1:
				checkLog = noteRef.order_by_child('username').equal_to(user.login).get()
				if (len(checkLog)) != len(notes):
					delAN()
					notes.clear()
					self.counter_id = 0
					for key in checkLog:
						addN(self.counter_id, checkLog[key]["title"], checkLog[key]["notes"], checkLog[key]["date"])
						print(self.counter_id)
						num = self.counter_id
						notes.append(note_Widget())  # self.counter_id, parent=self)
						notes[self.counter_id].setFixedHeight(70)
						notes[self.counter_id].id = self.counter_id
						notes[self.counter_id].title = checkLog[key]["title"]
						notes[self.counter_id].text = checkLog[key]["notes"]
						notes[self.counter_id].date = checkLog[key]["date"]
						notes[self.counter_id].checkBox_3.stateChanged.connect(lambda: delNote())
						notes[self.counter_id].set()
						self.verticalLayout.addWidget(notes[self.counter_id])
						self.counter_id += 1

		self.lineEdit_2.setPlaceholderText("")
		self.lineEdit.setText("")
		self.lineEdit_2.setText("")

	# APP EVENTS
	def mousePressEvent(self, event):
		self.dragPos = event.globalPos()

	def show_login(self):
		self.w2 = LoginWindow()
		self.w2.show()

	def fullClose(self):
		self.close()
		self.w2.close()


# def SyncN(self):
# 	keys = []
# 	delAN()
# 	notes.clear()
# 	# try:
# 	# 	for i in range(len(notes) - 1, 0):
# 	# 		print (i)
# 	# 		notes[i].deleteLater()
# 	# except Exception as ex:
# 	# 	print(ex)
# 	# 	return
# 	checkLog = noteRef.order_by_child('username').equal_to(user.login).get()
# 	for key in checkLog:
# 		addN(self.counter_id, checkLog[key]["title"], checkLog[key]["notes"], checkLog[key]["date"])
#
# 		num = self.counter_id
# 		notes.append(note_Widget())  # self.counter_id, parent=self)
# 		notes[self.counter_id].setFixedHeight(70)
# 		notes[self.counter_id].id = self.counter_id
# 		notes[self.counter_id].title = checkLog[key]["title"]
# 		notes[self.counter_id].text = checkLog[key]["notes"]
# 		notes[self.counter_id].date = checkLog[key]["date"]
#
# 		def delNote():
# 			print (notes)
# 			print (num)
# 			delN(notes[num].id)
# 			delNoteFB(notes[num].id, user.login)
# 			notes.remove(notes[num])
# 			print (notes)
#
# 		notes[self.counter_id].checkBox_3.stateChanged.connect(lambda: delNote())
# 		notes[self.counter_id].set()
#
# 		self.verticalLayout.addWidget(notes[self.counter_id])
# 		self.counter_id += 1

# addN(self.counter_id, myTitle, myText, str(nDate))
# num = self.counter_id
# notes.append(note_Widget())  # self.counter_id, parent=self)
# notes[self.counter_id].setFixedHeight(70)
# notes[self.counter_id].id = self.counter_id
# notes[self.counter_id].title = myTitle
# notes[self.counter_id].text = myText
# notes[self.counter_id].date = nDate
#
# def delNote():
# 	delN(notes[num].id)
# 	delNoteFB(notes[num].id, user.login)
# 	notes[num].deleteLater()
#
# notes[self.counter_id].checkBox_3.stateChanged.connect(lambda: delNote())
# notes[self.counter_id].set()
#
# self.verticalLayout.addWidget(notes[self.counter_id])
#
# addNoteFB(str(nDate), self.counter_id, myText, myTitle, username)
# self.counter_id += 1
#
# c.execute("SELECT * from notes")
#
# self.lineEdit.setText("")
# self.lineEdit_2.setText("")


class LoginWindow(QWidget):
	def __init__(self):
		super(LoginWindow, self).__init__()
		self.setWindowTitle("Login")
		self.ui = Ui_Login()
		self.ui.setupUi(self)
		Ui_Login_functions.ui_login_func(self)

	def Reg(self):
		if self.ui.lineEdit.text() == "" or self.ui.lineEdit_2.text() == "":
			self.ui.lineEdit.setPlaceholderText("Enter login")
			self.ui.lineEdit_2.setPlaceholderText("Enter password")
			return
		checkLog = userRef.order_by_child('username').equal_to(self.ui.lineEdit.text()).get()
		if len(checkLog) != 0:
			self.ui.lineEdit.setText("")
			self.ui.lineEdit.setPlaceholderText("Choose another")
			return
		user.login = self.ui.lineEdit.text()
		user.password = self.ui.lineEdit_2.text()
		addUserFB(user.login, user.password)
		delU()
		addU(user.login, user.password)
		delAN()

		for i in range(len(notes)):
			notes[i].deleteLater()

		self.close()

	def Log(self):
		if self.ui.lineEdit.text() == "" or self.ui.lineEdit_2.text() == "":
			self.ui.lineEdit.setPlaceholderText("Enter login")
			self.ui.lineEdit_2.setPlaceholderText("Enter password")
			return
		checkLog = userRef.order_by_child('username').equal_to(self.ui.lineEdit.text()).get()
		for key in checkLog:
			if (checkLog[key]["password"]) != self.ui.lineEdit_2.text():
				self.ui.lineEdit.setText("")
				self.ui.lineEdit_2.setText("")
				self.ui.lineEdit.setPlaceholderText("Wrong data")
				return

		if len(checkLog) == 0:
			self.ui.lineEdit.setText("")
			self.ui.lineEdit_2.setText("")
			self.ui.lineEdit.setPlaceholderText("Wrong data")
			return

		user.login = self.ui.lineEdit.text()
		user.password = self.ui.lineEdit_2.text()
		delU()
		addU(user.login, user.password)
		delAN()

		for i in range(len(notes)):
			notes[i].deleteLater()

		self.close()


class Ui_Login_functions(LoginWindow):
	def ui_login_func(self):
		self.ui.pushButton_2.clicked.connect(self.Reg)
		self.ui.pushButton.clicked.connect(self.Log)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
