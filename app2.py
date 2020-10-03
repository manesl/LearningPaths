from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from send_email import send_email
from sqlalchemy import func

app = Flask(__name__) #variable to store flask object
#basically you are instantiating a Flask object
#name is a special variable that returns the name of this script called main

@app.route('/') #this is a decorator and it provides a url
def home(): #this function defines what a web page will do'
        return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/course', methods=['POST'])
def course():
    if request.method=='POST':
        email=request.form["email_name"]#grab the form element
        print(email) #for testing purpose
        password=request.form["password"]
        print(password) #for testing purpose there are two paths both are accepted home/signup->course or home/signup->login->course
        return render_template("course.html")
#all courses like datascience, ml, pic microcontrollers, web development falls here, each page has three non working buttons for beginner, inter, advanced
#only pic page first learning path button is working

@app.route('/datascience', methods=['POST'])
def datascience():
    return render_template("datascience.html")

@app.route('/ml', methods=['POST'])
def ml():
    return render_template("ml.html")

#special page
@app.route('/mc', methods=['POST'])
def mc():
    return render_template("mc.html")

@app.route('/web', methods=['POST'])
def web():
    return render_template("web.html")

#special learning path 1
@app.route('/mc_learning_path_1', methods=['POST'])
def mc_learning_path_1():
    return render_template("mc_learning_path_1.html")

if __name__ == "__main__": #when the name of this script which is main matches the __name__ defined 
    app.run(debug=True)
