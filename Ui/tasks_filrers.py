from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class Ui_tasks_filters(object):
    def setupUi(self, tasks_filters):
        if not tasks_filters.objectName():
            tasks_filters.setObjectName(u"tasks_filters")
        tasks_filters.resize(250, 600)
        tasks_filters.setMinimumSize(QtCore.QSize(250, 600))
        tasks_filters.setMaximumSize(QtCore.QSize(250, 600))
        tasks_filters.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.FILTERS = QtWidgets.QTextBrowser(tasks_filters)
        self.FILTERS.setObjectName(u"FILTERS")
        self.FILTERS.setGeometry(QtCore.QRect(-160, 20, 569, 81))
        self.FILTERS.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.gridLayoutWidget = QtWidgets.QWidget(tasks_filters)
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

        self.gridLayout1.addWidget(self.Task_id, 2, 0, 1, 1)

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


        self.Status = QLineEdit(self.gridLayoutWidget)
        self.Status.setObjectName(u"Status")
        self.Status.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.Status, 4, 0, 1, 1)

        self.Executor_id = QLineEdit(self.gridLayoutWidget)
        self.Executor_id.setObjectName(u"Executor_id")
        self.Executor_id.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.Executor_id, 1, 0, 1, 1)

        self.Author_id = QLineEdit(self.gridLayoutWidget)
        self.Author_id.setObjectName(u"Author_id")
        self.Author_id.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.gridLayout1.addWidget(self.Author_id, 0, 0, 1, 1)



        self.retranslateUi(tasks_filters)

        QtCore.QMetaObject.connectSlotsByName(tasks_filters)
    # setupUi

    def retranslateUi(self, tasks_filters):
        tasks_filters.setWindowTitle(QtCore.QCoreApplication.translate("tasks_filters", u"Form", None))
        self.FILTERS.setHtml(QtCore.QCoreApplication.translate("tasks_filters", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:22pt;\">FILTERS</span></p></body></html>", None))
        self.Task_id.setText(QtCore.QCoreApplication.translate("tasks_filters", u"", None))
        self.Task_id.setPlaceholderText("Order id")
        self.search.setText(QtCore.QCoreApplication.translate("tasks_filters", u"SEARCH", None))
        self.Status.setText(QtCore.QCoreApplication.translate("tasks_filters", u"", None))
        self.Status.setPlaceholderText("Status")
        self.Executor_id.setText(QtCore.QCoreApplication.translate("tasks_filters", u"", None))
        self.Executor_id.setPlaceholderText("Executor_id")
        self.Author_id.setText(QtCore.QCoreApplication.translate("tasks_filters", u"", None))
        self.Author_id.setPlaceholderText("Author_id")
    # retranslateUi

