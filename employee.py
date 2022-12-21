import psycopg2
from PyQt5.QtWidgets import QMainWindow

import config
import main
from Ui.Ui_employee import Ui_usercard
from Ui.employee_filters import Ui_Employee_filters


class Employee:
	id = None
	role = None
	name = None
	phone = None
	email = None
	service_id = None

	def __init__(self, id: int, role: str, name: str, phone: int, email: str, service_id: int):
		self.id = id
		self.role = role
		self.name = name
		self.phone = phone
		self.email = email
		self.service_id = service_id

class User:
	login = None
	role = None
	id = 8
	password = None
	service_id = 5


current_user = User
employee = Employee

employees = []
femployees = []
employees_cards = []


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