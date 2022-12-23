from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize, QCoreApplication, QMetaObject
from PyQt5.QtWidgets import QLineEdit, QFrame, QTextBrowser, QTextEdit


class Ui_Service_form(object):
    def setupUi(self, Service_form):
        if not Service_form.objectName():
            Service_form.setObjectName(u"Service_form")
        Service_form.resize(1322, 132)
        self.Service_frame = QFrame(Service_form)
        self.Service_frame.setObjectName(u"Service_frame")
        self.Service_frame.setGeometry(QRect(0, 0, 1281, 122))
        self.Service_frame.setMinimumSize(QSize(1240, 122))
        self.Service_frame.setMaximumSize(QSize(1281, 122))
        self.Service_frame.setStyleSheet(u"background-color: rgb(36, 37, 39);\n"
"border-style:solid ;\n"
"    border-width: 2px;\n"
"    border-color: rgb(123, 115, 27);\n"
"border-radius: 15px;")
        self.Service_frame.setFrameShape(QFrame.StyledPanel)
        self.Service_frame.setFrameShadow(QFrame.Raised)
        self.Name = QTextBrowser(self.Service_frame)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(50, 10, 500, 41))
        self.Name.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Address = QTextBrowser(self.Service_frame)
        self.Address.setObjectName(u"Address")
        self.Address.setGeometry(QRect(10, 70, 721, 41))
        self.Address.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Address.setAutoFormatting(QTextEdit.AutoNone)
        self.Phone = QTextBrowser(self.Service_frame)
        self.Phone.setObjectName(u"Phone")
        self.Phone.setGeometry(QRect(1010, 10, 251, 41))
        self.Phone.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.ID = QTextBrowser(self.Service_frame)
        self.ID.setObjectName(u"ID")
        self.ID.setGeometry(QRect(10, 10, 31, 41))
        self.ID.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Manager = QTextBrowser(self.Service_frame)
        self.Manager.setObjectName(u"Manager")
        self.Manager.setGeometry(QRect(1010, 70, 221, 41))
        self.Manager.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Manager.setAutoFormatting(QTextEdit.AutoNone)

        self.retranslateUi(Service_form)

        QMetaObject.connectSlotsByName(Service_form)
    # setupUi

    def retranslateUi(self, Service_form):
        Service_form.setWindowTitle(QCoreApplication.translate("Service_form", u"Form", None))
        self.Name.setHtml(QCoreApplication.translate("Service_form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">Service_name</span></p></body></html>", None))
        self.Address.setHtml(QCoreApplication.translate("Service_form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">service_address</span></p></body></html>", None))
        self.Phone.setHtml(QCoreApplication.translate("Service_form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">service_phone_number</span></p></body></html>", None))
        self.ID.setHtml(QCoreApplication.translate("Service_form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">ID</span></p></body></html>", None))
        self.Manager.setHtml(QCoreApplication.translate("Service_form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">service_manager</span></p></body></html>", None))
    # retranslateUi

