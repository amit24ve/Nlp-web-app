from flask import Flask,render_template,request
from db import Database

app = Flask(__name__)

dbo=Database()
@app.route('/')
def index():
    return render_template("login.html")
@app.route('/register')
def register():
    return render_template("register.html")
@app.route('/perform_operation', methods=['post'])
def perform_operation():
    name=request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response=dbo.insert(name,email,password)
    if response:
        return render_template("login.html",message="Registration Succesfully! Kindly login")
    else:
        return "email already exists"
app.run(debug=True)