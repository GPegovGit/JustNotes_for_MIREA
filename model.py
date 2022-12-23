import PyQt5
import psycopg2
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from psycopg2 import sql

import config
import main
from Ui.Ui_add_model import Ui_add_model
from Ui.add_service import Ui_add_service
from Ui.service import Ui_Service_form
from Ui.ui_add_car import Ui_add_car
from Ui.ui_add_car_brand import Ui_add_car_brand
from Ui.ui_car import Ui_Car_widget
from Ui.ui_car_brand import Ui_Car_Brand_widget
from Ui.ui_model_data import Ui_Model_widget
from employee import current_user
from noteWidget import cards


class Model:
	model_name = None
	model_year = None
	brand_id = None
	model_id = None

	def __init__(self, model_name: str, model_year: int, brand_id: int, model_id: int):
		self.model_name = model_name
		self.model_year = model_year
		self.brand_id = brand_id
		self.model_id = model_id

models = []
fmodels = []


class model_card(QMainWindow, Ui_Model_widget):
	def __init__(self, parent=None):
		super(model_card, self).__init__(parent)
		self.setupUi(self)

		self.model_name = None
		self.model_year = None
		self.brand_id = None
		self.model_id = None

	def set(self):
		self.Model_name.setPlainText(str(self.model_name))
		self.Year.setPlainText(str(self.model_year))
		self.BrandID.setPlainText(str(self.brand_id))
		self.ID.setPlainText(str(self.model_id))



class add_model(QMainWindow):
	def __init__(self, parent=None):
		super(add_model, self).__init__(parent)
		self.setWindowTitle("add_car_brand")
		self.ui = Ui_add_model()
		self.ui.setupUi(self)
		Ui_Add_Model_brand_functions.ui_add_func(self)
		self.parent = parent

	def addModel(self):

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
					query = sql.SQL("SELECT max(car_model_id) from model_data")
					cursor.execute(query)
					maxid = cursor.fetchall()
					for row in maxid:
						idt += row[0]
				except Exception as _ex:
					print("[INFO] Error. clients view error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. clients view error. Reason: ", _ex)

		model = Model(self.ui.Name.text(), self.ui.Year.text(), self.ui.Brand_id.text(), str(idt))

		models.append(model)

		carCard = model_card()
		carCard.setFixedHeight(122)
		carCard.brand_id = model.brand_id
		carCard.model_id = model.model_id
		carCard.model_name = model.model_name
		carCard.model_year = model.model_year
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
					s3 = sql.Literal(carCard.model_name)
					s4 = sql.Literal(carCard.model_year)

					query = sql.SQL(
						"INSERT INTO model_data(model_name, model_year, brand_id) VALUES ({})").format(
						sql.SQL(', ').join([s3, s4, s1]))
					cursor.execute(query)

				except Exception as _ex:
					print("[INFO] Error. New task not added. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error while working with PostgreSQL", _ex)
			self.close()
		self.close()


class Ui_Add_Model_brand_functions(add_model):
	def ui_add_func(self):
		self.ui.search.clicked.connect(self.addModel)
