from flask import Flask, render_template, request, jsonify
from mysqldb import DB
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route("/insert", methods=["POST"])
def insert() :
    db = DB()
    insert_data = request.form.get('data')
    status = db.insert_article(insert_data)
    db.close()
    return jsonify({"code" : status})

@app.route("/update", methods=["POST"])
def update() :
    db = DB()
    update_data = request.form.get('data')
    status = db.update_article(update_data)
    db.close()
    if status == 200:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure"})

@app.route("/query", methods=["POST"])
def query() :
    # id = request.form.get('temp')
    # db = DB()
    # if table.empty == True :
    #     return {"status" : "fail"}
    # temp = {"status" : "success", "data" : table.to_html(classes = 'data')}
    # return jsonify(temp)
    pass

@app.route("/delete", methods=["POST"])
def delete() :
    db = DB()
    delete_data = request.form.get('data')
    print(delete_data)
    status = db.delete_article(delete_data)
    db.close()
    if status == 200:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure"})


if __name__ == '__main__':
    app.run(port=8080, debug=True)