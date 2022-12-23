


from main import *

from Ui.ui_main import *
from main import MainWindow


class UIFunctions(MainWindow):

    def uiDefinitions(self):

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.line_button.clicked.connect(lambda: self.showMinimized())

        self.Close_button.clicked.connect(lambda: self.fullClose())

        self.Settings_button.clicked.connect(lambda: self.show_login())

        self.Show_clients.clicked.connect(lambda: self.show_clients())

        self.Show_tasks.clicked.connect(lambda: self.show_tasks())

        self.Show_employee.clicked.connect(lambda: self.show_employee())

        self.Download.clicked.connect(lambda: self.openDown())

        self.Filter.clicked.connect(lambda: self.openFilters())

        self.Add_task.clicked.connect(lambda: self.show_add())

        self.Show_service.clicked.connect(lambda: self.show_services())

        self.Show_car.clicked.connect(lambda: self.show_cars())

        self.Show_car_brand.clicked.connect(lambda: self.show_car_brand())

        self.Show_model_data.clicked.connect(lambda: self.show_model())

        self.Show_parts.clicked.connect(lambda: self.show_part())




        #
        # self.Close_button.clicked.connect(db.close)
        #
        # self.AddCollection.clicked.connect(lambda: self.addNote())
        #
        # self.Callendar_button.clicked.connect(lambda: self.addNotes())





