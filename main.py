#from database import *

import hashlib
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from Ui.ui_autorization import *
from Ui.ui_functions import *
from Ui.ui_main import *
from client import clients_cards, clients, client_card, Client, add_client, company_filter
from employee import employee_filter
from noteWidget import *
from order import *



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.counter_id: int = 0

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.frame_4.mouseMoveEvent = moveWindow

        UIFunctions.uiDefinitions(self)

        self.status = 0

    def view_tasks(username: str):
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
                                        f'SELECT * FROM task')
                                author_tasks = cursor.fetchall()

                                print('Tasks by authorship of an employee:')
                                for row in author_tasks:
                                        format = "dd.MM.yyyy"
                                        tempdate = PyQt5.QtCore.QDate.fromString(row[8], format)
                                        task = Task(row[2], row[3], tempdate, row[1], row[0], row[6], row[4], row[5])
                                        tasks.append(task)

                            except Exception as _ex:
                                    print("[INFO] Error. view tasks error. Reason: ", _ex)
        except Exception as _ex:
            print("[INFO] Error. view tasks error. Reason: ", _ex)

    def view_clients(self):
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
                            cursor.execute(f'SELECT * FROM client')
                            contracts = cursor.fetchall()

                            print('Clients seen by the current user:')
                            for row in contracts:
                                    client = Client(row[0], row[3], row[1], row[2], row[4])
                                    clients.append(client)

                    except Exception as _ex:
                            print("[INFO] Error. clients view error. Reason: ", _ex)
        except Exception as _ex:
            print("[INFO] Error. clients view error. Reason: ", _ex)


    def view_employees(self):
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
                        if (current_user.role == 'employee'):
                            cursor.execute(
                                    f'SELECT * FROM employee WHERE job_title = \'employee\'')
                        else:
                            cursor.execute(
                                    f'SELECT * FROM employee')
                            users = cursor.fetchall()

                            for row in users:
                                    employee = Employee(row[6], row[0], row[1] + " " + row[2] + " " + row[3], row[4], row[5])
                                    employees.append(employee)

                    except Exception as _ex:
                            print("[INFO] Error. employees view error. Reason: ", _ex)
        except Exception as _ex:
            print("[INFO] Error. employees view error. Reason: ", _ex)

    def AddTVert(self, widget):
            self.verticalLayout.addWidget(widget)

    def openDown(self):
        self.w4 = DownloadWindow()
        self.w4.show()

    def openFilters(self):
        if self.status == 1:
            self.w5 = task_filter(self)
            self.w5.show()
        elif self.status == 2:
            self.w5 = employee_filter(self)
            self.w5.show()
        elif self.status == 3:
            self.w5 = company_filter(self)
            self.w5.show()


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def show_login(self):
        self.w2 = LoginWindow(self)
        self.w2.show()

    def show_tasks(self):
        if not self.isLogged(): return
        self.status = 1
        for i in range(len(clients_cards)):
            clients_cards[i].deleteLater()
        clients_cards.clear()
        for i in range(len(employees_cards)):
            employees_cards[i].deleteLater()
        employees_cards.clear()
        for i in range(len(tasks)):
            tasskCard = task_card()

            tasskCard.setFixedHeight(122)
            tasskCard.text = tasks[i].text
            tasskCard.id = tasks[i].id
            tasskCard.deadline = tasks[i].deadline.toString('yyyy.MM.dd')
            tasskCard.status = tasks[i].status
            tasskCard.Priority = tasks[i].Priority
            tasskCard.executor_id = tasks[i].executor_id
            tasskCard.number = i
            tasskCard.set()

            tasks_cards.append(tasskCard)

            self.verticalLayout.addWidget(tasks_cards[i])

    def show_clients(self):
        if not self.isLogged(): return
        self.status = 3
        for i in range(len(employees_cards)):
            employees_cards[i].deleteLater()
        employees_cards.clear()
        for i in range(len(tasks_cards)):
            tasks_cards[i].deleteLater()
        tasks_cards.clear()
        for i in range(len(clients)):
            clientCard = client_card()

            clientCard.setFixedHeight(122)
            clientCard.id = clients[i].id
            clientCard.title = clients[i].title
            clientCard.phone = clients[i].phone
            clientCard.email = clients[i].email
            clientCard.city = clients[i].city
            clientCard.number = i
            clientCard.set()

            clients_cards.append(clientCard)

            self.verticalLayout.addWidget(clients_cards[i])

    def show_employee(self):
        if not self.isLogged(): return
        self.status = 2
        for i in range(len(clients_cards)):
            clients_cards[i].deleteLater()
        clients_cards.clear()
        for i in range(len(tasks_cards)):
            tasks_cards[i].deleteLater()
        tasks_cards.clear()

        for i in range(len(employees)):
            employee_card = user_card()

            employee_card.setFixedHeight(122)
            employee_card.id = employees[i].id
            employee_card.name = employees[i].name
            employee_card.phone = employees[i].phone
            employee_card.email = employees[i].email
            employee_card.role = employees[i].role
            employee_card.number = i
            employee_card.set()

            employees_cards.append(employee_card)

            self.verticalLayout.addWidget(employees_cards[i])

    def show_add(self):
        if self.status == 1:
            self.w6 = add_task(self)
            self.w6.show()
        elif self.status == 3:
            self.w6 = add_client(self)
            self.w6.show()


    def refresh(self):
        print("refresh")

    def fullClose(self):
        self.close()
        self.w2.close()
        self.w3.close()
        self.w4.close()
        self.w5.close()

    def isLogged(self):
        if current_user.login is None:
            return False
        return True

class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle("Login")
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        Ui_Login_functions.ui_login_func(self)
        self.parent = parent

    def openReg(self):
        #проверка на права
        if (current_user.login != "postgres"):
            self.ui.lineEdit.setText("")
            self.ui.lineEdit_2.setText("")
            self.ui.lineEdit.setPlaceholderText("No permissions")
            self.ui.lineEdit_2.setPlaceholderText("No permissions")
            return

        self.w3 = RegistrationWindow(self.parent)
        self.close()
        self.w3.show()

    def Log(self):
        if self.ui.lineEdit.text() == "" or self.ui.lineEdit_2.text() == "":
            self.ui.lineEdit.setPlaceholderText("Enter login")
            self.ui.lineEdit_2.setPlaceholderText("Enter password")
            return

        try:
            if (self.ui.lineEdit.text() == "postgres"):
                connection = psycopg2.connect(
                    host=config.host,
                    user=self.ui.lineEdit.text(),
                    password=self.ui.lineEdit_2.text(),
                    database=config.db_name
                )
                connection.autocommit = True
                with connection.cursor() as cursor:
                    try:
                        query_str = f'SELECT job_title, employee_id FROM public.employee WHERE username = \'{self.ui.lineEdit.text()}\''
                        cursor.execute(query_str)
                        role_and_id = cursor.fetchall()

                        for row in role_and_id:
                                print("job_title = ", row[0], )
                                current_user.role = row[0]
                                print("employee_id = ", row[1], "\n")
                                current_user.id = row[1]

                    except Exception as _ex:
                        print("[INFO] get_job_title_and_id_by_username error. Reason: ", _ex)
                current_user.password = self.ui.lineEdit_2.text()
            else:
                connection = psycopg2.connect(
                    host=config.host,
                    user=self.ui.lineEdit.text(),
                    password=hashlib.sha1(self.ui.lineEdit_2.text().encode()).hexdigest(),
                    database=config.db_name
                )
                connection.autocommit = True
                with connection.cursor() as cursor:
                    try:
                        query_str = f'SELECT job_title, employee_id FROM public.employee WHERE username = \'{self.ui.lineEdit.text()}\''
                        cursor.execute(query_str)
                        role_and_id = cursor.fetchall()

                        for row in role_and_id:
                            current_user.role = row[0]
                            current_user.id = row[1]

                    except Exception as _ex:
                        print("[INFO] get_job_title_and_id_by_username error. Reason: ", _ex)
                current_user.password = hashlib.sha1(self.ui.lineEdit_2.text().encode()).hexdigest()
            current_user.login = self.ui.lineEdit.text()

            MainWindow.view_employees(self.parent)
            MainWindow.view_clients(self.parent)
            MainWindow.view_tasks(self.parent)
            connection.close()
            self.close()

        except Exception as _ex:
            self.ui.lineEdit.setText("")
            self.ui.lineEdit_2.setText("")
            self.ui.lineEdit.setPlaceholderText("Wrong data")
            self.ui.lineEdit_2.setPlaceholderText("Wrong data")






class Ui_Login_functions(LoginWindow):
    def ui_login_func(self):
        self.ui.pushButton_2.clicked.connect(self.openReg)
        self.ui.pushButton.clicked.connect(self.Log)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
