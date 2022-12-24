from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class ui_task(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1390, 148)
        self.Task_form = QtWidgets.QFrame(Form)
        self.Task_form.setObjectName(u"Task_form")
        self.Task_form.setGeometry(QtCore.QRect(5, 0, 1281, 122))
        self.Task_form.setMinimumSize(QtCore.QSize(1281, 122))
        self.Task_form.setMaximumSize(QtCore.QSize(1281, 122))
        self.Task_form.setStyleSheet(u"background-color: rgb(36, 37, 39);\n"
"border-style:solid ;\n"
"    border-width: 2px;\n"
"    border-color: rgb(123, 115, 27);\n"
"border-radius: 15px;")
        self.Task_form.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Task_form.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Task_text = QtWidgets.QTextBrowser(self.Task_form)
        self.Task_text.setObjectName(u"Task_text")
        self.Task_text.setGeometry(QtCore.QRect(80, 10, 817, 41))
        self.Task_text.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Part_id = QtWidgets.QTextBrowser(self.Task_form)
        self.Part_id.setObjectName(u"Priority")
        self.Part_id.setGeometry(QtCore.QRect(60, 70, 111, 41))
        self.Part_id.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Part_id.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.Exucutor_id = QtWidgets.QTextBrowser(self.Task_form)
        self.Exucutor_id.setObjectName(u"Exucutor_id")
        self.Exucutor_id.setGeometry(QtCore.QRect(231, 70, 145, 41))
        self.Exucutor_id.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")


        self.License_plate = QtWidgets.QTextBrowser(self.Task_form)
        self.License_plate.setObjectName(u"License_plate")
        self.License_plate.setGeometry(QtCore.QRect(507, 70, 160, 41))
        self.License_plate.setStyleSheet(u"text-align: center;\n"
                                       "font-family: Myriad Pro;\n"
                                       "color: rgb(123, 115, 27);\n"
                                       "font-size:25px;;\n"
                                       "background-color: rgb(36, 37, 39);\n"
                                       "text-decorations: none;\n"
                                       "border-style:none ;")

        self.Service_id = QtWidgets.QTextBrowser(self.Task_form)
        self.Service_id.setObjectName(u"Service_id")
        self.Service_id.setGeometry(QtCore.QRect(883, 70, 132, 41))
        self.Service_id.setStyleSheet(u"text-align: center;\n"
                                         "font-family: Myriad Pro;\n"
                                         "color: rgb(123, 115, 27);\n"
                                         "font-size:25px;;\n"
                                         "background-color: rgb(36, 37, 39);\n"
                                         "text-decorations: none;\n"
                                         "border-style:none ;")

        self.Service_id_number = QtWidgets.QTextBrowser(self.Task_form)
        self.Service_id_number.setObjectName(u"License_plate_number")
        self.Service_id_number.setGeometry(QtCore.QRect(1021, 70, 51, 41))
        self.Service_id_number.setStyleSheet(u"text-align: center;\n"
                                                "font-family: Myriad Pro;\n"
                                                "color: rgb(123, 115, 27);\n"
                                                "font-size:25px;;\n"
                                                "background-color: rgb(36, 37, 39);\n"
                                                "text-decorations: none;\n"
                                                "border-style:none ;")

        self.License_plate_number = QtWidgets.QTextBrowser(self.Task_form)
        self.License_plate_number.setObjectName(u"License_plate_number")
        self.License_plate_number.setGeometry(QtCore.QRect(676, 70, 145, 41))
        self.License_plate_number.setStyleSheet(u"text-align: center;\n"
                                           "font-family: Myriad Pro;\n"
                                           "color: rgb(123, 115, 27);\n"
                                           "font-size:25px;;\n"
                                           "background-color: rgb(36, 37, 39);\n"
                                           "text-decorations: none;\n"
                                           "border-style:none ;")

        self.Task_id = QtWidgets.QTextBrowser(self.Task_form)
        self.Task_id.setObjectName(u"Task_id")
        self.Task_id.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.Task_id.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Deadline = QtWidgets.QTextBrowser(self.Task_form)
        self.Deadline.setObjectName(u"Deadline")
        self.Deadline.setGeometry(QtCore.QRect(1135, 70, 140, 41))
        self.Deadline.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Deadline.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.Task_Status = QtWidgets.QTextBrowser(self.Task_form)
        self.Task_Status.setObjectName(u"Task_Status")
        self.Task_Status.setGeometry(QtCore.QRect(1120, 10, 111, 41))
        self.Task_Status.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Task_Status.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.Part_id_number = QtWidgets.QTextBrowser(self.Task_form)
        self.Part_id_number.setObjectName(u"Priority_number")
        self.Part_id_number.setGeometry(QtCore.QRect(180, 70, 51, 41))
        self.Part_id_number.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Executor_number = QtWidgets.QTextBrowser(self.Task_form)
        self.Executor_number.setObjectName(u"Executor_number")
        self.Executor_number.setGeometry(QtCore.QRect(425, 70, 51, 41))
        self.Executor_number.setStyleSheet(u"text-align: center;\n"
"font-family: Myriad Pro;\n"
"color: rgb(123, 115, 27);\n"
"font-size:25px;;\n"
"background-color: rgb(36, 37, 39);\n"
"text-decorations: none;\n"
"border-style:none ;")
        self.Change_task = QtWidgets.QPushButton(self.Task_form)
        self.Change_task.setObjectName(u"Change_task")
        self.Change_task.setGeometry(QtCore.QRect(10, 70, 41, 41))
        self.Change_task.setAutoFillBackground(False)
        self.Change_task.setStyleSheet(u"background-color: rgb(123, 115, 27);\n"
"border-radius: 20px;")
        icon = QtGui.QIcon()
        icon.addFile(u"C:/Users/User/PycharmProjects/JustNotes_for_MIREA/Source/Settings.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Change_task.setIcon(icon)
        self.Change_task.setIconSize(QtCore.QSize(25, 25))

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCore.QCoreApplication.translate("Form", u"Form", None))
        self.Task_text.setHtml(QtCore.QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">Name</span></p></body></html>", None))


        self.Part_id.setHtml(QtCore.QCoreApplication.translate("Form",
                                                                  u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
                                                                  "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">Part ID:</span></p></body></html>",
                                                                  None))

        self.Part_id_number.setHtml(QtCore.QCoreApplication.translate("Form",
                                                                         u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                         "p, li { white-space: pre-wrap; }\n"
                                                                         "</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
                                                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">12</span></p></body></html>",
                                                                         None))

        self.Service_id.setHtml(QtCore.QCoreApplication.translate("Form",
                                                                     u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                     "p, li { white-space: pre-wrap; }\n"
                                                                     "</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
                                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">Service ID:</span></p></body></html>",
                                                                     None))

        self.License_plate.setHtml(QtCore.QCoreApplication.translate("Form",
                                                                   u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                   "p, li { white-space: pre-wrap; }\n"
                                                                   "</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
                                                                   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">License Plate:</span></p></body></html>",
                                                                   None))

        self.Service_id_number.setHtml(QtCore.QCoreApplication.translate("Form",
                                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                            "p, li { white-space: pre-wrap; }\n"
                                                                            "</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
                                                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">12</span></p></body></html>",
                                                                            None))

        self.License_plate_number.setHtml(QtCore.QCoreApplication.translate("Form",
                                                                       u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                       "p, li { white-space: pre-wrap; }\n"
                                                                       "</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
                                                                       "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">A888AA000</span></p></body></html>",
                                                                       None))
        self.Exucutor_id.setHtml(QtCore.QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tahoma'; font-size:16pt;\">Executor ID:</span></p></body></html>", None))
        self.Task_id.setHtml(QtCore.QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">ID:</span></p></body></html>", None))
        self.Deadline.setHtml(QtCore.QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">Deadline:</span></p></body></html>", None))
        self.Task_Status.setHtml(QtCore.QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">Status:</span></p></body></html>", None))

        self.Executor_number.setHtml(QtCore.QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Myriad Pro'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25px;\">ID</span></p></body></html>", None))
        self.Change_task.setText("")
    # retranslateUi

