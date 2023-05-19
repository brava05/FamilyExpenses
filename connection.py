from PySide6 import QtWidgets, QtSql
from PySide6.QtSql import QSqlQuery


def create_connection():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('portfolio_db.db')

    if not db.open():
        QtWidgets.QMessageBox.critical(None,
                                       'Cannot open db portfolio',
                                       'Problems happens',
                                       QtWidgets.QMessageBox.Cancel)
        return False

    query = QtSql.QSqlQuery()
    # query.exec("DROP TABLE portfolio")
    query.exec("CREATE TABLE IF NOT EXISTS portfolio (ID integer primary key AUTOINCREMENT,"
               "Share VARCHAR(20), Quantity INT, Price FLOAT, Amount FLOAT(10, 2),"
               "DeltaAmount FLOAT(10, 2), Percent FLOAT(10, 2), PercentPlan INT)")

    query.exec("CREATE TABLE IF NOT EXISTS expenses (ID integer primary key AUTOINCREMENT,"
               "Category VARCHAR(20),Description VARCHAR(20), Balance REAL, Status VARCHAR(20),")

    return True


class Data:
    def __init__(self):
        super(Data, self).__init__()
        ok = create_connection()

    def execute_query(self, sql_query, values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if values is not None:
            for value in values:
                query.addBindValue(value)

        query.exec()
        return query

    def add_new_share_query(self, share, percent, quantity):
        sql_query = "INSERT INTO portfolio (Share, PercentPlan, Quantity) VALUES (?, ?, ?)"
        self.execute_query(sql_query, [share, quantity, percent])

    def update_price(self, share, price):
        sql_query = "UPDATE portfolio SET Price=?, Amount=Price*Quantity  WHERE Share=?"
        self.execute_query(sql_query, [price, share])

    def update_percentages(self):
        sum = self.get_sum_amount()
        if sum == 0:
            return

        sql_query = "UPDATE portfolio SET Percent=Amount/?*100"
        self.execute_query(sql_query, [sum])

        sql_query = "UPDATE portfolio SET DeltaAmount = (PercentPlan - Percent)*?/100"
        self.execute_query(sql_query, [sum])

    def get_all_shares(self):
        query = QtSql.QSqlQuery("SELECT Share FROM portfolio")
        query.exec()
        res = []
        while query.next():
            res.append(query.value(0))
        return res

    def get_sum_amount(self):
        query = QtSql.QSqlQuery("SELECT SUM(Amount) AS Amount FROM portfolio")
        query.exec()
        while query.next():
            return query.value(0)
        return 0

    def add_new_transaction_query(self, date, category, descr, balance, status):
        sql_query = "INSERT INTO expenses (Date, Category, Description, Balance, Status)" \
                    " VALUES (?, ?, ?, ?, ?)"
        self.execute_query(sql_query, [date, category, descr, balance, status])

    def update_transaction_query(self, date, category, descr, balance, status, id):
        sql_query = "UPDATE expenses SET Date=?, Category=?, Description=?, Balance=?, Status=?" \
                    "WHERE ID=?"
        self.execute_query(sql_query, [date, category, descr, balance, status, id])

    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM expenses WHERE ID=?"
        self.execute_query(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f'SELECT SUM ({column}) FROM expenses'
        if filter is not None and value is not None:
            sql_query += f'WHERE {filter} = ?'

        query_values = []
        if value is not None:
            query_values.append(value)

        query = self.execute_query(sql_query, query_values)

        if query.next():
            return str(query.value(0))

        return "0"

    def total_balance(self):
        return self.get_total(column="Balance")

    def total_income(self):
        return self.get_total(column="Balance", filter="Status", value="Income")

    def total_outcome(self):
        return self.get_total(column="Balance", filter="Status", value="Outcome")

    def total_groceries(self):
        return self.get_total(column="Balance", filter="Category", value="Grocery")

    def total_auto(self):
        return self.get_total(column="Balance", filter="Category", value="Auto")

    def total_other(self):
        return self.get_total(column="Balance", filter="Category", value="Other")


