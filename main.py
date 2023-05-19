import sys
# import datetime
from datetime import datetime as dt
from datetime import timedelta

import yfinance as yf
import yahoo_fin.stock_info as si
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel
from currency_converter import CurrencyConverter

from connection import Data
from main_form import Ui_MainWindow
from NewTransaction import Ui_Dialog
from Currency import Ui_Dialog as Ui_Currency
from portfolio_meneger import Ui_Dialog as Ui_Portfolio


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.new_window = None
        self.model = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.conn = Data()

    def init_ui(self):
        self.ui.ButtonConverter.clicked.connect(self.open_converter)
        self.ui.Button_NewTransaction.clicked.connect(self.open_new_transaction_window)
        self.ui.PortfolioMeneger.clicked.connect(self.open_portfolio_window)

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
        self.ui_window.output_currency.setText("RUB")
        self.ui_window.input_amount.setText("100")
        self.new_window.show()
        self.ui_window.ButtonConvert.clicked.connect(self.convert)

    def open_portfolio_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Portfolio()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.button_show_allocation.clicked.connect(self.show_allocation)
        self.ui_window.button_add_new_share.clicked.connect(self.add_new_share)

        self.new_window.show()

    def convert_CC(self):
        conv = CurrencyConverter()
        input_currency = self.ui_window.input_currency.text()
        output_currency = self.ui_window.output_currency.text()
        input_amount = int(self.ui_window.input_amount.text())
        date_time_str = self.ui_window.dateEdit.text()
        date_time_obj = dt.strptime(date_time_str, '%d.%m.%Y')
        # output_amount = conv.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency), date_time_obj)
        output_amount = conv.convert(input_amount, input_currency, output_currency, date_time_obj)
        self.ui_window.output_amount.setText(str(output_amount))

    def convert(self):
        # yahoofin
        input_currency = self.ui_window.input_currency.text()
        output_currency = self.ui_window.output_currency.text()
        input_amount = int(self.ui_window.input_amount.text())
        date_time_str = self.ui_window.dateEdit.text()
        date_time_obj = dt.strptime(date_time_str, '%d.%m.%Y')
        # construct the currency pair symbol
        symbol = f"{input_currency}{output_currency}=X"
        latest_data = si.get_data(symbol, interval="1d", start_date=date_time_obj+timedelta(days=-2), end_date=date_time_obj)
        latest_price = latest_data.iloc[-1].close

        output_amount = latest_price * input_amount
        self.ui_window.output_amount.setText(str(output_amount))

    def show_allocation(self):
        self.update_all_prices()
        self.conn.update_percentages()

        self.model = QSqlTableModel(self)
        self.model.setTable('portfolio')
        self.model.select()
        self.ui_window.tableView.setModel(self.model)

    def add_new_share(self):
        share = self.ui_window.Share.text()
        quantity = int(self.ui_window.Quantity.text())
        self.conn.add_new_share_query(share, quantity, 10)
        self.show_allocation()

    def update_all_prices(self):
        shares = self.conn.get_all_shares()

        today_data = dt.today()
        today_str = today_data.strftime("%Y-%m-%d")
        start_data = today_data + timedelta(days=-10)
        start_str = start_data.strftime("%Y-%m-%d")

        for ticker in shares:
            data = yf.download(ticker, start_str, today_str)['Adj Close']
            if data.empty:
                continue

            # надо брать последнюю цену, а запрос не возвращает предыдущую цену
            # если запросить только одну дату и на нее не окажется цены
            price = data[data.size - 1]
            self.conn.update_price(ticker, float(price))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
