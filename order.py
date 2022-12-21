import PyQt5
import psycopg2
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

import config
import main
from Ui.add_task import Ui_add_task
from Ui.changeTask import Ui_change_task
from Ui.tasks_filrers import Ui_tasks_filters
from Ui.ui_task_card import ui_task
from employee import current_user


class Task:
	id = None
	text = None
	deadline = None
	author_id = None
	executor_id = None
	contract_id = None
	Priority = None
	status = None
	license_plate = None
	service_id = None
	customer_id = None
	part_id = None

	def __init__(self, id: int, text: str, deadline: PyQt5.QtCore.QDate, author_id: int, executor_id: int, status: str,
				 license_plate: str, service_id: int, customer_id: int, part_id: int):
		self.id = id
		self.text = text
		self.deadline = deadline
		self.author_id = author_id
		self.executor_id = executor_id
		self.status = status
		self.license_plate = license_plate
		self.service_id = service_id
		self.customer_id = customer_id
		self.part_id = part_id


task = Task
tasks = []
ftasks = []
tasks_cards = []


class change(QMainWindow, Ui_change_task):
	def __init__(self, parent=None):
		super(change, self).__init__(parent)
		self.setupUi(self)
		self.parent = parent
		Ui_Change_Task_functions.ui_change_func(self)
		self.Task_id.setText(str(self.parent.executor_id))
		print(parent.number)
		print(tasks)
		self.Priority.setText(self.parent.status)
		self.dateTimeEdit.setDate(tasks[self.parent.number].deadline)
		if current_user.id != tasks[self.parent.number].executor_id and current_user.id != tasks[
			self.parent.number].author_id and not current_user.login == "postgres": self.dateTimeEdit.hide()
		if current_user.role == "employee": self.Task_id.hide()

	def set(self):
		self.parent.executor_id = self.Task_id.text()
		self.parent.status = self.Priority.text()
		self.parent.deadline = self.dateTimeEdit.text()

		self.parent.Executor_number.setPlainText(str(self.parent.executor_id))
		self.parent.Deadline.setPlainText(str(self.parent.deadline))
		self.parent.Task_Status.setPlainText(self.parent.status)

		tasks[self.parent.id - 1].deadline = self.dateTimeEdit.date()
		tasks[self.parent.id - 1].executor_id = int(self.parent.executor_id)
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
						f'UPDATE service_order SET deadline = \'{self.parent.deadline}\',executor_employee_id = {tasks[self.parent.id - 1].executor_id}, status = \'{tasks[self.parent.id - 1].status}\' WHERE order_id = {self.parent.id}')
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
		self.executor_id = 0
		self.deadline = ""
		self.status = ""
		self.number = 0
		self.plate = ""
		self.service_id = 0
		self.part = 0

	def set(self):
		self.Task_text.setPlainText(self.text)
		self.Executor_number.setPlainText(str(self.executor_id))
		self.Task_id.setPlainText(str(self.id))
		self.Deadline.setPlainText(str(self.deadline))
		self.Task_Status.setPlainText(self.status)
		self.Service_id_number.setPlainText(str(self.service_id))
		self.Part_id_number.setPlainText(str(self.part))
		self.License_plate_number.setPlainText(self.plate)

		if (self.status == "Finished" or self.status == "finished"):
			self.Change_task.hide()

	def openChange(self):
		self.w7 = change(self)
		self.w7.show()


class Ui_Task_Card_functions(task_card):
	def ui_task_card_f(self):
		self.Change_task.clicked.connect(self.openChange)


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
					cursor.execute(f'SELECT max(order_id) from service_order')
					contracts = cursor.fetchall()
					idt = 1
					for row in contracts:
						idt += row[0]
				except Exception as _ex:
					print("[INFO] Error. clients view error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. clients view error. Reason: ", _ex)

		task = Task(idt, str(self.ui.Task_id.text()), self.ui.dateTimeEdit.date(), current_user.id, executor_id,
					str("Active"), self.ui.plate.text(), current_user.service_id, self.ui.customer_id.text(),
					self.ui.part_id.text())

		tasks.append(task)

		taskCard = task_card()
		taskCard.setFixedHeight(122)
		taskCard.number = len(tasks) - 1
		taskCard.text = task.text
		taskCard.id = task.id
		taskCard.deadline = self.ui.dateTimeEdit.text()
		taskCard.status = task.status
		taskCard.executor_id = task.executor_id
		taskCard.plate = task.license_plate
		taskCard.service_id = task.service_id
		taskCard.part = task.part_id
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
						f'INSERT INTO service_order (deadline, appointment_date, executor_employee_id, author_employee_id, description, status, license_plate, customer_id, service_id, part_id) VALUES ('
						f'\'{taskCard.deadline}\', \'{currenttime}\', {task.executor_id}, {task.author_id}, \'{task.text}\', \'{task.status}\', \'{taskCard.plate}\', {task.customer_id}, {task.service_id}, {task.part_id})')
					print('New task added succesfully')
				except Exception as _ex:
					print("[INFO] Error. New task not added. Reason: ", _ex)
					return
		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)
			self.close()
		finally:
			# if connection:
			# 	# cursor.close()
			# connection.close()
			print("[INFO] PostgreSQL connection closed")

		self.close()


class Ui_Add_Task_functions(add_task):
	def ui_add_func(self):
		self.ui.search.clicked.connect(self.addTask)


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
					if self.ui.Status.text() != "":
						if s == 0:
							query_str += f' WHERE status = {self.ui.Status.text()}'
						else:
							query_str += f' AND status = {self.ui.Status.text()}'
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
