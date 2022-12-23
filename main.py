# from database import *
import datetime
import hashlib
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from Ui.ui_autorization import *
from Ui.ui_functions import *
from Ui.ui_main import *
from car import add_car, cars, car_card, Car
from car_brand import add_car_brand, car_brands, car_brand_card, Car_brand
from client import clients, client_card, Client, add_client, company_filter
from employee import employee_filter, employees, user_card, Employee
from model import models, model_card, add_model, Model
from noteWidget import *
from noteWidget import cards
from order import *
from part import parts, add_part, part_card
from service import services, service_card, add_service, Service


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
                    if (current_user.role == "employee"):
                        cursor.execute(
                            f'SELECT * FROM service_order WHERE executor_employee_id =  \'{current_user.id}\'')
                        author_tasks = cursor.fetchall()
                        for row in author_tasks:
                            format = "dd.MM.yyyy"
                            tempdate = PyQt5.QtCore.QDate.fromString(row[10], format)
                            task = Task(row[5], row[3], tempdate, row[7], row[8], row[6], row[0], row[2], row[1],
                                        row[4])
                            tasks.append(task)
                    else:
                        cursor.execute(
                            f'SELECT * FROM service_order')
                        author_tasks = cursor.fetchall()

                        for row in author_tasks:
                            v = str(row[10])
                            d = datetime.datetime.strptime(v, '%Y-%m-%d')
                            dateStr = datetime.date.strftime(d, '%Y.%m.%d')
                            format = "yyyy.MM.dd"
                            tempdate = PyQt5.QtCore.QDate.fromString(dateStr, format)
                            task = Task(row[5], row[3], tempdate, row[7], row[8], row[6], row[0], row[2], row[1],
                                        row[4])
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
                    cursor.execute(f'SELECT * FROM customer_view')
                    contracts = cursor.fetchall()

                    print('Clients seen by the current user:')
                    for row in contracts:
                        client = Client(row[5], row[1], row[2], row[3], row[0], row[4])
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
                        query = sql.SQL("SELECT * FROM employees_view WHERE job_title = \'employee\'")
                        cursor.execute(query)
                        users = cursor.fetchall()
                        for row in users:
                            employee = Employee(row[5], row[3], row[0] + " " + row[1] + " " + row[2], row[4], row[6])
                            employees.append(employee)

                    else:
                        query = sql.SQL("SELECT * FROM employees_view")
                        cursor.execute(query)
                        users = cursor.fetchall()
                        for row in users:
                            employee = Employee(row[5], row[3], row[0] + " " + row[1] + " " + row[2], row[4], row[6])
                            employees.append(employee)

                except Exception as _ex:
                    print("[INFO] Error. employees view error. Reason: ", _ex)
        except Exception as _ex:
            print("[INFO] Error. employees view error. Reason: ", _ex)


    def view_services(self):
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
                    query = sql.SQL("SELECT * FROM service_view")
                    cursor.execute(query)
                    service_ = cursor.fetchall()
                    for row in service_:
                        service = Service(row[4], row[0], row[1], row[2], row[3])
                        services.append(service)
                except Exception as _ex:
                    print("[INFO] Error. Get services error. Reason: ", _ex)
        except Exception as _ex:
            print("[INFO] Error. Get services error. Reason: ", _ex)

    def view_carb_brands(self):
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
                    query = sql.SQL("SELECT * FROM car_brand")
                    cursor.execute(query)
                    service_ = cursor.fetchall()
                    for row in service_:
                        brands = Car_brand(row[0], row[1])
                        car_brands.append(brands)
                except Exception as _ex:
                    print("[INFO] Error. Get services error. Reason: ", _ex)
        except Exception as _ex:
            print("[INFO] Error. Get services error. Reason: ", _ex)

    def view_cars(self):
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
                    query = sql.SQL("SELECT * FROM cars_view")
                    cursor.execute(query)
                    cars_ = cursor.fetchall()
                    for row in cars_:
                        car = Car(row[0], row[1], row[3], row[2])
                        cars.append(car)
                except Exception as _ex:
                    print("[INFO] Error. Get cars error. Reason: ", _ex)
                    return
        except Exception as _ex:
            print("[INFO] Error. Get cars error. Reason: ", _ex)

    def view_models(self):
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
                    query = sql.SQL("SELECT * FROM model_data")
                    cursor.execute(query)
                    cars_ = cursor.fetchall()
                    for row in cars_:
                        model = Model(row[0], row[1], row[3], row[2])
                        models.append(model)
                except Exception as _ex:
                    print("[INFO] Error. Get cars error. Reason: ", _ex)
                    return
        except Exception as _ex:
            print("[INFO] Error. Get cars error. Reason: ", _ex)




    def AddTVert(self, widget):
        self.verticalLayout.addWidget(widget)

    def openDown(self):
        self.w4 = DownloadWindow(self)
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

    def hide_all(self):
        for i in range(len(cards)):
            cards[i].deleteLater()
        cards.clear()

    def del_all(self):
        for i in range(len(cards)):
            cards[i].deleteLater()
        cards.clear()
        clients.clear()
        employees.clear()
        tasks.clear()
        services.clear()
        cars.clear()
        car_brands.clear()
        models.clear()
        parts.clear()

    def show_cars(self):
        if not self.isLogged(): return
        self.status = 5
        self.hide_all()
        for i in range(len(cars)):
            carCard = car_card()
            carCard.setFixedHeight(132)
            carCard.license_plate = cars[i].license_plate
            carCard.car_model_id = cars[i].car_model_id
            carCard.color = cars[i].color
            carCard.estimated_value = cars[i].estimated_value
            carCard.set()

            cards.append(carCard)

            self.verticalLayout.addWidget(cards[i])

    def show_car_brand(self):
        if not self.isLogged(): return
        self.status = 6
        self.hide_all()
        for i in range(len(car_brands)):
            carbrandCard = car_brand_card()
            carbrandCard.setFixedHeight(61)
            carbrandCard.brand_id = car_brands[i].brand_id
            carbrandCard.brand_name = car_brands[i].brand_name
            carbrandCard.set()

            cards.append(carbrandCard)

            self.verticalLayout.addWidget(cards[i])

    def show_model(self):
        if not self.isLogged(): return
        self.status = 7
        self.hide_all()
        for i in range(len(models)):
            carCard = model_card()
            carCard.setFixedHeight(122)
            carCard.brand_id = models[i].brand_id
            carCard.model_id = models[i].model_id
            carCard.model_name = models[i].model_name
            carCard.model_year = models[i].model_year
            carCard.set()

            cards.append(carCard)

            self.verticalLayout.addWidget(cards[i])

    def show_part(self):
        if not self.isLogged(): return
        self.status = 8
        self.hide_all()
        for i in range(len(parts)):
            carCard = part_card()
            carCard.setFixedHeight(122)
            carCard.part_name = parts[i].part_name
            carCard.part_manufacturer_name = parts[i].part_manufacturer_name
            carCard.part_id = parts[i].part_id
            carCard.part_price = parts[i].part_price
            carCard.set()

            cards.append(carCard)

            self.verticalLayout.addWidget(cards[i])

    def show_services(self):
        if not self.isLogged(): return
        self.status = 4
        self.hide_all()
        for i in range(len(services)):
            serviceCard = service_card()
            serviceCard.setFixedHeight(132)
            serviceCard.name = services[i].name
            serviceCard.id = services[i].id
            serviceCard.phone = services[i].phone
            serviceCard.address = services[i].address
            serviceCard.manager = services[i].manager
            serviceCard.set()

            cards.append(serviceCard)

            self.verticalLayout.addWidget(cards[i])

    def show_tasks(self):
        if not self.isLogged(): return
        self.status = 1
        self.hide_all()
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
            tasskCard.plate = tasks[i].license_plate
            tasskCard.service_id = tasks[i].service_id
            tasskCard.part = tasks[i].part_id
            tasskCard.set()

            cards.append(tasskCard)

            self.verticalLayout.addWidget(cards[i])

    def show_clients(self):
        if not self.isLogged(): return
        self.status = 3
        self.hide_all()
        for i in range(len(clients)):
            clientCard = client_card()

            clientCard.setFixedHeight(122)
            clientCard.id = clients[i].id
            clientCard.name = clients[i].fName + " " + clients[i].sName + " " + clients[i].pName
            clientCard.phone = clients[i].phone
            clientCard.email = clients[i].email
            clientCard.set()

            cards.append(clientCard)

            self.verticalLayout.addWidget(cards[i])

    def show_employee(self):
        if not self.isLogged(): return
        self.status = 2
        self.hide_all()

        for i in range(len(employees)):
            employee_card = user_card()

            employee_card.setFixedHeight(122)
            employee_card.id = employees[i].id
            employee_card.name = employees[i].name
            employee_card.email = employees[i].email
            employee_card.role = employees[i].role
            employee_card.service = employees[i].service_id
            employee_card.set()

            cards.append(employee_card)

            self.verticalLayout.addWidget(cards[i])

    def show_add(self):
        if self.status == 1:
            self.w6 = add_task(self)
            self.w6.show()
        elif self.status == 3:
            self.w6 = add_client(self)
            self.w6.show()
        elif self.status == 4:
            self.w6 = add_service(self)
            self.w6.show()
        elif self.status == 5:
            self.w6 = add_car(self)
            self.w6.show()
        elif self.status == 6:
            self.w6 = add_car_brand(self)
            self.w6.show()
        elif self.status == 7:
            self.w6 = add_model(self)
            self.w6.show()
        elif self.status == 8:
            self.w6 = add_part(self)
            self.w6.show()
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
        # проверка на права
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
                            current_user.role = row[0]
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
                        query_str = f'SELECT job_title, employee_id, employee_service_id FROM employee WHERE username = \'{self.ui.lineEdit.text()}\''
                        cursor.execute(query_str)
                        role_and_id = cursor.fetchall()

                        for row in role_and_id:
                            current_user.role = row[0]
                            current_user.id = row[1]
                            current_user.service_id = row[2]

                    except Exception as _ex:
                        print("[INFO] get_job_title_and_id_by_username error. Reason: ", _ex)
                current_user.password = hashlib.sha1(self.ui.lineEdit_2.text().encode()).hexdigest()
            current_user.login = self.ui.lineEdit.text()

            MainWindow.del_all(self.parent)
            MainWindow.view_employees(self.parent)
            MainWindow.view_clients(self.parent)
            MainWindow.view_tasks(self.parent)
            MainWindow.view_services(self.parent)
            MainWindow.view_cars(self.parent)
            MainWindow.view_carb_brands(self.parent)
            MainWindow.view_models(self.parent)
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
