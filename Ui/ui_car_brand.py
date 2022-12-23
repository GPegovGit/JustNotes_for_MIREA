from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize, QCoreApplication, QMetaObject
from PyQt5.QtWidgets import QLineEdit, QFrame, QTextBrowser, QTextEdit

class Ui_Car_Brand_widget(object):
    def setupUi(self, Part_widget):
        if not Part_widget.objectName():
            Part_widget.setObjectName(u"Part_widget")
        Part_widget.resize(1322, 61)
        self.Part_frame = QFrame(Part_widget)
        self.Part_frame.setObjectName(u"Part_frame")
        self.Part_frame.setGeometry(QRect(0, 0, 1281, 61))
        self.Part_frame.setMinimumSize(QSize(1240, 61))
        self.Part_frame.setMaximumSize(QSize(1281, 61))
        self.Part_frame.setStyleSheet(u"background-color: rgb(36, 37, 39);\n"
"border-style:solid ;\n"
"    border-width: 2px;\n"
"    border-color: rgb(123, 115, 27);\n"
"border-radius: 15px;")
        self.Part_frame.setFrameShape(QFrame.StyledPanel)
        self.Part_frame.setFrameShadow(QFrame.Raised)
        self.Car_brand = QTextBrowser(self.Part_frame)
        self.Car_brand.setObjectName(u"Car_brand")
        self.Car_brand.setGeometry(QRect(100, 10, 1091, 41))
        self.Car_brand.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.ID = QTextBrowser(self.Part_frame)
        self.ID.setObjectName(u"ID")
        self.ID.setGeometry(QRect(10, 10, 51, 41))
        self.ID.setStyleSheet(u"text-align: center;\n"
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
        self.Car_brand.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">Car_brand</span></p></body></html>", None))
        self.ID.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">ID</span></p></body></html>", None))
    # retranslateUi

