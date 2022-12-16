

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class Ui_add_client(object):
    def setupUi(self, add_client):
        if not add_client.objectName():
            add_client.setObjectName(u"add_client")
        add_client.resize(250, 600)
        add_client.setMinimumSize(QtCore.QSize(250, 600))
        add_client.setMaximumSize(QtCore.QSize(250, 600))
        add_client.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.ADD = QtWidgets.QTextBrowser(add_client)
        self.ADD.setObjectName(u"ADD")
        self.ADD.setGeometry(QtCore.QRect(-160, 20, 569, 81))
        self.ADD.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.gridLayoutWidget = QtWidgets.QWidget(add_client)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 110, 211, 441))
        self.gridLayout1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.Task_id = QLineEdit(self.gridLayoutWidget)
        self.Task_id.setObjectName(u"Task_id")
        self.Task_id.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.Task_id, 1, 0, 1, 1)

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

        self.Priority = QLineEdit(self.gridLayoutWidget)
        self.Priority.setObjectName(u"Priority")
        self.Priority.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.Priority, 2, 0, 1, 1)

        self.Status = QLineEdit(self.gridLayoutWidget)
        self.Status.setObjectName(u"Status")
        self.Status.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.Status, 3, 0, 1, 1)

        self.Executor_id = QLineEdit(self.gridLayoutWidget)
        self.Executor_id.setObjectName(u"Executor_id")
        self.Executor_id.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.Executor_id, 0, 0, 1, 1)


        self.retranslateUi(add_client)

        QtCore.QMetaObject.connectSlotsByName(add_client)
    # setupUi

    def retranslateUi(self, add_client):
        add_client.setWindowTitle(QtCore.QCoreApplication.translate("add_client", u"Form", None))
        self.ADD.setHtml(QtCore.QCoreApplication.translate("add_client", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">ADD</span></p></body></html>", None))
        self.Task_id.setText(QtCore.QCoreApplication.translate("add_client", u"", None))
        self.Task_id.setPlaceholderText("Phone")
        self.search.setText(QtCore.QCoreApplication.translate("add_client", u"ADD", None))
        self.Priority.setText(QtCore.QCoreApplication.translate("add_client", u"", None))
        self.Priority.setPlaceholderText("Email")
        self.Status.setText(QtCore.QCoreApplication.translate("add_client", u"", None))
        self.Status.setPlaceholderText("City")
        self.Executor_id.setText(QtCore.QCoreApplication.translate("add_client", u"", None))
        self.Executor_id.setPlaceholderText("Company_Name")
    # retranslateUi

