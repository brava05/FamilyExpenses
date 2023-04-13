# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Curency.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import res_new_tr

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 373)
        Dialog.setStyleSheet(u"background-color: LightSkyBlue;")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 361, 341))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 291, 31))
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 70, 301, 282))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dateEdit = QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")
        self.dateEdit.setDate(QDate(2023, 1, 1))

        self.verticalLayout.addWidget(self.dateEdit)

        self.input_currency = QLineEdit(self.layoutWidget)
        self.input_currency.setObjectName(u"input_currency")
        self.input_currency.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.input_currency)

        self.input_amount = QLineEdit(self.layoutWidget)
        self.input_amount.setObjectName(u"input_amount")
        self.input_amount.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.input_amount)

        self.output_currency = QLineEdit(self.layoutWidget)
        self.output_currency.setObjectName(u"output_currency")
        self.output_currency.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.output_currency)

        self.output_amount = QLineEdit(self.layoutWidget)
        self.output_amount.setObjectName(u"output_amount")
        self.output_amount.setMaximumSize(QSize(16777209, 16777215))
        self.output_amount.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.output_amount)

        self.ButtonConvert = QPushButton(self.layoutWidget)
        self.ButtonConvert.setObjectName(u"ButtonConvert")
        self.ButtonConvert.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230 px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/arrow_right_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonConvert.setIcon(icon)
        self.ButtonConvert.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.ButtonConvert)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Currency converter", None))
        self.input_currency.setPlaceholderText(QCoreApplication.translate("Dialog", u"input currency", None))
        self.input_amount.setPlaceholderText(QCoreApplication.translate("Dialog", u"input amount", None))
        self.output_currency.setText("")
        self.output_currency.setPlaceholderText(QCoreApplication.translate("Dialog", u"output currency", None))
        self.output_amount.setText("")
        self.output_amount.setPlaceholderText(QCoreApplication.translate("Dialog", u"output amount", None))
        self.ButtonConvert.setText(QCoreApplication.translate("Dialog", u"Convert", None))
    # retranslateUi

