import psycopg2
from PyQt5.QtWidgets import QMainWindow
from psycopg2 import sql

import config
import main
from Ui.Ui_company import Ui_Part_widget
from Ui.add_client import Ui_add_client
from Ui.company_filters import Ui_CLients_filters
from employee import current_user
from noteWidget import cards


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



class client_card(QMainWindow, Ui_Part_widget):
	def __init__(self):
		super(client_card, self).__init__()
		self.setupUi(self)

		self.id = 0
		self.name = ""
		self.phone = ""
		self.email = ""

	def set(self):
		self.Id.setPlainText(str(self.id))
		self.Name.setPlainText(self.name)
		self.Phone.setPlainText(str(self.phone))
		self.Email.setPlainText(str(self.email))


class add_client(QMainWindow):
	def __init__(self, parent=None):
		super(add_client, self).__init__(parent)
		self.setWindowTitle("Add_client")
		self.ui = Ui_add_client()
		self.ui.setupUi(self)
		Ui_Add_Client_functions.ui_add_func(self)
		self.parent = parent

	def addClient(self):
		idc = 1
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

					query = sql.SQL("SELECT max(customer_id) from customer")
					cursor.execute(query)
					maxid = cursor.fetchall()

					for row in maxid:
						idc += row[0]

				except Exception as _ex:
					print("[INFO] Error. clients view error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. clients view error. Reason: ", _ex)

		client = Client(idc, self.ui.fname.text(), self.ui.sname.text(), self.ui.pname.text(),
						self.ui.Task_id.text(), self.ui.Priority.text())

		clients.append(client)

		clientCard = client_card()

		clientCard.setFixedHeight(122)
		clientCard.id = client.id
		clientCard.name = client.fName + " " + client.sName + " " + client.pName
		clientCard.phone = client.phone
		clientCard.email = client.email
		clientCard.set()

		cards.append(clientCard)

		self.ui.fname.setText("")
		self.ui.sname.setText("")
		self.ui.pname.setText("")
		self.ui.Task_id.setText("")
		self.ui.Priority.setText("")

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

					s1 = sql.Literal(client.phone)
					s2 = sql.Literal(client.fName)
					s3 = sql.Literal(client.sName)
					s4 = sql.Literal(client.pName)
					s5 = sql.Literal(client.email)
					query = sql.SQL(
						"INSERT INTO customer(phone_number, firstname, lastname, patronymyc, email) VALUES ({})").format(
						sql.SQL(', ').join([s1, s2, s3, s4, s5]))
					cursor.execute(query)

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
					query_str = f'SELECT * FROM customer'
					s = 0
					if self.ui.fName.text() != "":
						query_str += f' WHERE firstname = \'{self.ui.fName.text()}\''
						s += 1
					if self.ui.sName.text() != "":
						if s == 0:
							query_str += f' WHERE lastname = \'{self.ui.sName.text()}\''
						else:
							query_str += f' AND lastname = \'{self.ui.sName.text()}\''
						s += 1
					if self.ui.pName.text() != "":
						if s == 0:
							query_str += f' WHERE patronymyc = \'{self.ui.pName.text()}\''
						else:
							query_str += f' AND patronymyc = \'{self.ui.pName.text()}\''
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

					for row in filtered_clients:
						fclient = Client(row[5], row[1], row[2], row[3], row[0], row[4])
						fclients.append(fclient)

					for i in range(len(cards)):
						cards[i].deleteLater()
					cards.clear()

					for i in range(len(fclients)):
						clientCard = client_card()

						clientCard.setFixedHeight(122)
						clientCard.id = fclients[i].id
						clientCard.name = fclients[i].fName + " " + fclients[i].sName + " " + fclients[i].pName
						clientCard.phone = fclients[i].phone
						clientCard.email = fclients[i].email
						clientCard.set()

						cards.append(clientCard)

						main.MainWindow.AddTVert(self.parent, cards[i])

				except Exception as _ex:
					print("[INFO] Error. Client filter error. Reason: ", _ex)
		except Exception as _ex:
			print("[INFO] Error. Client filter error. Reason: ", _ex)


class Ui_company_filter_window(company_filter):
	def ui_cfilter_func(self):
		self.ui.search.clicked.connect(self.filter_client)
