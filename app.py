from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")



@app.route("/all")
def all():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    customers = c.execute("SELECT * from customer").fetchall()

    conn.close()

    return render_template("all.html", customers=customers)


@app.route("/one/<int:number>")
def one(number):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    customer = c.execute("SELECT * from customer WHERE number=?", (number,)).fetchone()

    conn.close()

    return render_template("all.html", customers=(customer,))


@app.route("/create", methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        number = request.form['number']
        surname = request.form['surname']

        c.execute("INSERT INTO customer VALUES(?,?)", (number, surname))

        conn.commit()

        conn.close()

        return render_template("index.html")

    else:

        return render_template("create.html")


@app.route("/update/<int:number>/<string:surname>", methods=("GET", "POST"))
def update(number, surname):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("UPDATE customer SET surname=? WHERE number=?", (surname, number))

    conn.commit()

    conn.close()

    return render_template("index.html")

