import mysql.connector as con

class DB:

    def __init__(self):
        mydb = con.connect(
            host="localhost",
            user="root",
            passwd="abracadata",
            database="mydb"
        )
        self.cur = mydb.cursor()
        self.init_tables()


    def init_tables(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                article_id      INT PRIMARY KEY,
                journal_name    CHAR(255),
                journal_id      INT
            );
        ''')

    def insert_article(self):
        pass

    def query_article(self):
        pass

    def update_article(self):
        pass

    def delete_article(self):
        pass

