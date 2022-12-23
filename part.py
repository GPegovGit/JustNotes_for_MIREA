import PyQt5
import psycopg2
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from psycopg2 import sql

import config
import main
from Ui import ui_part
from Ui.Ui_add_model import Ui_add_model
from Ui.Ui_add_part import Ui_add_part
from Ui.Ui_company import Ui_Part_widget
from Ui.add_service import Ui_add_service
from Ui.service import Ui_Service_form
from Ui.ui_add_car import Ui_add_car
from Ui.ui_add_car_brand import Ui_add_car_brand
from Ui.ui_car import Ui_Car_widget
from Ui.ui_car_brand import Ui_Car_Brand_widget
from Ui.ui_model_data import Ui_Model_widget
from employee import current_user
from noteWidget import cards


class Part:
	part_name = None
	part_manufacturer_name = None
	part_id = None
	part_price = None

	def __init__(self, part_name: str, part_manufacturer_name: str, part_id: int, part_price: int):
		self.part_name = part_name
		self.part_manufacturer_name = part_manufacturer_name
		self.part_id = part_id
		self.part_price = part_price

parts = []
fparts = []


class part_card(QMainWindow, ui_part.Ui_Part_widget):
	def __init__(self, parent=None):
		super(part_card, self).__init__(parent)
		self.setupUi(self)

		self.part_name = None
		self.part_manufacturer_name = None
		self.part_id = None
		self.part_price = None

	def set(self):
		self.Part_name.setPlainText(str(self.part_name))
		self.Price.setPlainText(str(self.part_price) + "$")
		self.Manufacture.setPlainText(str(self.part_manufacturer_name))
		self.ID.setPlainText(str(self.part_id))



class add_part(QMainWindow):
	def __init__(self, parent=None):
		super(add_part, self).__init__(parent)
		self.setWindowTitle("add_car_brand")
		self.ui = Ui_add_part()
		self.ui.setupUi(self)
		Ui_Add_Part_brand_functions.ui_add_func(self)
		self.parent = parent

	def addMPart(self):
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
					query = sql.SQL("SELECT max(part_id) from part")
					cursor.execute(query)
					maxid = cursor.fetchall()
					for row in maxid:
						idt += row[0]
				except Exception as _ex:
					print("[INFO] Error. clients view error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. clients view error. Reason: ", _ex)

		part = Part(self.ui.Name.text(), self.ui.Manufacturer.text(), str(idt), self.ui.Price.text())

		parts.append(part)
		for i in range(3):
			carCard = part_card()
			carCard.setFixedHeight(122)
			carCard.part_name = part.part_name
			carCard.part_manufacturer_name = part.part_manufacturer_name
			carCard.part_id = idt
			carCard.part_price = part.part_price
			carCard.set()

			cards.append(carCard)

			main.MainWindow.AddTVert(self.parent, carCard)
			idt += 1

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
						f'BEGIN; INSERT INTO part(part_name, part_manufacturer_name, part_price) VALUES (\'{carCard.part_name}\', \'{carCard.part_manufacturer_name}\', {carCard.part_price}); INSERT INTO part(part_name, part_manufacturer_name, part_price) VALUES (\'{carCard.part_name}\', \'{carCard.part_manufacturer_name}\', {carCard.part_price}); INSERT INTO part(part_name, part_manufacturer_name, part_price) VALUES (\'{carCard.part_name}\', \'{carCard.part_manufacturer_name}\', {carCard.part_price}); COMMIT; ')
				except Exception as _ex:
					print("[INFO] Error. New task not added. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)
			self.close()
		self.close()


	def addPart(self):

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
					query = sql.SQL("SELECT max(part_id) from part")
					cursor.execute(query)
					maxid = cursor.fetchall()
					for row in maxid:
						idt += row[0]
				except Exception as _ex:
					print("[INFO] Error. clients view error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. clients view error. Reason: ", _ex)

		part = Part(self.ui.Name.text(), self.ui.Manufacturer.text(), str(idt), self.ui.Price.text())

		parts.append(part)


		carCard = part_card()
		carCard.setFixedHeight(122)
		carCard.part_name = part.part_name
		carCard.part_manufacturer_name = part.part_manufacturer_name
		carCard.part_id = part.part_id
		carCard.part_price = part.part_price
		carCard.set()

		cards.append(carCard)

		main.MainWindow.AddTVert(self.parent, carCard)

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
					s1 = sql.Literal(carCard.part_name)
					s2 = sql.Literal(carCard.part_manufacturer_name)
					s3 = sql.Literal(carCard.part_price)

					query = sql.SQL(
						"INSERT INTO part(part_name, part_manufacturer_name, part_price) VALUES ({})").format(
						sql.SQL(', ').join([s1, s2, s3]))
					cursor.execute(query)

				except Exception as _ex:
					print("[INFO] Error. New task not added. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)
			self.close()
		self.close()


class Ui_Add_Part_brand_functions(add_part):
	def ui_add_func(self):
		self.ui.search.clicked.connect(self.addPart)
		self.ui.search_2.clicked.connect(self.addMPart)
