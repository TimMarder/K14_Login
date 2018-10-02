# Polish-Israeli Coding Confederacy
# Tim Marder & Damian Wasilewicz
# SoftDev1 pd06
# K #14: Do I Know You?
# 2018-10-01

#imports necessary tools from flask and os
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import redirect
import os


app = Flask(__name__)
app.secret_key = os.urandom(32) #sets secret key to 32 bits of
                                #random data as a string

#determines whether or not user is currently logged in by checking if the session
# "dictionary" has a key with appropriate username; displays welcome page if logged in,
#sends user to home to sign in if user isn't logged in
@app.route("/")
def home():
    if (session.get('username') == "timian"):
        return render_template("welcome.html",
                                user = "timian")
    else:
        return render_template("home.html")


#removes user from session, logging them out
@app.route("/logout")
def log_out():
    try:                                    # If page is open in two tabs and
        session.pop('username')             # logout is attempted on both, this
        return return_template("home.html") # prevents a crash
    except:
        return render_template("home.html")


#home page; determines whether input information is correct
#and returns welcome page if login successful, home page if not
#error page includes hint as to which part of login combo was wrong
@app.route("/auth", methods = ["POST"])
def authenticate():
    if ((request.form['username'] == "timian") &
        (request.form['password'] == "wasilarder")):
        session['username'] = "timian"
        return render_template("welcome.html",
                                user = "timian")
    elif ((request.form['username']) == "timian"):
        return render_template("error.html",
                                user = request.form['username'],
                                pwd = request.form['password'],
                                error = "Your password was incorrect")
    elif ((request.form['password']) == "wasilarder"):
        return render_template("error.html",
                                user = request.form['username'],
                                pwd = request.form['password'],
                                error = "Your username was incorrect")
    else:
        return render_template("error.html",
                                user = request.form['username'],
                                pwd = request.form['password'],
                                error = "Your password and password were both incorrect!")

if __name__ == "__main__":
    app.debug = True
    app.run()
