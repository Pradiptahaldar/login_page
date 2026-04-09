from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

#connect to mysql server
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pradipta"
)
cursor=conn.cursor()
#home page
@app.route("/")
def home():
    return render_template("login.html")

#handling login
@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()

    if user:
        return "Login successful!"
    else:
        return "Invalid email or password."

#run the app
if __name__ == "__main__":
    app.run(debug=True)

