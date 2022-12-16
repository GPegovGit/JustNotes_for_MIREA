import PyQt5
from PyQt5 import QtCore
import PySide6
from PySide6 import QtCore

class Task:
	id = None
	text = None
	deadline = None
	author_id = None
	executor_id = None
	contract_id = None
	Priority = None
	status = None

	def __init__(self, id: int, text: str, deadline: PyQt5.QtCore.QDate, author_id: int, executor_id: int, contract_id: int, Priority: int, status: str):
		self.id = id
		self.text = text
		self.deadline = deadline
		self.author_id = author_id
		self.executor_id = executor_id
		self.contract_id = contract_id
		self.Priority = Priority
		self.status = status




class Client:
	id = None
	title = None
	phone = None
	email = None
	city = None

	def __init__(self, id: int, title: str, phone: int, email: str, city: str):
		self.id = id
		self.title = title
		self.city = city
		self.phone = phone
		self.email = email

class Employee:
	id = None
	role = None
	name = None
	phone = None
	email = None

	def __init__(self, id: int, role: str, name: str, phone: int, email: str):
		self.id = id
		self.role = role
		self.name = name
		self.phone = phone
		self.email = email


class User:
	login = None
	role = None
	id = 1
	password = None


current_user = User
employee = Employee
client = Client
task = Task

tasks = []
clients = []
employees = []

ftasks = []
fclients = []
femployees = []

tasks_cards = []
clients_cards = []
employees_cards = []





