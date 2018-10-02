# Tim Marder
# SoftDev1 pd06
# K#13 -- Echo Echo Echo
# 2018-09-28

from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import redirect
import os


app = Flask(__name__)

@app.route("/")
def hello_world():
    if (session.get('username') == "peglegs"):
        return redirect(url_for("login_success"))
    else:
        print(app)
        print(request)
        print(request.args)
        print(request.headers)
        return render_template("home.html",
                                username = request.cookies.get('username'),
                                password = request.cookies.get('password'),
                                user = "peglegs",
                                pwd = "oxana")



@app.route("/loginsuccess")
def login_success():
    session['username'] = "peglegs"
    return render_template("welcome.html",
                            username = request.cookies.get('username'),
                            password = request.cookies.get('password'),
                            user = "peglegs",
                            pwd = "oxana")

@app.route("/logout")
def log_out():
    session.pop('username')
    return redirect(url_for("hello_world"))

@app.route("/loginfail")
def login_fail():
    return render_template("error.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/auth", methods = ["GET", "POST"])
def authenticate():
    if ((request.form['username'] == "peglegs") & (request.form['password'] == "oxana")):
        return redirect(url_for("login_success"))
    else:
        return redirect(url_for("login_fail"))
    #return render_template("auth.html")

if __name__ == "__main__":
    app.debug = True
    app.config['SECRET_KEY'] = os.urandom(32)
    app.run()
