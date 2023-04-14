from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object('myApp.config')
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/sgbd")
def membres():
    return render_template("sgbd.html")
@app.route("/fichiers")
def index():
    return render_template("fichiers.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/logout")
def logout():
  #  return redirect('/login')