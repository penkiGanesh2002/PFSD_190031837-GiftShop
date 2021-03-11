from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Employee(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    e_email = db.Column(db.String(20), nullable=False)
    e_password = db.Column(db.String(25), nullable=False)


class Customer(db.Model):
    ct_id = db.Column(db.Integer, primary_key=True)
    ct_name = db.Column(db.String(20), nullable=False)
    ct_product = db.Column(db.String(25), nullable=False)
    ct_email = db.Column(db.String(30), nullable=False)


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html', title='Home')


@app.route('/login')
def login():
    return render_template('login.html', title='Login')


@app.route('/view')
def view():
    c = Employee.query.filter_by(e_id=2)
    return render_template('view.html', title='View', data1=Employee.query.all(), data2=Customer.query.all(), c=c)

