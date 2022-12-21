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
        self.Part_name = QTextBrowser(self.Part_frame)
        self.Part_name.setObjectName(u"Part_name")
        self.Part_name.setGeometry(QRect(100, 10, 1091, 41))
        self.Part_name.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Manufacture = QTextBrowser(self.Part_frame)
        self.Manufacture.setObjectName(u"Manufacture")
        self.Manufacture.setGeometry(QRect(10, 70, 141, 41))
        self.Manufacture.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Manufacture.setAutoFormatting(QTextEdit.AutoNone)
        self.ID = QTextBrowser(self.Part_frame)
        self.ID.setObjectName(u"ID")
        self.ID.setGeometry(QRect(10, 10, 31, 41))
        self.ID.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Price = QTextBrowser(self.Part_frame)
        self.Price.setObjectName(u"Price")
        self.Price.setGeometry(QRect(1100, 70, 131, 41))
        self.Price.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Price.setAutoFormatting(QTextEdit.AutoNone)
        self.ID_2 = QTextBrowser(self.Part_frame)
        self.ID_2.setObjectName(u"ID_2")
        self.ID_2.setGeometry(QRect(150, 73, 31, 41))
        self.ID_2.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.ID_3 = QTextBrowser(self.Part_frame)
        self.ID_3.setObjectName(u"ID_3")
        self.ID_3.setGeometry(QRect(1240, 73, 31, 41))
        self.ID_3.setStyleSheet(u"text-align: center;\n"
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
        self.Part_name.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">Model_name</span></p></body></html>", None))
        self.Manufacture.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">Model Year:</span></p></body></html>", None))
        self.ID.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">ID</span></p></body></html>", None))
        self.Price.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">Brand ID:</span></p></body></html>", None))
        self.ID_2.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">ID</span></p></body></html>", None))
        self.ID_3.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">ID</span></p></body></html>", None))
    # retranslateUi

