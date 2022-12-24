# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrationKfRmoq.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class Ui_Download_window(object):
    def setupUi(self, Download_window):
        if not Download_window.objectName():
            Download_window.setObjectName(u"Download_window")
        Download_window.resize(569, 400)
        Download_window.setMinimumSize(QtCore.QSize(569, 400))
        Download_window.setMaximumSize(QtCore.QSize(569, 700))
        Download_window.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.DOWNLOAD = QtWidgets.QTextBrowser(Download_window)
        self.DOWNLOAD.setObjectName(u"DOWNLOAD")
        self.DOWNLOAD.setGeometry(QtCore.QRect(0, 20, 569, 81))
        self.DOWNLOAD.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.by_employee = QtWidgets.QTextBrowser(Download_window)
        self.by_employee.setObjectName(u"by_employee")
        self.by_employee.setGeometry(QtCore.QRect(318, 110, 251, 71))
        self.by_employee.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(49, 49, 49);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.all_tasks = QtWidgets.QTextBrowser(Download_window)
        self.all_tasks.setObjectName(u"all_tasks")
        self.all_tasks.setGeometry(QtCore.QRect(0, 110, 251, 71))
        self.all_tasks.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(49, 49, 49);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.task_id_text = QLineEdit(Download_window)
        self.task_id_text.setObjectName(u"task_id_text")
        self.task_id_text.setGeometry(QtCore.QRect(348, 210, 191, 30))
        self.task_id_text.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.download_all_tasks = QtWidgets.QPushButton(Download_window)
        self.download_all_tasks.setObjectName(u"download_all_tasks")
        self.download_all_tasks.setEnabled(True)
        self.download_all_tasks.setGeometry(QtCore.QRect(93, 280, 65, 65))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_all_tasks.sizePolicy().hasHeightForWidth())
        self.download_all_tasks.setSizePolicy(sizePolicy)
        self.download_all_tasks.setAutoFillBackground(False)
        self.download_all_tasks.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(123, 115, 27);\n"
"	border-radius: 32px;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addFile(u"C:/Users/User/PycharmProjects/JustNotes_for_MIREA/Source/Download.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_all_tasks.setIcon(icon)
        self.download_all_tasks.setIconSize(QtCore.QSize(45, 45))
        self.download_tasks_by_employee = QtWidgets.QPushButton(Download_window)
        self.download_tasks_by_employee.setObjectName(u"download_tasks_by_employee")
        self.download_tasks_by_employee.setEnabled(True)
        self.download_tasks_by_employee.setGeometry(QtCore.QRect(410, 280, 65, 65))
        sizePolicy.setHeightForWidth(self.download_tasks_by_employee.sizePolicy().hasHeightForWidth())
        self.download_tasks_by_employee.setSizePolicy(sizePolicy)
        self.download_tasks_by_employee.setAutoFillBackground(False)
        self.download_tasks_by_employee.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(123, 115, 27);\n"
"	border-radius: 32px;\n"
"}\n"
"")
        self.download_tasks_by_employee.setIcon(icon)
        self.download_tasks_by_employee.setIconSize(QtCore.QSize(45, 45))

        self.retranslateUi(Download_window)

        QtCore.QMetaObject.connectSlotsByName(Download_window)
    # setupUi

    def retranslateUi(self, Download_window):
        Download_window.setWindowTitle(QtCore.QCoreApplication.translate("Download_window", u"Form", None))
        self.DOWNLOAD.setHtml(QtCore.QCoreApplication.translate("Download_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:22pt;\">DOWNLOAD</span></p></body></html>", None))
        self.by_employee.setHtml(QtCore.QCoreApplication.translate("Download_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">TASKS BY EMPLOYEE</span></p></body></html>", None))
        self.all_tasks.setHtml(QtCore.QCoreApplication.translate("Download_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">ALL COMPLETED TASKS</span></p></body></html>", None))
        self.task_id_text.setText(QtCore.QCoreApplication.translate("Download_window", u"ID", None))
        self.download_all_tasks.setText("")
        self.download_all_tasks.setProperty("border-radius: 50%;", "")
        self.download_tasks_by_employee.setText("")
        self.download_tasks_by_employee.setProperty("border-radius: 50%;", "")
    # retranslateUi

