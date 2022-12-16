

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class Ui_change_task(object):
    def setupUi(self, add_task):
        if not add_task.objectName():
            add_task.setObjectName(u"add_task")
        add_task.resize(250, 600)
        add_task.setMinimumSize(QtCore.QSize(250, 600))
        add_task.setMaximumSize(QtCore.QSize(250, 600))
        add_task.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.ADD = QtWidgets.QTextBrowser(add_task)
        self.ADD.setObjectName(u"ADD")
        self.ADD.setGeometry(QtCore.QRect(-160, 20, 569, 81))
        self.ADD.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.gridLayoutWidget = QtWidgets.QWidget(add_task)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 110, 211, 441))
        self.gridLayout1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.Contract_id = QLineEdit(self.gridLayoutWidget)
        self.Contract_id.setObjectName(u"Contract_id")
        self.Contract_id.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.Contract_id, 4, 0, 1, 1)

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

        self.gridLayout1.addWidget(self.search, 6, 0, 1, 1)

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

        self.dateTimeEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout1.addWidget(self.dateTimeEdit, 5, 0, 1, 1)


        self.retranslateUi(add_task)

        QtCore.QMetaObject.connectSlotsByName(add_task)
    # setupUi

    def retranslateUi(self, add_task):
        add_task.setWindowTitle(QtCore.QCoreApplication.translate("add_task", u"Form", None))
        self.ADD.setHtml(QtCore.QCoreApplication.translate("add_task", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">CHANGE</span></p></body></html>", None))
        self.Contract_id.setText(QtCore.QCoreApplication.translate("add_task", u"", None))
        self.Contract_id.setPlaceholderText("Priority")
        self.Task_id.setText(QtCore.QCoreApplication.translate("add_task", u"", None))
        self.Task_id.setPlaceholderText("Executor id")
        self.search.setText(QtCore.QCoreApplication.translate("add_task", u"CHANGE", None))
        self.Priority.setText(QtCore.QCoreApplication.translate("add_task", u"", None))
        self.Priority.setPlaceholderText("Status")
    # retranslateUi

