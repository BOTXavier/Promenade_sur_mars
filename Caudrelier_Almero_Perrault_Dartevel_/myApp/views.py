from flask import Flask, render_template, redirect, request, session
from .controller import function as f
from .model import bdd
from werkzeug.utils import secure_filename
import myApp.model.bdd as bdd

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
  session.clear()
  return redirect('/login')


@app.route("/streetview")
def streetview():
    return render_template("streetview.html")

@app.route("/data")
def data():
    bdd.order_data()
    print('succès des données')
    return render_template("streetview.html")

@app.route("/photo_droite")
def photo_droite():
    url = bdd.bouton_droite()
    print('succès droite')
    print (url[0]['url'])
    return render_template("streetview.html")

@app.route("/photo_gauche")
def photo_gauche():
    
    print('succès gauche')
    return render_template("streetview.html")

@app.route("/photo_haut")
def photo_haut():
    
    print('succès haut')
    return render_template("streetview.html")

@app.route("/photo_bas")
def photo_bas():
    
    print('succès bas')
    return render_template("streetview.html")

@app.route("/photo_devant")
def photo_devant():
    
    print('succès devant')
    return render_template("streetview.html")

@app.route("/photo_derriere")
def photo_derriere():
    
    print('succès derriere')
    return render_template("streetview.html")


# ajout d'un membre
@app.route("/addMembre", methods=['POST'])
def addMembre():
    nom = request.form['nom']
    prenom = request.form['prenom']
    mail = request.form['mail']
    login = request.form['login']
    motPasse = request.form['mdp']
    statut = request.form['statut']
    lastId = bdd.add_membreData(nom, prenom, mail, login, motPasse, statut)
    print(lastId)  # dernier id créé par la BDD
    if "errorDB" not in session:    
        session["infoVert"] = "Nouveau membre inséré"
    else:
        session["infoRouge"] = "Problème ajout utilisateur"
    return redirect("/login")


@app.route('/connecter', methods=['POST'])
def connecter():
    login = request.form['login']
    motPasse = request.form['mdp']
    user = bdd.verifAuthData(login,motPasse)
    if user == None:
        print("Les informations ne correspondent pas à notre base de donnée")
        return redirect("/login")
        
    else:
        print("Bienvenue, jeune utilisateur")
        session["login"] = login
        return redirect("/")

