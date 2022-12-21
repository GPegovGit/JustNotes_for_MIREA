from PyQt5.QtWidgets import QWidget, QMainWindow

from Ui.ui_download import Ui_Download_window
from Ui.ui_registration import Ui_Registration
from employee import Employee, employees, user_card, employees_cards
from main import *


class DownloadWindow(QWidget):
	def __init__(self):
		super(DownloadWindow, self).__init__()
		self.setWindowTitle("Download")
		self.ui = Ui_Download_window()
		self.ui.setupUi(self)
		Ui_download_window.ui_download_func(self)

	def all_tasks(self):
		try:
			connection = psycopg2.connect(
				host=config.host,
				user=current_user.login,
				password=current_user.password,
				database=config.db_name
			)
			connection.autocommit = True
			with connection.cursor() as cursor:
				try:
					cursor.execute(
						f'COPY (SELECT json_agg(row_to_json(task)) :: text FROM task) to \'C:\DB\ended_tasks_report.json\'')
					tasks_report = cursor.fetchall()

				except Exception as _ex:
					print("[INFO] Error. tasks report error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)

	def task_by_employee(self):
		try:
			connection = psycopg2.connect(
				host=config.host,
				user=current_user.login,
				password=current_user.password,
				database=config.db_name
			)
			connection.autocommit = True
			with connection.cursor() as cursor:
				try:
					cursor.execute(
						f'COPY (SELECT json_agg(row_to_json(task)) :: text FROM task WHERE executor_employee_id = \'{self.ui.task_id_text.text()}\') to \'C:\DB\employees_report.json\'')
					employees_report = cursor.fetchall()

				except Exception as _ex:
					print("[INFO] Error. employees report error. Reason: ", _ex)

		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)
		finally:
			# if connection:
			# 	# cursor.close()
			# 	connection.close()
			print("[INFO] PostgreSQL connection closed")


class Ui_download_window(DownloadWindow):
	def ui_download_func(self):
		self.ui.download_all_tasks.clicked.connect(self.all_tasks)
		self.ui.download_tasks_by_employee.clicked.connect(self.task_by_employee)











class RegistrationWindow(QMainWindow):
	def __init__(self, parent=None):
		super(RegistrationWindow, self).__init__(parent)
		self.setWindowTitle("Registration")
		self.ui = Ui_Registration()
		self.ui.setupUi(self)
		Ui_Registration_functions.ui_registration_func(self)
		self.parent = parent

	def addUser(self):
		if self.ui.radioButton.isChecked():
			role_ = "manager"
		else:
			role_ = "employee"
		try:
			# connect to exist database
			connection = psycopg2.connect(
				host=config.host,
				user=current_user.login,
				password=current_user.password,
				database=config.db_name
			)
			connection.autocommit = True
			with connection.cursor() as cursor:
				try:
					cursor.execute(
						f'SELECT employee_id FROM employee WHERE employee_id = (select max(employee_id) from employee)')
					contracts = cursor.fetchall()
					idu = 1
					for row in contracts:
						idu += row[0]
						print(idu)
				except Exception as _ex:
					print("[INFO] Error. clients view error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. clients view error. Reason: ", _ex)
		employee = Employee(idu, role_,
							self.ui.lineEdit_f_2.text() + " " + self.ui.lineEdit_f_3.text() + " " + self.ui.lineEdit_f_4.text(),
							self.ui.lineEdit_f_5.text(), self.ui.lineEdit_f_6.text())
		employees.append(employee)

		employee_card = user_card()

		employee_card.setFixedHeight(144)
		employee_card.number = len(employees) - 1
		employee_card.id = employee.id
		employee_card.name = (
				self.ui.lineEdit_f_2.text() + " " + self.ui.lineEdit_f_3.text() + " " + self.ui.lineEdit_f_4.text())
		employee_card.phone = self.ui.lineEdit_f_5.text()
		employee_card.email = self.ui.lineEdit_f_6.text()

		employee_card.role = employee.role
		employee_card.set()

		employees_cards.append(employee_card)

		main.MainWindow.AddTVert(self.parent, employee_card)

		try:
			connection = psycopg2.connect(
				host=config.host,
				user=current_user.login,
				password=current_user.password,
				database=config.db_name
			)
			connection.autocommit = True

			with connection.cursor() as cursor:
				try:
					cursor.execute(
						f'CALL add_employee(\'{employee.role}\',\'{self.ui.lineEdit_f_2.text()}\',\'{self.ui.lineEdit_f_3.text()}\','
						f'\'{self.ui.lineEdit_f_4.text()}\', {employee.phone},\'{employee.email}\',\'{self.ui.lineEditx.text()}\', \'{hashlib.sha1(self.ui.lineEdit_f.text().encode()).hexdigest()}\')')
					print('New employee added succesfully')
				except Exception as _ex:
					print("[INFO] Error. New employee not added. Reason: ", _ex)

			connection.close()

		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)
		finally:
			print("[INFO] PostgreSQL connection closed")

		self.ui.lineEdit_f.setText("")
		self.ui.lineEdit_f_2.setText("")
		self.ui.lineEdit_f_3.setText("")
		self.ui.lineEdit_f_4.setText("")
		self.ui.lineEdit_f_5.setText("")
		self.ui.lineEdit_f_6.setText("")
		self.ui.lineEditx.setText("")
		self.close()


class Ui_Registration_functions(RegistrationWindow):
	def ui_registration_func(self):
		self.ui.reggg.clicked.connect(self.addUser)
