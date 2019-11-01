import mysql.connector as con
import csv

class DB:

    def __init__(self):
        self.conn = con.connect(
            host="localhost",
            user="root",
            passwd="abracadata",
            database="mydb"
        )
        self.cur = self.conn.cursor()
        self.init_tables()

    def init_tables(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                article_id      INT PRIMARY KEY,
                journal_id      INT,
                journal_name    TEXT,
                authors_name    TEXT
            );
        ''')

    def insert_article(self, article_id, journal_id, journal_name, authors_name):
        insert_query = '''
            INSERT INTO articles
            VALUES (%(article_id)s, %(journal_id)s, %(journal_name)s, %(authors_name)s)
            ON DUPLICATE KEY UPDATE
                journal_id = %(journal_id)s,
                journal_name = %(journal_name)s,
                authors_name = %(authors_name)s;
        '''
        insert_data = {
            'article_id' : article_id,
            'journal_id' : journal_id,
            'journal_name' : journal_name,
            'authors_name' : authors_name
        }
        self.cur.execute(insert_query, insert_data)
        self.conn.commit()

    def load_articles_data(self, csv_path):
        with open(csv_path) as csv_file:
            csv_data = csv.reader(csv_file)
            row_count = -1
            for row in csv_data:
                row_count += 1
                if row_count == 0:
                    continue
                article_id = int(row[0])
                journal_id = int(row[1])
                journal_name = row[2]
                authors_name = row[3]

                self.insert_article(article_id, journal_id, journal_name, authors_name)

    def query_article(self):
        pass

    def update_article(self):
        pass

    def delete_article(self):
        pass

    def close(self):
        self.conn.close()
