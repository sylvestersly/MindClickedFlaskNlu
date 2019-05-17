'''
The engine of the application. This contains the database fields to enable login.
A secret Key generated using python screts >> import secrets module
The function chat is the main app for the  intent-entities extraction as well as sending call-backs
When the text is input into the system information is sent RASA-NLU server using http://localhost:5000/parse.
Accordingly the response has the intent and the entities.
Depending on the intent, depression_assessment learn more will be referenced.
Responses are received to be viewed

'''

from flask import Flask
from flask import render_template, url_for, flash, redirect, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
import requests
# from models import *
from knowledge import *
import random

app = Flask(__name__)
app.secret_key = '5c4b51a3a398cbb8f7ac68d953122b09'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MCdb.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='1.jpg')
    password = db.Column(db.String(60), nullable=False)


def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.image_file}')"


@app.route('/')
def index():
    return render_template('home.html')


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    try:
        user_message = request.form["text"]
        response = requests.get("http://localhost:5000/parse", params={"q": user_message})
        response = response.json()
        print(response)
        entities = response.get("entities")
        intent = response.get("intent")
        print("Intent {}, Entities {}".format(intent['name'], entities))
        if intent['name'] == "start_assessment":
            response_text = start_assessment(entities)
        elif intent['name'] == "depression_assessment":
            response_text = depression_assessment(entities)
        elif intent['name'] == "psychosis_assessment":
            response_text = psychosis_assessment(entities)
        elif intent['name'] == "affirm":
            response_text = affirm()
        elif intent['name'] == "greet":
            response_text = greeting()
        elif intent['name'] == "goodbye":
            response_text = goodbye()
        else:
            response_text = "Sorry, can not help at this time"
        return jsonify({"status": "success", "response": response_text})
        # return 'OK'
    except Exception as e:
        print(e)
        return jsonify({"status": "success", "response": "Sorry I am not trained to do that yet..."})

        # The aim is to make have flask render the chat template and run this function
        # if request.path == '/chat':
        #     return 'chat'
        # return render_template('index.html')

@app.route("/home")
def home():
    return render_template('chat.html', title='Assessment')

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@mindclicked.com' and form.password.data == '123456789':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


app.config['DEBUG'] = True
if __name__ == "__main__":
    app.run(port=8080)
