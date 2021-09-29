from mysql import connector
from mysql.connector import Error
from mysql.connector.errors import IntegrityError


class DbConnection:
    def __init__(self):
        try:
            self.conn = connector.connect(
                host='localhost',
                username='root',
                password='Acc3$$D3ni3d',
                db='recording'
            )
            self.cur = self.conn.cursor()
        except Error:
            print('=============================================')
            print('Database Connection Error')
            print('======================')
            print('Wait, database is connecting automatically...')
            print('======================')
            try:
                self.conn = connector.connect(
                    host='localhost',
                    username='root',
                    password='',
                    db='recording'
                )
                self.cur = self.conn.cursor()
                print('Database is now connected')
                print('=============================================')
            except Error as e:
                print('You need to connect database manually')
                print('=============================================')

    def update(self, query, values):
        self.cur.execute(query, values)
        self.conn.commit()

    def delete(self, query, values):
        self.cur.execute(query, values)
        self.conn.commit()

    def select(self, query):
        self.cur.execute(query)
        results = self.cur.fetchall()
        self.conn.commit()
        return results

    def select_value(self, query, value):
        self.cur.execute(query, value)
        results = self.cur.fetchall()
        self.conn.commit()
        return results

    def insert(self, query, values):
        self.cur.execute(query, values)
        self.conn.commit()

    def __del__(self):
        try:
            if self.cur:
                self.cur.close()

            if self.conn:
                self.conn.close()
        except ReferenceError:
            print('Connection Destroyed  ')