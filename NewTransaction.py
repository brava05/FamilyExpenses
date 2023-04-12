# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewTransaction.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#     QMetaObject, QObject, QPoint, QRect,
#     QSize, QTime, QUrl, Qt)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#     QFont, QFontDatabase, QGradient, QIcon,
#     QImage, QKeySequence, QLinearGradient, QPainter,
#     QPalette, QPixmap, QRadialGradient, QTransform)
# from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
#     QFrame, QLabel, QLineEdit, QPushButton,
#     QSizePolicy, QVBoxLayout, QWidget)
# import res_new_tr_rc

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
        self.label.setGeometry(QRect(70, 20, 241, 31))
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 70, 301, 251))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.combo_category = QComboBox(self.widget)
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.setObjectName(u"combo_category")
        self.combo_category.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}\n"
"")
        self.combo_category.setMaxVisibleItems(10)

        self.verticalLayout.addWidget(self.combo_category)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")
        self.dateEdit.setDate(QDate(2023, 1, 1))

        self.verticalLayout.addWidget(self.dateEdit)

        self.le_Descr = QLineEdit(self.widget)
        self.le_Descr.setObjectName(u"le_Descr")
        self.le_Descr.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_Descr)

        self.le_Balance = QLineEdit(self.widget)
        self.le_Balance.setObjectName(u"le_Balance")
        self.le_Balance.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_Balance)

        self.combo_Income = QComboBox(self.widget)
        self.combo_Income.addItem("")
        self.combo_Income.addItem("")
        self.combo_Income.setObjectName(u"combo_Income")
        self.combo_Income.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}")

        self.verticalLayout.addWidget(self.combo_Income)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Dialog)

        self.combo_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"New transaction", None))
        self.combo_category.setItemText(0, QCoreApplication.translate("Dialog", u"Grosseries", None))
        self.combo_category.setItemText(1, QCoreApplication.translate("Dialog", u"Entertaiment", None))
        self.combo_category.setItemText(2, QCoreApplication.translate("Dialog", u"Auto", None))
        self.combo_category.setItemText(3, QCoreApplication.translate("Dialog", u"Other", None))

        self.combo_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose category", None))
        self.le_Descr.setPlaceholderText(QCoreApplication.translate("Dialog", u"Description", None))
        self.le_Balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.combo_Income.setItemText(0, QCoreApplication.translate("Dialog", u"Income", None))
        self.combo_Income.setItemText(1, QCoreApplication.translate("Dialog", u"Outcome", None))

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
    # retranslateUi

