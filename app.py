from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# connect to mysql
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pradipta"
)
cursor = conn.cursor()

# ---------------- HOME (LOGIN PAGE) ----------------
@app.route("/")
def home():
    return render_template("login.html")


# ---------------- SIGNUP (GET + POST in ONE route) ----------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])   # convert to int
        phone = request.form["phone"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            cursor.execute(
                "INSERT INTO users (name, age, phone, email, password) VALUES (%s, %s, %s, %s, %s)",
                (name, age, phone, email, password)
            )
            conn.commit()
            print("Inserted successfully")

        except Exception as e:
            print("Error:", e)

        return redirect("/")

    return render_template("signup.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    cursor.execute(
        "SELECT * FROM users WHERE email = %s AND password = %s",
        (email, password)
    )
    user = cursor.fetchone()

    if user:
        return "Login successful!"
    else:
        return "Invalid email or password."


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
