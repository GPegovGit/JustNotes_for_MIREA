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
        self.Plate = QTextBrowser(self.Part_frame)
        self.Plate.setObjectName(u"Plate")
        self.Plate.setGeometry(QRect(100, 10, 1091, 41))
        self.Plate.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Color = QTextBrowser(self.Part_frame)
        self.Color.setObjectName(u"Color")
        self.Color.setGeometry(QRect(10, 70, 141, 41))
        self.Color.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Color.setAutoFormatting(QTextEdit.AutoNone)
        self.Model = QTextBrowser(self.Part_frame)
        self.Model.setObjectName(u"Model")
        self.Model.setGeometry(QRect(1100, 70, 131, 41))
        self.Model.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Model.setAutoFormatting(QTextEdit.AutoNone)
        self.Color_number = QTextBrowser(self.Part_frame)
        self.Color_number.setObjectName(u"Color_number")
        self.Color_number.setGeometry(QRect(150, 73, 221, 41))
        self.Color_number.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Model_number = QTextBrowser(self.Part_frame)
        self.Model_number.setObjectName(u"Model_number")
        self.Model_number.setGeometry(QRect(1240, 73, 31, 41))
        self.Model_number.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Value_number = QTextBrowser(self.Part_frame)
        self.Value_number.setObjectName(u"Value_number")
        self.Value_number.setGeometry(QRect(680, 73, 131, 41))
        self.Value_number.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Value = QTextBrowser(self.Part_frame)
        self.Value.setObjectName(u"Value")
        self.Value.setGeometry(QRect(460, 70, 221, 41))
        self.Value.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Value.setAutoFormatting(QTextEdit.AutoNone)

        self.retranslateUi(Part_widget)

        QMetaObject.connectSlotsByName(Part_widget)
    # setupUi

    def retranslateUi(self, Part_widget):
        Part_widget.setWindowTitle(QCoreApplication.translate("Part_widget", u"Form", None))
        self.Plate.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">license_plate</span></p></body></html>", None))
        self.Color.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">Color:</span></p></body></html>", None))
        self.Model.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">Model ID:</span></p></body></html>", None))
        self.Color_number.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">ID</span></p></body></html>", None))
        self.Model_number.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">ID</span></p></body></html>", None))
        self.Value_number.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">ID</span></p></body></html>", None))
        self.Value.setHtml(QCoreApplication.translate("Part_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">Estimated Value:</span></p></body></html>", None))
    # retranslateUi

