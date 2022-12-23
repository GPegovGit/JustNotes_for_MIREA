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
from Ui.ui_car import Ui_Car_widget
from employee import current_user
from noteWidget import cards


class Car:
	license_plate = None
	color = None
	estimated_value = None
	car_model_id = None

	def __init__(self, license_plate: str, color: str, estimated_value: int, car_model_id: int):
		self.license_plate = license_plate
		self.color = color
		self.estimated_value = estimated_value
		self.car_model_id = car_model_id

cars = []
fcars = []


class car_card(QMainWindow, Ui_Car_widget):
	def __init__(self, parent=None):
		super(car_card, self).__init__(parent)
		self.setupUi(self)

		self.license_plate = ""
		self.color = ""
		self.estimated_value = 0
		self.car_model_id = 0

	def set(self):
		self.Color_number.setPlainText(self.color)
		self.Model_number.setPlainText(str(self.car_model_id))
		self.Plate.setPlainText(self.license_plate)
		self.Value_number.setPlainText(str(self.estimated_value) + "$")


class add_car(QMainWindow):
	def __init__(self, parent=None):
		super(add_car, self).__init__(parent)
		self.setWindowTitle("Add_service")
		self.ui = Ui_add_car()
		self.ui.setupUi(self)
		Ui_Add_Car_functions.ui_add_func(self)
		self.parent = parent

	def addCar(self):
		car = Car(self.ui.License_plate.text(), self.ui.Color.text(), self.ui.Estimated_value.text(), self.ui.Car_model_id.text())

		cars.append(car)

		carCard = car_card()
		carCard.setFixedHeight(122)
		carCard.license_plate = car.license_plate
		carCard.color = car.color
		carCard.estimated_value = car.estimated_value
		carCard.car_model_id = car.car_model_id
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
					s1 = sql.Literal(carCard.license_plate)
					s2 = sql.Literal(carCard.color)
					s3 = sql.Literal(carCard.estimated_value)
					s4 = sql.Literal(carCard.car_model_id)

					query = sql.SQL(
						"INSERT INTO car(license_plate, color, estimated_value, car_model_id) VALUES ({})").format(
						sql.SQL(', ').join([s1, s2, s3, s4]))
					cursor.execute(query)

				except Exception as _ex:
					print("[INFO] Error. New task not added. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)
			self.close()
		self.close()


class Ui_Add_Car_functions(add_car):
	def ui_add_func(self):
		self.ui.search.clicked.connect(self.addCar)
