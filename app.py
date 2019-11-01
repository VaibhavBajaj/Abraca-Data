from mysqldb import DB

db = DB()
db.load_articles_data('data/AllArticles.csv')
db.close()