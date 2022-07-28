from flask import Flask, redirect, url_for, render_template, request
from sqlalchemy import true; Flask(__name__)

app= Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    return render_template("index1.html")


@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == "POST":
        IP1=str(request.form['IP'])
        #print (IP1)
    return render_template("result.html",iip=IP1)


if __name__ == '__main__':
    app.run(debug = true)
