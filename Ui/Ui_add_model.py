from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class Ui_add_model(object):
    def setupUi(self, add_service):
        if not add_service.objectName():
            add_service.setObjectName(u"add_task")
        add_service.resize(250, 600)
        add_service.setMinimumSize(QtCore.QSize(250, 600))
        add_service.setMaximumSize(QtCore.QSize(250, 600))
        add_service.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.ADD = QtWidgets.QTextBrowser(add_service)
        self.ADD.setObjectName(u"ADD")
        self.ADD.setGeometry(QtCore.QRect(-160, 20, 569, 81))
        self.ADD.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.gridLayoutWidget = QtWidgets.QWidget(add_service)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 110, 211, 441))
        self.gridLayout1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)

        self.Name = QLineEdit(self.gridLayoutWidget)
        self.Name.setObjectName(u"Task_id")
        self.Name.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.Name, 1, 0, 1, 1)

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

        self.gridLayout1.addWidget(self.search, 9, 0, 1, 1)

        self.Year = QLineEdit(self.gridLayoutWidget)
        self.Year.setObjectName(u"Executor_id")
        self.Year.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.Year, 0, 0, 1, 1)


        self.Brand_id = QLineEdit(self.gridLayoutWidget)
        self.Brand_id.setObjectName(u"Priority")
        self.Brand_id.setStyleSheet(u"text-align: center;\n"
                                   "font-family: Myriad Pro;\n"
                                   "color: rgb(123, 115, 27);\n"
                                   "font-size:25px;;\n"
                                   "background-color: rgb(36, 37, 39);\n"
                                   "text-decorations: none;\n"
                                   "border-style:none ;")

        self.gridLayout1.addWidget(self.Brand_id, 7, 0, 1, 1)


        self.retranslateUi(add_service)

        QtCore.QMetaObject.connectSlotsByName(add_service)
    # setupUi

    def retranslateUi(self, add_task):
        add_task.setWindowTitle(QtCore.QCoreApplication.translate("add_task", u"Form", None))
        self.ADD.setHtml(QtCore.QCoreApplication.translate("add_task", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">ADD</span></p></body></html>", None))
        self.Year.setText(QtCore.QCoreApplication.translate("add_task", u"", None))
        self.Year.setPlaceholderText("Model Year")
        self.Name.setText(QtCore.QCoreApplication.translate("add_task", u"", None))
        self.Name.setPlaceholderText("Model Name")
        self.Brand_id.setText(QtCore.QCoreApplication.translate("add_task", u"", None))
        self.Brand_id.setPlaceholderText("Brand Id")
        self.search.setText(QtCore.QCoreApplication.translate("add_task", u"ADD", None))
    # retranslateUi

