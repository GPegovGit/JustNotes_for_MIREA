import datetime
from PyQt5 import QtCore
import PySide6
import psycopg2
from PyQt5.QtWidgets import QWidget, QMainWindow
from PySide6.QtCore import Slot, Signal

import config
import hashlib
import json

import main
from changeTask import *
from main import *
from ui_task_card import ui_task
from Ui_company import Ui_clientcard
from Ui_employee import Ui_usercard
from add_client import Ui_add_client
from add_task import Ui_add_task
from company_filters import Ui_CLients_filters
from employee_filters import Ui_Employee_filters
from tasks_filrers import Ui_tasks_filters
from ui_download import Ui_Download_window
from ui_registration import Ui_Registration
from widget_classes import *


class change(QMainWindow, Ui_change_task):
	def __init__(self, parent=None):
		super(change, self).__init__(parent)
		self.setupUi(self)
		self.parent = parent
		Ui_Change_Task_functions.ui_change_func(self)
		self.Contract_id.setText(str(self.parent.Priority))
		self.Task_id.setText(str(self.parent.executor_id))
		self.Priority.setText(str(self.parent.status))
		self.dateTimeEdit.setDate(tasks[self.parent.id - 1].deadline)
		if current_user.id != tasks[self.parent.number].executor_id and current_user.id != tasks[
			self.parent.number].author_id and not current_user.login == "postgres": self.dateTimeEdit.hide(), self.Priority.hide()
		if current_user.role == "employee": self.Task_id.hide()

	def set(self):
		self.parent.Priority = self.Contract_id.text()
		self.parent.executor_id = self.Task_id.text()
		self.parent.status = self.Priority.text()
		self.parent.deadline = self.dateTimeEdit.text()

		self.parent.Priority_number.setPlainText(str(self.parent.Priority))
		self.parent.Executor_number.setPlainText(str(self.parent.executor_id))
		self.parent.Deadline.setPlainText(str(self.parent.deadline))
		self.parent.Task_Status.setPlainText(self.parent.status)

		tasks[self.parent.id - 1].deadline = self.dateTimeEdit.date()
		tasks[self.parent.id - 1].executor_id = int(self.parent.executor_id)
		tasks[self.parent.id - 1].Priority = int(self.parent.Priority)
		tasks[self.parent.id - 1].status = str(self.parent.status)

		if (self.parent.status == "Finished" or self.parent.status == "finished"):
			self.parent.Change_task.hide()

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
						f'UPDATE task SET deadline = \'{self.parent.deadline}\',executor_employee_id = {tasks[self.parent.id - 1].executor_id},priority = {tasks[self.parent.id - 1].Priority}, status = \'{tasks[self.parent.id - 1].status}\' WHERE task_id = {self.parent.id}')
					print('Task updated succesfully')
				except Exception as _ex:
					print("[INFO] Error. New task not added. Reason: ", _ex)

		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)

		self.close()


class Ui_Change_Task_functions(change):
	def ui_change_func(self):
		self.search.clicked.connect(self.set)


class task_card(QMainWindow, ui_task):
	def __init__(self, parent=None):
		super(task_card, self).__init__(parent)
		self.setupUi(self)
		Ui_Task_Card_functions.ui_task_card_f(self)

		self.id = 0
		self.text = ""
		self.Priority = 0
		self.executor_id = 0
		self.deadline = ""
		self.status = ""
		self.number = 0

	def set(self):
		self.Task_text.setPlainText(self.text)
		self.Priority_number.setPlainText(str(self.Priority))
		self.Executor_number.setPlainText(str(self.executor_id))
		self.Task_id.setPlainText(str(self.id))
		self.Deadline.setPlainText(str(self.deadline))
		self.Task_Status.setPlainText(self.status)

		if (self.status == "Finished" or self.status == "finished"):
			self.Change_task.hide()

	def openChange(self):
		self.w7 = change(self)
		self.w7.show()


class Ui_Task_Card_functions(task_card):
	def ui_task_card_f(self):
		self.Change_task.clicked.connect(self.openChange)


class client_card(QMainWindow, Ui_clientcard):
	def __init__(self):
		super(client_card, self).__init__()
		self.setupUi(self)

		self.id = 0
		self.title = ""
		self.city = ""
		self.phone = ""
		self.email = ""
		self.number = 0

	def set(self):
		self.Email_text.setPlainText(str(self.id))
		self.Email_text_2.setPlainText(self.title)
		self.Phone_text.setPlainText(str(self.city))
		self.Name_text.setPlainText(str(self.phone))
		self.Role_text.setPlainText(str(self.email))


class task_filter(QMainWindow):
	def __init__(self, parent=None):
		super(task_filter, self).__init__(parent)
		self.setWindowTitle("Login")
		self.ui = Ui_tasks_filters()
		self.ui.setupUi(self)
		self.parent = parent
		Ui_task_filter_window.ui_tfilter_func(self)

	def filter_tasks(self):
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
					query_str = f'SELECT * FROM task'
					s = 0
					if self.ui.Author_id.text() != "":
						query_str += f' WHERE author_employee_id = {int(self.ui.Author_id.text())}'
						s += 1
					if self.ui.Executor_id.text() != "":
						if s == 0:
							query_str += f' WHERE executor_employee_id = {int(self.ui.Executor_id.text())}'
						else:
							query_str += f' AND executor_employee_id = {int(self.ui.Executor_id.text())}'
						s += 1
					if self.ui.Task_id.text() != "":
						if s == 0:
							query_str += f' WHERE task_id = {int(self.ui.Task_id.text())}'
						else:
							query_str += f' AND task_id = {int(self.ui.Task_id.text())}'
						s += 1
					if self.ui.Priority.text() != "":
						if s == 0:
							query_str += f' WHERE priority = {int(self.ui.Priority.text())}'
						else:
							query_str += f' AND priority = {int(self.ui.Priority.text())}'
						s += 1
					if self.ui.Status.text() != "":
						if s == 0:
							query_str += f' WHERE status = {self.ui.Status.text()}'
						else:
							query_str += f' AND status = {self.ui.Status.text()}'
						s += 1
					if self.ui.Contract_id.text() != "":
						if s == 0:
							query_str += f' WHERE contract_id = {int(self.ui.Contract_id.text())}'
						else:
							query_str += f' AND contract_id = {int(self.ui.Contract_id.text())}'
						s += 1

					ftasks.clear()
					cursor.execute(query_str)
					filtered_tasks = cursor.fetchall()

					print('Filtered tasks:')
					for row in filtered_tasks:
						print("deadline = ", row[0], )
						print("appointment_date = ", row[1])
						print("executor_employee_id = ", row[2])
						print("author_employee_id = ", row[3])
						print("task_id = ", row[4])
						print("task_description = ", row[5])
						print("priority = ", row[6])
						print("status = ", row[7])
						print("contract_id = ", row[8], "\n")
						format = "dd.MM.yyyy"
						tempdate = PyQt5.QtCore.QDate.fromString(row[8], format)
						task = Task(row[2], row[3], tempdate, row[1], row[0], row[6], row[4], row[5])
						ftasks.append(task)

					for i in range(len(tasks_cards)):
						tasks_cards[i].deleteLater()
					tasks_cards.clear()

					for i in range(len(ftasks)):
						tasskCard = task_card()

						tasskCard.setFixedHeight(122)
						tasskCard.text = ftasks[i].text
						tasskCard.id = ftasks[i].id
						tasskCard.deadline = ftasks[i].deadline.toString('yyyy.MM.dd')
						tasskCard.status = ftasks[i].status
						tasskCard.Priority = ftasks[i].Priority
						tasskCard.executor_id = ftasks[i].executor_id
						tasskCard.set()

						tasks_cards.append(tasskCard)
					main.MainWindow.AddTVert(self.parent, tasks_cards[i])

				except Exception as _ex:
					print("[INFO] Error. Task filter error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. Task filter error. Reason: ", _ex)


class Ui_task_filter_window(task_filter):
	def ui_tfilter_func(self):
		self.ui.search.clicked.connect(self.filter_tasks)


class company_filter(QMainWindow):
	def __init__(self, parent=None):
		super(company_filter, self).__init__(parent)
		self.setWindowTitle("Login")
		self.ui = Ui_CLients_filters()
		self.ui.setupUi(self)
		self.parent = parent
		Ui_company_filter_window.ui_cfilter_func(self)

	def filter_client(self):
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
					query_str = f'SELECT * FROM client'
					s = 0
					if self.ui.company_name.text() != "":
						query_str += f' WHERE company_name = \'{self.ui.company_name.text()}\''
						s += 1
					if self.ui.city.text() != "":
						if s == 0:
							query_str += f' WHERE registration_city = \'{self.ui.city.text()}\''
						else:
							query_str += f' AND registration_city = \'{self.ui.city.text()}\''
						s += 1
					if self.ui.email.text() != "":
						if s == 0:
							query_str += f' WHERE email = \'{self.ui.email.text()}\''
						else:
							query_str += f' AND email = \'{self.ui.email.text()}\''
						s += 1
					if self.ui.phone.text() != "":
						if s == 0:
							query_str += f' WHERE phone_number = {int(self.ui.phone.text())}'
						else:
							query_str += f' AND phone_number = {int(self.ui.phone.text())}'
						s += 1

					fclients.clear()
					cursor.execute(query_str)
					filtered_clients = cursor.fetchall()

					print('Filtered tasks:')
					for row in filtered_clients:
						fclient = Client(row[0], row[3], row[1], row[2], row[4])
						fclients.append(fclient)

					for i in range(len(clients_cards)):
						clients_cards[i].deleteLater()
					clients_cards.clear()

					for i in range(len(fclients)):
						clientCard = client_card()

						clientCard.setFixedHeight(122)
						clientCard.id = fclients[i].id
						clientCard.title = fclients[i].title
						clientCard.phone = fclients[i].phone
						clientCard.email = fclients[i].email
						clientCard.city = fclients[i].city
						clientCard.set()

						clients_cards.append(clientCard)

						main.MainWindow.AddTVert(self.parent, clients_cards[i])

				except Exception as _ex:
					print("[INFO] Error. Client filter error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. Client filter error. Reason: ", _ex)


class Ui_company_filter_window(company_filter):
	def ui_cfilter_func(self):
		self.ui.search.clicked.connect(self.filter_client)


class employee_filter(QMainWindow):
	def __init__(self, parent=None):
		super(employee_filter, self).__init__(parent)
		self.setWindowTitle("Login")
		self.ui = Ui_Employee_filters()
		self.ui.setupUi(self)
		self.parent = parent
		Ui_employee_filter_window.ui_efilter_func(self)

	def filter_employee(self):
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
					query_str = f'SELECT * FROM employee'
					s = 0
					if self.ui.fname.text() != "":
						query_str += f' WHERE first_name = \'{self.ui.fname.text()}\''
						s += 1
					if self.ui.sname.text() != "":
						if s == 0:
							query_str += f' WHERE last_name = \'{self.ui.sname.text()}\''
						else:
							query_str += f' AND last_name = \'{self.ui.sname.text()}\''
						s += 1
					if self.ui.pname.text() != "":
						if s == 0:
							query_str += f' WHERE patronymyc = \'{self.ui.pname.text()}\''
						else:
							query_str += f' AND patronymyc = \'{self.ui.pname.text()}\''
						s += 1
					if self.ui.phone.text() != "":
						if s == 0:
							query_str += f' WHERE phone_number = {int(self.ui.phone.text())}'
						else:
							query_str += f' AND phone_number = {int(self.ui.phone.text())}'
						s += 1
					if self.ui.email.text() != "":
						if s == 0:
							query_str += f' WHERE email = \'{self.ui.email.text()}\''
						else:
							query_str += f' AND email = \'{self.ui.email.text()}\''
						s += 1
					if self.ui.role.text() != "":
						if s == 0:
							query_str += f' WHERE job_title = \'{self.ui.role.text()}\''
						else:
							query_str += f' AND job_title = \'{self.ui.role.text()}\''
						s += 1

					femployees.clear()
					cursor.execute(query_str)
					filtered_employees = cursor.fetchall()

					print('Filtered employees:')
					for row in filtered_employees:
						print("job_title = ", row[0], )
						print("first_name = ", row[1])
						print("last_name = ", row[2])
						print("patronymyc = ", row[3])
						print("phone_number = ", row[4])
						print("email = ", row[5])
						print("employee_id = ", row[6])
						print("username = ", row[7])
						print("password = ", row[8], "\n")

						employee = Employee(row[6], row[0], row[1] + " " + row[2] + " " + row[3], row[4], row[5])
						femployees.append(employee)

						for i in range(len(employees_cards)):
							employees_cards[i].deleteLater()
						employees_cards.clear()

						for i in range(len(femployees)):
							employee_card = user_card()

							employee_card.setFixedHeight(122)
							employee_card.id = femployees[i].id
							employee_card.name = femployees[i].name
							employee_card.phone = femployees[i].phone
							employee_card.email = femployees[i].email
							employee_card.role = femployees[i].role
							employee_card.set()

							employees_cards.append(employee_card)

							main.MainWindow.AddTVert(self.parent, employees_cards[i])

				except Exception as _ex:
					print("[INFO] Error. Employee filter error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. Employee filter error. Reason: ", _ex)


class Ui_employee_filter_window(employee_filter):
	def ui_efilter_func(self):
		self.ui.search.clicked.connect(self.filter_employee)


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


class add_task(QMainWindow):
	def __init__(self, parent=None):
		super(add_task, self).__init__(parent)
		self.setWindowTitle("Add_task")
		self.ui = Ui_add_task()
		self.ui.setupUi(self)
		Ui_Add_Task_functions.ui_add_func(self)
		self.parent = parent
		if current_user.role == "employee": self.ui.Executor_id.hide()

	def addTask(self):
		if current_user.role == "employee":
			executor_id = current_user.id
		else:
			executor_id = int(self.ui.Executor_id.text())

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
					cursor.execute(f'SELECT task_id FROM task WHERE task_id = (select max(task_id) from task)')
					contracts = cursor.fetchall()
					idt = 1
					for row in contracts:
						idt += row[0]
				except Exception as _ex:
					print("[INFO] Error. clients view error. Reason: ", _ex)
					return
		except Exception as _ex:
			print("[INFO] Error. clients view error. Reason: ", _ex)

		task = Task(idt, str(self.ui.Task_id.text()), self.ui.dateTimeEdit.date(), current_user.id, executor_id,
					int(self.ui.Contract_id.text()), int(self.ui.Priority.text()), str("Active"))

		tasks.append(task)

		taskCard = task_card()
		taskCard.setFixedHeight(122)
		taskCard.number = len(tasks) - 1
		taskCard.text = task.text
		taskCard.id = task.id
		taskCard.deadline = self.ui.dateTimeEdit.text()
		taskCard.status = task.status
		taskCard.Priority = task.Priority
		taskCard.executor_id = task.executor_id
		taskCard.set()

		tasks_cards.append(taskCard)

		main.MainWindow.AddTVert(self.parent, taskCard)

		###добавить в бд

		currenttime = (QtCore.QDate.currentDate().toString('dd.MM.yyyy'))

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
						f'INSERT INTO task (deadline, appointent_date, executor_employee_id, author_employee_id, task_description, priority, status, contract_id) VALUES (\'{(taskCard.deadline)}\', \'{currenttime}\', {task.executor_id}, {task.author_id}, \'{task.text}\', {task.Priority}, \'{task.status}\', \'{task.contract_id}\')')
					print('New task added succesfully')
				except Exception as _ex:
					print("[INFO] Error. New task not added. Reason: ", _ex)
					return
		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)
		finally:
			# if connection:
			# 	# cursor.close()
			# connection.close()
			print("[INFO] PostgreSQL connection closed")

		self.close()


class Ui_Add_Task_functions(add_task):
	def ui_add_func(self):
		self.ui.search.clicked.connect(self.addTask)


class add_client(QMainWindow):
	def __init__(self, parent=None):
		super(add_client, self).__init__(parent)
		self.setWindowTitle("Add_client")
		self.ui = Ui_add_client()
		self.ui.setupUi(self)
		Ui_Add_Client_functions.ui_add_func(self)
		self.parent = parent

	def addClient(self):
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
						f'SELECT client_id FROM client WHERE client_id = (select max(client-id) from client)')
					contracts = cursor.fetchall()
					idc = 1
					for row in contracts:
						idc += row[0]
				except Exception as _ex:
					print("[INFO] Error. clients view error. Reason: ", _ex)
					return
		except Exception as _ex:
			print("[INFO] Error. clients view error. Reason: ", _ex)

		client = Client(idc, self.ui.Executor_id.text(), int(self.ui.Task_id.text()), self.ui.Priority.text(),
						self.ui.Status.text())
		clients.append(client)

		clientCard = client_card()

		clientCard.setFixedHeight(122)
		clientCard.id = client.id
		clientCard.number = len(client) - 1
		clientCard.title = self.ui.Executor_id.text()
		clientCard.phone = self.ui.Task_id.text()
		clientCard.email = self.ui.Priority.text()
		clientCard.city = self.ui.Status.text()
		clientCard.set()

		clients_cards.append(clientCard)

		self.ui.Executor_id.setText("")
		self.ui.Task_id.setText("")
		self.ui.Priority.setText("")
		self.ui.Status.setText("")

		main.MainWindow.AddTVert(self.parent, clientCard)

		###добавить в бд

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
						f'INSERT INTO client (phone_number, email, company_name, registration_city) VALUES ({client.phone}, \'{client.email}\', \'{client.title}\', \'{client.city}\')')
					print('New client added succesfully')
				except Exception as _ex:
					print("[INFO] Error. New client not added. Reason: ", _ex)

		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)
		finally:
			print("[INFO] PostgreSQL connection closed")

		self.close()


class Ui_Add_Client_functions(add_client):
	def ui_add_func(self):
		self.ui.search.clicked.connect(self.addClient)


class user_card(QMainWindow, Ui_usercard):
	def __init__(self):
		super(user_card, self).__init__()
		self.setupUi(self)

		self.id = 0
		self.name = ""
		self.email = ""
		self.phone = ""
		self.role = ""
		self.number = 0

	def set(self):
		self.id_text.setPlainText(str(self.id))
		self.email_text.setPlainText(str(self.email))
		self.role_text.setPlainText(str(self.role))
		self.phone_text.setPlainText(str(self.phone))
		self.Name_text.setPlainText(str(self.name))


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
						f'CALL add_employee(\'{employee.role}\',\'{self.ui.lineEdit_f_2.text()}\',\'{self.ui.lineEdit_f_3.text()}\',\'{self.ui.lineEdit_f_4.text()}\', {employee.phone},\'{employee.email}\',\'{self.ui.lineEditx.text()}\', \'{hashlib.sha1(self.ui.lineEdit_f.text().encode()).hexdigest()}\')')
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
