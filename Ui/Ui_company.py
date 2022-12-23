from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize, QCoreApplication, QMetaObject
from PyQt5.QtWidgets import QLineEdit, QFrame, QTextBrowser, QTextEdit


class Ui_Part_widget(object):
    def setupUi(self, Part_widget):
        if not Part_widget.objectName():
            Part_widget.setObjectName(u"Part_widget")
        Part_widget.resize(1322, 132)
        self.Part_frame = QFrame(Part_widget)
        self.Part_frame.setObjectName(u"Part_frame")
        self.Part_frame.setGeometry(QRect(0, 0, 1281, 122))
        self.Part_frame.setMinimumSize(QSize(1240, 122))
        self.Part_frame.setMaximumSize(QSize(1281, 122))
        self.Part_frame.setStyleSheet(u"background-color: rgb(36, 37, 39);\n"
"border-style:solid ;\n"
"    border-width: 2px;\n"
"    border-color: rgb(123, 115, 27);\n"
"border-radius: 15px;")
        self.Part_frame.setFrameShape(QFrame.StyledPanel)
        self.Part_frame.setFrameShadow(QFrame.Raised)
        self.Name = QTextBrowser(self.Part_frame)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(100, 10, 1091, 41))
        self.Name.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Email = QTextBrowser(self.Part_frame)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(1010, 70, 261, 41))
        self.Email.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Email.setAutoFormatting(QTextEdit.AutoNone)
        self.Phone = QTextBrowser(self.Part_frame)
        self.Phone.setObjectName(u"Phone")
        self.Phone.setGeometry(QRect(10, 70, 221, 41))
        self.Phone.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Phone.setAutoFormatting(QTextEdit.AutoNone)
        self.Id = QTextBrowser(self.Part_frame)
        self.Id.setObjectName(u"Id")
        self.Id.setGeometry(QRect(10, 10, 41, 41))
        self.Id.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")

        self.retranslateUi(Part_widget)

        QMetaObject.connectSlotsByName(Part_widget)
    # setupUi

    def retranslateUi(self, Part_widget):
        Part_widget.setWindowTitle(QCoreApplication.translate("Part_widget", u"Form", None))
        self.Name.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">Name</span></p></body></html>", None))
        self.Email.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">email</span></p></body></html>", None))
        self.Phone.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">89168233658</span></p></body></html>", None))
        self.Id.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">12</span></p></body></html>", None))
    # retranslateUi

