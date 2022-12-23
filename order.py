import PyQt5
import psycopg2
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from psycopg2 import sql

import config
import main
from Ui.add_task import Ui_add_task
from Ui.changeTask import Ui_change_task
from Ui.tasks_filrers import Ui_tasks_filters
from Ui.ui_task_card import ui_task
from employee import current_user
from noteWidget import cards


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


class change(QMainWindow, Ui_change_task):
	def __init__(self, parent=None):
		super(change, self).__init__(parent)
		self.setupUi(self)
		self.parent = parent
		Ui_Change_Task_functions.ui_change_func(self)
		self.Task_id.setText(str(self.parent.executor_id))
		print(parent.number)
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

		tasks[self.parent.number].deadline = self.dateTimeEdit.date()
		tasks[self.parent.number].executor_id = int(self.parent.executor_id)
		tasks[self.parent.number].status = str(self.parent.status)

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
						f'UPDATE service_order SET deadline = \'{self.parent.deadline}\',executor_employee_id = {tasks[self.parent.number].executor_id}, status = \'{tasks[self.parent.number].status}\' WHERE order_id = {self.parent.id}')
					# print('Task updated succesfully')
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
		self.number = len(cards)
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
					query = sql.SQL("SELECT max(order_id) from service_order")
					cursor.execute(query)
					maxid = cursor.fetchall()
					idt = 1
					for row in maxid:
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
		taskCard.deadline = task.deadline.toString('yyyy.MM.dd')
		taskCard.status = task.status
		taskCard.executor_id = task.executor_id
		taskCard.plate = task.license_plate
		taskCard.service_id = task.service_id
		taskCard.part = task.part_id
		taskCard.set()

		cards.append(taskCard)

		main.MainWindow.AddTVert(self.parent, taskCard)

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
					s1 = sql.Literal(taskCard.deadline)
					s2 = sql.Literal(currenttime)
					s3 = sql.Literal(task.executor_id)
					s4 = sql.Literal(task.author_id)
					s5 = sql.Literal(task.text)
					s6 = sql.Literal(task.status)
					s7 = sql.Literal(taskCard.plate)
					s8 = sql.Literal(task.customer_id)
					s9 = sql.Literal(task.service_id)
					s10 = sql.Literal(task.part_id)
					query = sql.SQL(
						"INSERT INTO service_order(deadline, appointment_date, executor_employee_id, author_employee_id, description, status, license_plate, customer_id, service_id, part_id) VALUES ({})").format(
						sql.SQL(', ').join([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]))
					cursor.execute(query)

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
					query_str = f'SELECT * FROM service_order'
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
							query_str += f' WHERE order_id = {int(self.ui.Task_id.text())}'
						else:
							query_str += f' AND order_id = {int(self.ui.Task_id.text())}'
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

					for row in filtered_tasks:
						format = "dd.MM.yyyy"
						tempdate = PyQt5.QtCore.QDate.fromString(row[10], format)
						task = Task(row[5], row[3], tempdate, row[7], row[8], row[6], row[0], row[2], row[1], row[4])
						ftasks.append(task)

					for i in range(len(cards)):
						cards[i].deleteLater()
					cards.clear()

					for i in range(len(ftasks)):

						tasskCard = task_card()
						tasskCard.setFixedHeight(122)
						tasskCard.number = len(cards)
						tasskCard.text = ftasks[i].text
						tasskCard.id = ftasks[i].id
						tasskCard.deadline = ftasks[i].deadline.toString('yyyy.MM.dd')
						tasskCard.status = ftasks[i].status
						tasskCard.executor_id = ftasks[i].executor_id
						tasskCard.plate = ftasks[i].license_plate
						tasskCard.service_id = ftasks[i].service_id
						tasskCard.part = ftasks[i].part_id
						tasskCard.set()
						tasskCard.Change_task.hide()

						cards.append(tasskCard)
						main.MainWindow.AddTVert(self.parent, cards[i])

				except Exception as _ex:
					print("[INFO] Error. Task filter error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. Task filter error. Reason: ", _ex)


class Ui_task_filter_window(task_filter):
	def ui_tfilter_func(self):
		self.ui.search.clicked.connect(self.filter_tasks)
