import PyQt5
import psycopg2
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from psycopg2 import sql

import config
import main
from Ui.add_service import Ui_add_service
from Ui.service import Ui_Service_form
from Ui.ui_add_car import Ui_add_car
from Ui.ui_add_car_brand import Ui_add_car_brand
from Ui.ui_car import Ui_Car_widget
from Ui.ui_car_brand import Ui_Car_Brand_widget
from employee import current_user
from noteWidget import cards


class Car_brand:
	brand_name = None
	brand_id = None

	def __init__(self, brand_name: str, brand_id: int):
		self.brand_name = brand_name
		self.brand_id = brand_id


car_brands = []
fcar_brandss = []


class car_brand_card(QMainWindow, Ui_Car_Brand_widget):
	def __init__(self, parent=None):
		super(car_brand_card, self).__init__(parent)
		self.setupUi(self)

		self.brand_name = None
		self.brand_id = None

	def set(self):
		self.Car_brand.setPlainText(str(self.brand_name))
		self.ID.setPlainText(str(self.brand_id))



class add_car_brand(QMainWindow):
	def __init__(self, parent=None):
		super(add_car_brand, self).__init__(parent)
		self.setWindowTitle("add_car_brand")
		self.ui = Ui_add_car_brand()
		self.ui.setupUi(self)
		Ui_Add_Car_brand_functions.ui_add_func(self)
		self.parent = parent

	def addCar(self):

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
					query = sql.SQL("SELECT max(brand_id) from car_brand")
					cursor.execute(query)
					maxid = cursor.fetchall()
					idt = 1
					for row in maxid:
						idt += row[0]
				except Exception as _ex:
					print("[INFO] Error. clients view error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. clients view error. Reason: ", _ex)

		car_brand = Car_brand(self.ui.Brand_Name.text(), str(idt))

		car_brands.append(car_brand)

		carCard = car_brand_card()
		carCard.setFixedHeight(61)
		carCard.brand_id = car_brand.brand_id
		carCard.brand_name = car_brand.brand_name
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
					s1 = sql.Literal(carCard.brand_id)
					s2 = sql.Literal(carCard.brand_name)

					query = sql.SQL(
						"INSERT INTO car_brand(brand_id, brand_name) VALUES ({})").format(
						sql.SQL(', ').join([s1, s2]))
					cursor.execute(query)

				except Exception as _ex:
					print("[INFO] Error. New task not added. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)
			self.close()
		self.close()


class Ui_Add_Car_brand_functions(add_car_brand):
	def ui_add_func(self):
		self.ui.search.clicked.connect(self.addCar)
