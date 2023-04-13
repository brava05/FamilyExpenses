import sys

from datetime import datetime as dt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from currency_converter import CurrencyConverter
from main_form import Ui_MainWindow
from NewTransaction import Ui_Dialog
from Currency import Ui_Dialog as Ui_Currency


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.ui.ButtonConverter.clicked.connect(self.open_converter)
        self.ui.Button_NewTransaction.clicked.connect(self.open_new_transaction_window)

    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def open_converter(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Currency()
        self.ui_window.setupUi(self.new_window)

        self.ui_window.input_currency.setText("USD")
        self.ui_window.output_currency.setText("EUR")
        self.ui_window.input_amount.setText("100")
        self.new_window.show()
        self.ui_window.ButtonConvert.clicked.connect(self.convert)

    def convert(self):
        conv = CurrencyConverter()
        input_currency = self.ui_window.input_currency.text()
        output_currency = self.ui_window.output_currency.text()
        input_amount = int(self.ui_window.input_amount.text())
        date_time_str = self.ui_window.dateEdit.text()
        date_time_obj = dt.strptime(date_time_str, '%d.%m.%Y')
        output_amount = conv.convert(input_amount,
                                     '%s' % (input_currency),
                                     '%s' % (output_currency),
                                     date_time_obj)
        self.ui_window.output_amount.setText(str(output_amount))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
