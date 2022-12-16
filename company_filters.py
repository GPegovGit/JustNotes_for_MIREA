from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class Ui_CLients_filters(object):
    def setupUi(self, CLients_filters):
        if not CLients_filters.objectName():
            CLients_filters.setObjectName(u"CLients_filters")
        CLients_filters.resize(250, 600)
        CLients_filters.setMinimumSize(QtCore.QSize(250, 600))
        CLients_filters.setMaximumSize(QtCore.QSize(250, 600))
        CLients_filters.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.FILTERS = QtWidgets.QTextBrowser(CLients_filters)
        self.FILTERS.setObjectName(u"FILTERS")
        self.FILTERS.setGeometry(QtCore.QRect(-160, 20, 569, 81))
        self.FILTERS.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.gridLayoutWidget = QtWidgets.QWidget(CLients_filters)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 110, 211, 441))
        self.gridLayout1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
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

        self.gridLayout1.addWidget(self.search, 4, 0, 1, 1)

        self.city = QLineEdit(self.gridLayoutWidget)
        self.city.setObjectName(u"city")
        self.city.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.city, 1, 0, 1, 1)

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

        self.company_name = QLineEdit(self.gridLayoutWidget)
        self.company_name.setObjectName(u"company_name")
        self.company_name.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.company_name, 0, 0, 1, 1)

        self.email = QLineEdit(self.gridLayoutWidget)
        self.email.setObjectName(u"email")
        self.email.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.email, 2, 0, 1, 1)


        self.retranslateUi(CLients_filters)

        QtCore.QMetaObject.connectSlotsByName(CLients_filters)
    # setupUi

    def retranslateUi(self, CLients_filters):
        CLients_filters.setWindowTitle(QtCore.QCoreApplication.translate("CLients_filters", u"Form", None))
        self.FILTERS.setHtml(QtCore.QCoreApplication.translate("CLients_filters", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:22pt;\">FILTERS</span></p></body></html>", None))
        self.search.setText(QtCore.QCoreApplication.translate("CLients_filters", u"SEARCH", None))
        self.city.setText(QtCore.QCoreApplication.translate("CLients_filters", u"", None))
        self.city.setPlaceholderText("City")
        self.phone.setText(QtCore.QCoreApplication.translate("CLients_filters", u"", None))
        self.phone.setPlaceholderText("Phone")
        self.company_name.setText(QtCore.QCoreApplication.translate("CLients_filters", u"", None))
        self.company_name.setPlaceholderText("CompanyName")
        self.email.setText(QtCore.QCoreApplication.translate("CLients_filters", u"", None))
        self.email.setPlaceholderText("Email")
    # retranslateUi

