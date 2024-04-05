import sqlite3
from datetime import datetime


class Database:
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file, check_same_thread=False)
        self.con.cursor().execute("CREATE TABLE IF NOT EXISTS userdata(theme INTEGER, logs INTEGER, log TEXT, api_key TEXT, join_date TEXT)")
        if self.con.cursor().execute("SELECT COUNT(*) FROM userdata").fetchone()[0] == 0:
            join_date = datetime.now().strftime("%m/%d/%Y")
            self.con.cursor().execute("INSERT INTO userdata VALUES (0, 1, '', '', '"+join_date+"')")
        self.con.cursor().execute("CREATE TABLE IF NOT EXISTS stats(last TEXT, orders INTEGER, sales INTEGER, questions INTEGER, feedbacks INTEGER)")

    def check_userdata(self):
        with self.con:
            return self.con.cursor().execute("SELECT * FROM userdata").fetchone()
        
    def edit_userdata(self, theme, logs, api_key):
        with self.con:
            self.con.cursor().execute("UPDATE userdata SET theme = ?, logs = ?, api_key = ?", (theme, logs, api_key,))

    '''
    def check_logs(self):
        with self.con:
            return self.con.cursor().execute("SELECT log FROM userdata").fetchone()
    '''

    '''            
    def add_log(self, log):
        with self.con:
            self.con.cursor().execute("UPDATE userdata SET log = ?", (log,))
    '''
            
    def update_date(self, last):
        with self.con:
            self.con.cursor().execute("UPDATE stats SET last = ?", (last,))

    def update_orders(self, orders):
        with self.con:
            self.con.cursor().execute("UPDATE stats SET orders = ?", (orders,))
    
    def update_sales(self, sales):
        with self.con:
            self.con.cursor().execute("UPDATE stats SET sales = ?", (sales,))

    def update_questions(self, questions):
        with self.con:
            self.con.cursor().execute("UPDATE stats SET questions = ?", (questions,))

    def update_feedbacks(self, feedbacks):
        with self.con:
            self.con.cursor().execute("UPDATE stats SET feedbacks = ?", (feedbacks,))
