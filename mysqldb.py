import mysql.connector as con
import pandas as pd

class DB:
    def __init__(self):
        self.mydb = con.connect(
            host="localhost",
            user="root",
            passwd="hyun403301",
            #auth_plugin='mysql_native_password',
            database="mydb"
        )

    def search_article_by_id(self, article_id):
        cur = self.mydb.cursor()
        query = "select * from articles Where article_id = " + str(article_id)
        result = pd.read_sql(query, self.mydb)
        return result

    def query_article(self, article_id, journal_id, authors, name):
        cur = self.mydb.cursor()
        input = str((authors_id))
        query = "insert into articles values"
        pass

    def update_article(self, author_id):
        self.cur.execute("""
        UPDATE Authors SET total_citation = total_citation + 1 WHERE author_id = """ + author_id
        )

    def delete_article(self):
        pass
if __name__ == "__main__" :
    db = DB()
    db.search_article_by_id(1)
