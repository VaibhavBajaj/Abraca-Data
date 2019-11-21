from flask import Flask, render_template, request, jsonify, make_response
from mysqldb import DB
app = Flask(__name__)

@app.route('/')
def index():
    db = DB()
    table = db.search_article_by_id(20)
    return render_template('webpage.html', titles = table.columns.values)

@app.route("/postmethod", methods=["GET", "POST"])
def search() :
    print("SDFDSFDSAff")
    id = request.form['temp']
    print(id)
    db = DB()
    table = db.search_article_by_id(id)
    return render_template('webpage.html',  tables=[table.to_html(classes='data')], titles = table.columns.values)


if __name__ == '__main__':
    app.run(port=8080, debug=True)