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
    return render_template("streetview.html", parameter=[811204,'https://mars.nasa.gov/mars2020-raw-images/pub/ods/surface/sol/00001/ids/edr/browse/fcam/FRR_0001_0667035458_958ECM_N0010052AUT_04096_00_2I3J01_1200.jpg'])

@app.route("/data")
def data():
    bdd.order_data()
    print('succès des données')
    return render_template("streetview.html")

@app.route("/photo_droite/<id>")
def photo_droite(id=None):
    id,url=bdd.bouton_droite(id)
    print('succès droite')
    print (url[0]['url'])
    return render_template("streetview.html", parameter=[id,url])

@app.route("/photo_gauche/<id>")
def photo_gauche(id_prec):
    id,url=bdd.bouton_gauche(id_prec)
    print(url)
    print('succès gauche')
    return render_template("streetview.html", parameter=[id,url])

@app.route("/photo_haut/<id>")
def photo_haut(id_prec):
    id,url=bdd.bouton_haute(id_prec)
    print(url)
    print('succès haut')
    return render_template("streetview.html", parameter=[id,url])

@app.route("/photo_bas/<id>")
def photo_bas(id_prec):
    id,url=bdd.bouton_bas(id_prec)
    print(url)
    print('succès bas')
    return render_template("streetview.html", parameter=[id,url])

@app.route("/photo_devant/<id>")
def photo_devant(id_prec):
    id,url=bdd.bouton_devant(id_prec)
    print(url)
    print('succès devant')
    return render_template("streetview.html", parameter=[id,url])

@app.route("/photo_derriere/<id>")
def photo_derriere(id_prec):
    id,url=bdd.bouton_derriere(id_prec)
    print(url,id)
    print('succès derriere')
    return render_template("streetview.html", parameter=[id,url])


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

