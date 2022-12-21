from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class Ui_Employee_filters(object):
    def setupUi(self, Employee_filters):
        if not Employee_filters.objectName():
            Employee_filters.setObjectName(u"Employee_filters")
        Employee_filters.resize(250, 600)
        Employee_filters.setMinimumSize(QtCore.QSize(250, 600))
        Employee_filters.setMaximumSize(QtCore.QSize(250, 600))
        Employee_filters.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.FILTERS = QtWidgets.QTextBrowser(Employee_filters)
        self.FILTERS.setObjectName(u"FILTERS")
        self.FILTERS.setGeometry(QtCore.QRect(-160, 20, 569, 81))
        self.FILTERS.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.gridLayoutWidget = QtWidgets.QWidget(Employee_filters)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 110, 211, 441))
        self.gridLayout1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.email = QLineEdit(self.gridLayoutWidget)
        self.email.setObjectName(u"email")
        self.email.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.email, 4, 0, 1, 1)

        self.search = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.search.setObjectName(u"search")
        self.search.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"border-style:solid ;\n"
"    border-width: 2px;\n"
"    border-color: rgb(123, 115, 27);\n"
"border-radius: 15px;")

        self.gridLayout1.addWidget(self.search, 6, 0, 1, 1)

        self.sname = QLineEdit(self.gridLayoutWidget)
        self.sname.setObjectName(u"sname")
        self.sname.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.sname, 1, 0, 1, 1)

        self.phone = QLineEdit(self.gridLayoutWidget)
        self.phone.setObjectName(u"phone")
        self.phone.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.phone, 3, 0, 1, 1)

        self.fname = QLineEdit(self.gridLayoutWidget)
        self.fname.setObjectName(u"fname")
        self.fname.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.fname, 0, 0, 1, 1)

        self.pname = QLineEdit(self.gridLayoutWidget)
        self.pname.setObjectName(u"pname")
        self.pname.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.pname, 2, 0, 1, 1)

        self.role = QLineEdit(self.gridLayoutWidget)
        self.role.setObjectName(u"role")
        self.role.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.role, 5, 0, 1, 1)


        self.retranslateUi(Employee_filters)

        QtCore.QMetaObject.connectSlotsByName(Employee_filters)
    # setupUi

    def retranslateUi(self, Employee_filters):
        Employee_filters.setWindowTitle(QtCore.QCoreApplication.translate("Employee_filters", u"Form", None))
        self.FILTERS.setHtml(QtCore.QCoreApplication.translate("Employee_filters", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:22pt;\">FILTERS</span></p></body></html>", None))
        self.email.setText(QtCore.QCoreApplication.translate("Employee_filters", u"", None))
        self.email.setPlaceholderText("Email")
        self.search.setText(QtCore.QCoreApplication.translate("Employee_filters", u"SEARCH", None))
        self.sname.setText(QtCore.QCoreApplication.translate("Employee_filters", u"", None))
        self.sname.setPlaceholderText("Second Name")
        self.phone.setText(QtCore.QCoreApplication.translate("Employee_filters", u"", None))
        self.phone.setPlaceholderText("Phone")
        self.fname.setText(QtCore.QCoreApplication.translate("Employee_filters", u"", None))
        self.fname.setPlaceholderText("First Name")
        self.pname.setText(QtCore.QCoreApplication.translate("Employee_filters", u"", None))
        self.pname.setPlaceholderText("Patronymic")
        self.role.setText(QtCore.QCoreApplication.translate("Employee_filters", u"", None))
        self.role.setPlaceholderText("Role")
    # retranslateUi

