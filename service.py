import PyQt5
import psycopg2
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from psycopg2 import sql

import config
import main
from Ui.add_service import Ui_add_service
from Ui.service import Ui_Service_form
from employee import current_user
from noteWidget import cards


class Service:
	id = None
	name = None
	address = None
	phone = None
	manager = None

	def __init__(self, id: int, name: str, address: str, phone: str, manager: str):
		self.id = id
		self.name = name
		self.address = address
		self.phone = phone
		self.manager = manager


service = Service
services = []
fservices = []


class service_card(QMainWindow, Ui_Service_form):
	def __init__(self, parent=None):
		super(service_card, self).__init__(parent)
		self.setupUi(self)

		self.id = 0
		self.name = ""
		self.address = 0
		self.phone = ""
		self.manager = ""

	def set(self):
		self.Name.setPlainText(self.name)
		self.Address.setPlainText(self.address)
		self.ID.setPlainText(str(self.id))
		self.Phone.setPlainText(self.phone)
		self.Manager.setPlainText(self.manager)


class add_service(QMainWindow):
	def __init__(self, parent=None):
		super(add_service, self).__init__(parent)
		self.setWindowTitle("Add_service")
		self.ui = Ui_add_service()
		self.ui.setupUi(self)
		Ui_Add_Service_functions.ui_add_func(self)
		self.parent = parent

	def addService(self):
		idt = 1
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
					query = sql.SQL("SELECT max(service_id) from service")
					cursor.execute(query)
					maxid = cursor.fetchall()
					idt = 1
					for row in maxid:
						idt += row[0]
				except Exception as _ex:
					print("[INFO] Error. clients view error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. clients view error. Reason: ", _ex)

		service = Service(idt, str(self.ui.Name.text()), self.ui.Address.text(), self.ui.Phone.text(), self.ui.Manager.text())

		services.append(service)

		serviceCard = service_card()
		serviceCard.setFixedHeight(132)
		serviceCard.name = service.name
		serviceCard.id = service.id
		serviceCard.phone = service.phone
		serviceCard.address = service.address
		serviceCard.manager = service.manager
		serviceCard.set()

		cards.append(serviceCard)

		main.MainWindow.AddTVert(self.parent, serviceCard)

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
					s1 = sql.Literal(serviceCard.name)
					s2 = sql.Literal(serviceCard.phone)
					s3 = sql.Literal(serviceCard.address)
					s4 = sql.Literal(serviceCard.manager)

					query = sql.SQL(
						"INSERT INTO service(service_name, service_phone_number, service_address, service_manager) VALUES ({})").format(
						sql.SQL(', ').join([s1, s2, s3, s4]))
					cursor.execute(query)

				except Exception as _ex:
					print("[INFO] Error. New task not added. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)
			self.close()
		finally:
			# if connection:
			# 	# cursor.close()
			# connection.close()
			print("[INFO] PostgreSQL connection closed")

		self.close()


class Ui_Add_Service_functions(add_service):
	def ui_add_func(self):
		self.ui.search.clicked.connect(self.addService)
