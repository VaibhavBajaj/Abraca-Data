from flask import Flask, render_template, request, jsonify
import json
from mysqldb import DB
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route("/insert", methods=["POST"])
def insert() :
    db = DB()
    insert_data = json.loads(request.form.get('data'))
    status = db.insert_article(insert_data)
    db.close()
    return jsonify({"code" : status})

@app.route("/update", methods=["POST"])
def update() :
    db = DB()
    update_data = json.loads(request.form.get('data'))
    status = db.update_article(update_data)
    db.close()
    return jsonify({"code": status})

@app.route("/query", methods=["POST"])
def query() :
    db = DB()
    query_data = json.loads(request.form.get('data'))
    args = list(query_data.values())
    table = db.query_article(*args)
    db.close()
    if table.empty:
        return jsonify({"code": -1})
    return jsonify({"code": 0, "data": table.to_html(classes = 'data')})

@app.route("/delete", methods=["POST"])
def delete() :
    db = DB()
    delete_data = json.loads(request.form.get('data'))
    print(delete_data)
    status = db.delete_article(delete_data)
    db.close()
    return jsonify({"code": status})


if __name__ == '__main__':
    app.run(port=8080, debug=True)