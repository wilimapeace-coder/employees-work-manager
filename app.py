from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn


@app.route("/")
def home():
    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
    except sqlite3.OperationalError:
        employees = []

    conn.close()

    return render_template("index.html", employees=employees)


@app.route("/add", methods=["POST"])
def add_employee():
    name = request.form["name"]
    task = request.form["task"]

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            task TEXT NOT NULL
        )
    """)

    cursor.execute(
        "INSERT INTO employees (name, task) VALUES (?, ?)",
        (name, task)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:employee_id>")
def delete_employee(employee_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
