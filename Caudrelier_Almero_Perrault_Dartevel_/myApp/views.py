from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config.from_object('myApp.config')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sgbd")
def membres():
    return render_template("sgbd.html")

@app.route("/elements")
def elements():
    return render_template("elements.html")

@app.route("/left-sidebar")
def leftsidebar():
    return render_template("left-sidebar.html")

@app.route("/right-sidebar")
def rightsidebar():
    return render_template("right-sidebar.html")

@app.route("/no-sidebar")
def nosidebar():
    return render_template("no-sidebar.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
  return redirect('/login')

@app.route("/streetview")
def streetview():
    return render_template("streetview.html")