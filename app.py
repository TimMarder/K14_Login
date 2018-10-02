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
app.secret_key = os.urandom(32)

@app.route("/")
def home():
    if (session.get('username') == "timian"):
        return render_template("welcome.html",
                                user = "timian")
    else:
        return render_template("home.html")



@app.route("/logout")
def log_out():
    session.pop('username')
    return redirect(url_for("home"))



@app.route("/auth", methods = ["GET", "POST"])
def authenticate():
    if ((request.form['username'] == "timian") &
        (request.form['password'] == "wasilarder")):
        session['username'] = "timian"
        return render_template("welcome.html",
                                user = "timian")
    else:
        return render_template("error.html",
                                user = request.form['username'],
                                pwd = request.form['password'])
    #return render_template("auth.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
