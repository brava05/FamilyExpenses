# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QVBoxLayout,
    QWidget)
import res_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1242, 666)
        MainWindow.setMaximumSize(QSize(1242, 16777215))
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: LightSkyBlue;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.PortfolioMeneger = QPushButton(self.centralwidget)
        self.PortfolioMeneger.setObjectName(u"PortfolioMeneger")
        self.PortfolioMeneger.setMaximumSize(QSize(16777215, 16777215))
        self.PortfolioMeneger.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/icons/icons/savings_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.PortfolioMeneger.setIcon(icon)
        self.PortfolioMeneger.setIconSize(QSize(48, 48))

        self.horizontalLayout_9.addWidget(self.PortfolioMeneger)

        self.ButtonConverter = QPushButton(self.centralwidget)
        self.ButtonConverter.setObjectName(u"ButtonConverter")
        self.ButtonConverter.setMaximumSize(QSize(16777215, 16777215))
        self.ButtonConverter.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/price_change_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonConverter.setIcon(icon1)
        self.ButtonConverter.setIconSize(QSize(48, 48))

        self.horizontalLayout_9.addWidget(self.ButtonConverter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.Balance_frame = QFrame(self.centralwidget)
        self.Balance_frame.setObjectName(u"Balance_frame")
        self.Balance_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.horizontalLayout_6 = QHBoxLayout(self.Balance_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.la_CurrentBalance = QLabel(self.Balance_frame)
        self.la_CurrentBalance.setObjectName(u"la_CurrentBalance")
        self.la_CurrentBalance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.la_CurrentBalance)

        self.la_Balance = QLabel(self.Balance_frame)
        self.la_Balance.setObjectName(u"la_Balance")
        self.la_Balance.setStyleSheet(u"color: white;\n"
"font-size: 35pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.la_Balance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.Balance_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 16777215))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.label_3.setPixmap(QPixmap(u":/icons/icons/monetization_on_FILL0_wght400_GRAD0_opsz48.svg"))

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.Balance_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.la_Income = QLabel(self.Balance_frame)
        self.la_Income.setObjectName(u"la_Income")
        self.la_Income.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.la_Income)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.Balance_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(60, 16777215))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.label_6.setPixmap(QPixmap(u":/icons/icons/heart_minus_FILL0_wght400_GRAD0_opsz48.svg"))

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_5 = QLabel(self.Balance_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.la_Outcome = QLabel(self.Balance_frame)
        self.la_Outcome.setObjectName(u"la_Outcome")
        self.la_Outcome.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.la_Outcome)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.CategoriesFrame = QFrame(self.Balance_frame)
        self.CategoriesFrame.setObjectName(u"CategoriesFrame")
        self.CategoriesFrame.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.CategoriesFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.label_9 = QLabel(self.CategoriesFrame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_grossery = QLabel(self.CategoriesFrame)
        self.icon_grossery.setObjectName(u"icon_grossery")
        self.icon_grossery.setMaximumSize(QSize(55, 16777215))
        self.icon_grossery.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_grossery.setPixmap(QPixmap(u":/icons/icons/home_FILL0_wght400_GRAD0_opsz48.svg"))

        self.horizontalLayout_3.addWidget(self.icon_grossery)

        self.la_grossery = QLabel(self.CategoriesFrame)
        self.la_grossery.setObjectName(u"la_grossery")
        self.la_grossery.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"color: white;\n"
"font-size: 14pt;\n"
"font-weight: bold;\n"
"")

        self.horizontalLayout_3.addWidget(self.la_grossery)

        self.balance_grossery = QLabel(self.CategoriesFrame)
        self.balance_grossery.setObjectName(u"balance_grossery")
        self.balance_grossery.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"font-weight: bold;")

        self.horizontalLayout_3.addWidget(self.balance_grossery)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_auto = QLabel(self.CategoriesFrame)
        self.icon_auto.setObjectName(u"icon_auto")
        self.icon_auto.setMaximumSize(QSize(55, 16777215))
        self.icon_auto.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_auto.setPixmap(QPixmap(u":/icons/icons/emoji_transportation_FILL0_wght400_GRAD0_opsz48.svg"))

        self.horizontalLayout_4.addWidget(self.icon_auto)

        self.la_auto = QLabel(self.CategoriesFrame)
        self.la_auto.setObjectName(u"la_auto")
        self.la_auto.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"color: white;\n"
"font-size: 14pt;\n"
"font-weight: bold;")

        self.horizontalLayout_4.addWidget(self.la_auto)

        self.balance_auto = QLabel(self.CategoriesFrame)
        self.balance_auto.setObjectName(u"balance_auto")
        self.balance_auto.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"font-weight: bold;")

        self.horizontalLayout_4.addWidget(self.balance_auto)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.icon_other = QLabel(self.CategoriesFrame)
        self.icon_other.setObjectName(u"icon_other")
        self.icon_other.setMaximumSize(QSize(55, 16777215))
        self.icon_other.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_other.setPixmap(QPixmap(u":/icons/icons/settings_accessibility_FILL0_wght400_GRAD0_opsz48.svg"))

        self.horizontalLayout_5.addWidget(self.icon_other)

        self.le_ohter = QLabel(self.CategoriesFrame)
        self.le_ohter.setObjectName(u"le_ohter")
        self.le_ohter.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"color: white;\n"
"font-size: 14pt;\n"
"font-weight: bold;")

        self.horizontalLayout_5.addWidget(self.le_ohter)

        self.balance_other = QLabel(self.CategoriesFrame)
        self.balance_other.setObjectName(u"balance_other")
        self.balance_other.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"font-weight: bold;")

        self.horizontalLayout_5.addWidget(self.balance_other)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addWidget(self.CategoriesFrame)


        self.verticalLayout_3.addWidget(self.Balance_frame)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Button_NewTransaction = QPushButton(self.centralwidget)
        self.Button_NewTransaction.setObjectName(u"Button_NewTransaction")
        self.Button_NewTransaction.setMaximumSize(QSize(16777215, 16777215))
        self.Button_NewTransaction.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/add_box_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_NewTransaction.setIcon(icon2)
        self.Button_NewTransaction.setIconSize(QSize(48, 48))

        self.horizontalLayout_7.addWidget(self.Button_NewTransaction)

        self.Button_EditTransaction = QPushButton(self.centralwidget)
        self.Button_EditTransaction.setObjectName(u"Button_EditTransaction")
        self.Button_EditTransaction.setMaximumSize(QSize(16777215, 16777215))
        self.Button_EditTransaction.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/arrow_right_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_EditTransaction.setIcon(icon3)
        self.Button_EditTransaction.setIconSize(QSize(48, 48))

        self.horizontalLayout_7.addWidget(self.Button_EditTransaction)

        self.Button_DelTransaction = QPushButton(self.centralwidget)
        self.Button_DelTransaction.setObjectName(u"Button_DelTransaction")
        self.Button_DelTransaction.setMaximumSize(QSize(16777215, 16777215))
        self.Button_DelTransaction.setStyleSheet(u"QPushButton {\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/delete_forever_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_DelTransaction.setIcon(icon4)
        self.Button_DelTransaction.setIconSize(QSize(48, 48))

        self.horizontalLayout_7.addWidget(self.Button_DelTransaction)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"QTableView:section {\n"
"color: white;\n"
"background-color: rgba(53, 53, 53);\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"QTableView:item {\n"
"color: white;\n"
"background-color: rgba(53, 53, 53);\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"QTableView:item:selected {\n"
"color: rgba(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1242, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.PortfolioMeneger.setText(QCoreApplication.translate("MainWindow", u"Portfolio meneger", None))
        self.ButtonConverter.setText(QCoreApplication.translate("MainWindow", u"Currency converter", None))
        self.la_CurrentBalance.setText(QCoreApplication.translate("MainWindow", u"Current Balance", None))
        self.la_Balance.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.la_Income.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Outcome", None))
        self.la_Outcome.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Expense categories", None))
        self.icon_grossery.setText("")
        self.la_grossery.setText(QCoreApplication.translate("MainWindow", u"groceries", None))
        self.balance_grossery.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.icon_auto.setText("")
        self.la_auto.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.balance_auto.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.icon_other.setText("")
        self.le_ohter.setText(QCoreApplication.translate("MainWindow", u"other", None))
        self.balance_other.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.Button_NewTransaction.setText(QCoreApplication.translate("MainWindow", u"New transaction", None))
        self.Button_EditTransaction.setText(QCoreApplication.translate("MainWindow", u"Edit transaction", None))
        self.Button_DelTransaction.setText(QCoreApplication.translate("MainWindow", u"Delete transaction", None))
    # retranslateUi

