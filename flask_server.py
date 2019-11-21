from flask import Flask, render_template, request, jsonify, make_response
from mysqldb import DB
import pandas as pd
app = Flask(__name__)

@app.route('/')
def index():
    db = DB()
    table = db.search_article_by_id(20)
    return render_template('webpage.html', titles = table.columns.values)

@app.route("/postmethod", methods=["GET", "POST"])
def search() :
    print("temp")
    if request.method == "POST" :
        print("SDFDSFDSAff")
    else :
        print("GET")
    id = request.form.get('temp')
    print(id)
    db = DB()
    table = db.search_article_by_id(id)
    if table.empty == True :
        return {"status" : "fail"}
    temp = {"status" : "sucess", "data" : table.to_html(classes = 'data')}
    return temp


if __name__ == '__main__':
    app.run(port=8080, debug=True)