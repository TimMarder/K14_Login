# Polish-Israeli Coding Confederacy
# Tim Marder & Damian Wasilewicz
# SoftDev1 pd06
# K #15 -- Oh yes, perhaps I do…
# 2018-10-03

#imports necessary tools from flask and os
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
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
        flash("You are already logged in! Redirecting to Welcome page!")
        #shows this message to the user when he opens the page while logged in
        return render_template("welcome.html",
                                user = "timian")
    else:
        return render_template("home.html")


#removes user from session, logging them out
@app.route("/logout")
def log_out():
    flash("Successfully logged out!") #lets the user know that logging out was a success
    try:                                    # If page is open in two tabs and
        session.pop('username')             # logout is attempted on both, this
        return return_template("home.html") # prevents a crash
    except:
        return render_template("home.html")


#home page; determines whether input information is correct
#and returns welcome page if login successful but stays
#on the home page if login failed and a detailed message
#is shown to the user
@app.route("/auth", methods = ["POST"])
def authenticate():
    if ((request.form['username'] == "timian") &
        (request.form['password'] == "wasilarder")):
        session['username'] = "timian"
        return render_template("welcome.html",
                                user = "timian")
    elif ((request.form['username']) == "timian"):
        flash("Incorrent Password. Try Again!")
        return render_template("home.html")
    elif ((request.form['password']) == "wasilarder"):
        flash("Incorrent Username. Try Again!")
        return render_template("home.html")
    else:
        flash("Incorrent Username & Password. Try Again!")
        return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
