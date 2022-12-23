import hashlib

import employee as employee
from PyQt5.QtWidgets import QWidget

import main
from Ui.ui_download import Ui_Download_window
from Ui.ui_registration import Ui_Registration

import psycopg2
from PyQt5.QtWidgets import QMainWindow
from psycopg2 import sql
import config
import employee
# from employee import current_user, employees, user_card, Employee


class DownloadWindow(QMainWindow):
	def __init__(self, parent=None):
		super(DownloadWindow, self).__init__(parent)
		self.setWindowTitle("Download")
		self.ui = Ui_Download_window()
		self.ui.setupUi(self)
		Ui_download_window.ui_download_func(self)
		self.parent = parent

	def all_tasks(self):
		try:
			connection = psycopg2.connect(
				host=config.host,
				user=employee.current_user.login,
				password=employee.current_user.password,
				database=config.db_name
			)
			connection.autocommit = True
			with connection.cursor() as cursor:
				try:
					cursor.execute(
						f'COPY (SELECT json_agg(row_to_json(service_order)) :: text FROM service_order) to \'C:\DB\ended_tasks_report.json\'')
					tasks_report = cursor.fetchall()

				except Exception as _ex:
					print("[INFO] Error. tasks report error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)

	def task_by_employee(self):
		try:
			connection = psycopg2.connect(
				host=config.host,
				user=employee.current_user.login,
				password=employee.current_user.password,
				database=config.db_name
			)
			connection.autocommit = True
			with connection.cursor() as cursor:
				try:
					cursor.execute(
						f'COPY (SELECT json_agg(row_to_json(service_order)) :: text FROM service_order WHERE executor_employee_id = \'{self.ui.task_id_text.text()}\') to \'C:\DB\employees_report.json\'')
					employees_report = cursor.fetchall()

				except Exception as _ex:
					print("[INFO] Error. employees report error. Reason: ", _ex)

		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)


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
		idu = 1
		try:
			# connect to exist database
			connection = psycopg2.connect(
				host=config.host,
				user=employee.current_user.login,
				password=employee.current_user.password,
				database=config.db_name
			)
			connection.autocommit = True
			with connection.cursor() as cursor:
				try:
					query = sql.SQL("SELECT max(employee_id) from employee")
					cursor.execute(query)
					maxid = cursor.fetchall()
					for row in maxid:
						idu += row[0]
						print(row[0])
				except Exception as _ex:
					print("[INFO] Error. clients view error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. clients view error. Reason: ", _ex)
		employe_ = employee.Employee(idu, role_,
									 self.ui.lineEdit_f_2.text() + " " + self.ui.lineEdit_f_3.text() + " " + self.ui.lineEdit_f_4.text(),
									 self.ui.lineEdit_f_6.text(), self.ui.Service.text())

		employee.employees.append(employee)

		employee_card = employee.user_card()

		employee_card.setFixedHeight(144)
		employee_card.id = employe_.id
		employee_card.name = (
				self.ui.lineEdit_f_2.text() + " " + self.ui.lineEdit_f_3.text() + " " + self.ui.lineEdit_f_4.text())
		employee_card.email = self.ui.lineEdit_f_6.text()

		employee_card.role = employe_.role
		employee_card.service = employe_.service_id
		employee_card.set()

		cards.append(employee_card)

		main.MainWindow.AddTVert(self.parent, employee_card)

		try:
			connection = psycopg2.connect(
				host=config.host,
				user=employee.current_user.login,
				password=employee.current_user.password,
				database=config.db_name
			)
			connection.autocommit = True

			with connection.cursor() as cursor:
				try:
					cursor.execute(
						f'CALL add_employee(\'{employe_.role}\',\'{self.ui.lineEdit_f_2.text()}\',\'{self.ui.lineEdit_f_3.text()}\','
						f'\'{self.ui.lineEdit_f_4.text()}\', \'{employe_.email}\',\'{self.ui.lineEditx.text()}\', \'{hashlib.sha1(self.ui.lineEdit_f.text().encode()).hexdigest()}\', {employe_.service_id})')
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
		self.ui.lineEdit_f_6.setText("")
		self.ui.lineEditx.setText("")
		self.close()


class Ui_Registration_functions(RegistrationWindow):
	def ui_registration_func(self):
		self.ui.reggg.clicked.connect(self.addUser)

cards = []