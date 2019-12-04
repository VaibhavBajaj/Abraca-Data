import mysql.connector as con
import pandas as pd
import csv

class DB:
    def __init__(self):
        self.mydb = con.connect(
            host="localhost",
            user="root",
            passwd="abracadata",
            database="mydb"
        )

    def query_article(self, id, name, affiliation, pub_title, journal):
        id_query = "true = true"
        name_query = "true = true"
        affiliation_query = "true = true"
        title_query = "true = true"
        journal_query = "true = true"
        if id is None and name is None and affiliation is None and title is None and journal is None:
            return -1

        if id is not None:
            id_query = "id = " + id
        if name is not None:
            name_query = "name LIKE " + name
        if affiliation is not None:
            affiliation_query = "affiliation LIKE " + affiliation
        if pub_title is not None:
            title_query = "pub_title LIKE " + pub_title
        if journal is not None:
            journal_query = "journal LIKE " + journal

        search_query = ''' SELECT * FROM articles
                    WHERE {} AND {} AND {} AND {} AND {}
                '''.format(id_query, name_query, affiliation_query, title_query, journal_query)
        result = pd.read_sql(search_query, self.mydb)
        return result

    # update_data sample dictionary
    # { id : '105', name : 'Vaibhav', affiliation : 'UIUC', citedby : '101', pub_title : 'Article Title',
    #   pub_year : '2012', pub_url : '', journal : 'Journal Name' }

    # Return 0 on success, other error codes on failure
    def update_article(self, update_data):
        if update_data['id'] is None:
            return -1

        data = self.query_article(update_data['id'], None, None, None, None)
        data = data.to_dict()
        for key, value in data.items():
            if update_data[key] is not None:
                data[key] = update_data[key]
            else:
                data[key] = value[0]

        print(update_data)
        update_data = data
        print(update_data)
        update_query = '''
            UPDATE articles
            SET name = %(name)s,
                affiliation = %(affiliation)s,
                citedby = %(citedby)s,
                pub_title = %(pub_title)s,
                pub_year = %(pub_year)s,
                pub_url = %(pub_url)s,
                journal = %(journal)s
            WHERE id = %(id)s;
        '''
        cur = self.mydb.cursor()
        try:
            cur.execute(update_query, params=update_data)
            self.mydb.commit()
        except con.Error as err:
            return err.errno
        finally:
            cur.close()
        return 0

    # insert_data sample dictionary
    # { name : 'Vaibhav', affiliation : 'UIUC', citedby : '101', pub_title : 'Article Title',
    #   pub_year : '2012', pub_url : '', journal : 'Journal Name' }

    # Return 0 on success, other error codes on failure
    def insert_article(self, insert_data):
        insert_query = '''
            INSERT INTO articles (name, affiliation, citedby, pub_title, pub_year, pub_url, journal)
            VALUES (%(name)s, %(affiliation)s, %(citedby)s, %(pub_title)s, %(pub_year)s, %(pub_url)s, %(journal)s)
        '''
        cur = self.mydb.cursor()
        try:
            cur.execute(insert_query, params=insert_data)
            self.mydb.commit()
        except con.Error as err:
            return err.errno
        finally:
            cur.close()
        return 0

    def create_articles_table(self):
        create_query = '''
            CREATE TABLE articles (
                id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
                name text,
                affiliation text,
                citedby	int,
                pub_title text,
                pub_year int,
                pub_url text,
                journal text
            );
        '''
        alter_query = '''
            ALTER TABLE articles CONVERT TO CHARACTER SET utf8
        '''
        cur = self.mydb.cursor()
        cur.execute(create_query)
        self.mydb.commit()
        cur.execute(alter_query)
        self.mydb.commit()
        cur.close()

    def load_articles_data(self, csv_path):
        with open(csv_path) as csv_file:
            csv_data = csv.reader(csv_file)
            row_count = -1
            keys = []
            for row in csv_data:
                row_count += 1
                if row_count == 0:
                    keys = row
                    continue
                data = dict(zip(keys, row))
                self.insert_article(data)

    # delete_data sample dictionary
    # { id : '101' }

    # Return 0 on success, other error codes on failure
    def delete_article(self, delete_data):
        delete_query = '''
            DElETE FROM articles WHERE id = %(id)s
        '''
        cur = self.mydb.cursor()
        try:
            cur.execute(delete_query, params=delete_data)
            self.mydb.commit()
        except con.Error as err:
            return err.errno
        finally:
            cur.close()
        return 0

    def close(self):
        self.mydb.close()

if __name__ == "__main__" :
    db = DB()
    db.create_articles_table()
    db.load_articles_data('data/articles.csv')
    db.close()
