import psycopg2
from PyQt5.QtWidgets import QMainWindow

import config
import main
from Ui.Ui_company import Ui_clientcard
from Ui.add_client import Ui_add_client
from Ui.company_filters import Ui_CLients_filters
from employee import current_user


class Client:
	id = None
	name = None
	phone = None
	email = None
	pName = None
	sName = None
	fName = None

	def __init__(self, id: int, fName: str, sName: str, pName: str, phone: int, email: str):
		self.id = id
		self.fName = fName
		self.sName = sName
		self.pName = pName
		self.phone = phone
		self.email = email

client = Client
clients = []
fclients = []
clients_cards = []

class client_card(QMainWindow, Ui_clientcard):
	def __init__(self):
		super(client_card, self).__init__()
		self.setupUi(self)

		self.id = 0
		self.name = ""
		self.phone = ""
		self.email = ""
		self.number = 0

	def set(self):
		self.Email_text.setPlainText(str(self.id))
		self.Email_text_2.setPlainText(self.title)
		self.Phone_text.setPlainText(str(self.city))
		self.Name_text.setPlainText(str(self.phone))
		self.Role_text.setPlainText(str(self.email))

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


