from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('preguntas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS preguntas
                 (nombre TEXT, p1 TEXT, r1 TEXT, p2 TEXT, r2 TEXT)''')
    conn.commit()
    conn.close()

@app.route("/", methods=["GET","POST"])
def index():
    conn = sqlite3.connect('preguntas.db')
    c = conn.cursor()

    if request.method == "POST":
        nombre = request.form["nombre"]
        p1 = request.form["p1"]
        r1 = request.form["r1"]
        p2 = request.form["p2"]
        r2 = request.form["r2"]

        c.execute("SELECT * FROM preguntas WHERE nombre=?", (nombre,))
        existe = c.fetchone()

        if not existe:
            c.execute("INSERT INTO preguntas VALUES (?,?,?,?,?)",(nombre,p1,r1,p2,r2))
            conn.commit()

    c.execute("SELECT * FROM preguntas")
    data = c.fetchall()

    conn.close()

    return render_template("index.html",data=data)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)