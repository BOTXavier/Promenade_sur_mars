from flask import Flask, render_template, redirect, request, session
from .controller import function 
from werkzeug.utils import secure_filename
import myApp.model.bdd as bdd
import myApp.config as config

app = Flask(__name__)
app.config.from_object('myApp.config')

app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def index():
    params = function.messageInfo(None)
    return render_template("index.html",**params)


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
    params = function.messageInfo(None)
    return render_template("login.html",**params)

@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/logout")
def logout():
    session.clear()
    session["infoBleu"] = "Vous êtes déconnecté. Merci de votre visite"
    params = function.messageInfo(None)
    return render_template('/index.html', **params)

@app.route("/profil")
def profil():
    return render_template("profil.html")


@app.route("/streetview")
def streetview():
    return render_template("streetview.html", parameter=[811204,'https://mars.nasa.gov/mars2020-raw-images/pub/ods/surface/sol/00001/ids/edr/browse/fcam/FRR_0001_0667035458_958ECM_N0010052AUT_04096_00_2I3J01_1200.jpg'])

@app.route("/Membres/HugoA")
def HugoA():
    return render_template("HugoA.html")

@app.route("/Membres/Louis-Yann")
def LouisYann():
    return render_template("Louis-Yann.html")

@app.route("/Membres/Xavier")
def xavier():
    return render_template("xavier.html")


@app.route("/data")
def data():
    bdd.order_data()
    print('succès des données')
    return render_template("streetview.html")

@app.route("/photo_droite/<id>")
def photo_droite(id=None):
    angles_mats=[[0,0,0,0],[0,0,0,0]]
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    bdd.ajuster_cams_mats(id,angles_mats,angles_sherlocks) #Trouver comment déterminer les angles des mats mobiles
    id,url=bdd.bouton_droite(int(id))
    return render_template("streetview.html", parameter=[id,url])

@app.route("/photo_gauche/<id>")
def photo_gauche(id=None):
    angles_mats=[[0,0,0,0],[0,0,0,0]]
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    bdd.ajuster_cams_mats(id,angles_mats,angles_sherlocks) #Trouver comment déterminer les angles des mats mobiles
    id,url=bdd.bouton_gauche(int(id))
    return render_template("streetview.html", parameter=[id,url])

@app.route("/photo_haut/<id>")
def photo_haut(id=None):
    angles_mats=[[0,0,0,0],[0,0,0,0]]
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    bdd.ajuster_cams_mats(id,angles_mats,angles_sherlocks) #Trouver comment déterminer les angles des mats mobiles
    id,url=bdd.bouton_haute(int(id))
    return render_template("streetview.html", parameter=[id,url])

@app.route("/photo_bas/<id>")
def photo_bas(id=None):
    angles_mats=[[0,0,0,0],[0,0,0,0]]
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    bdd.ajuster_cams_mats(id,angles_mats,angles_sherlocks) #Trouver comment déterminer les angles des mats mobiles
    id,url=bdd.bouton_bas(int(id))
    return render_template("streetview.html", parameter=[id,url])

@app.route("/photo_devant/<id>")
def photo_devant(id=None):
    angles_mats=[[0,0,0,0],[0,0,0,0]]
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    bdd.ajuster_cams_mats(id,angles_mats,angles_sherlocks) #Trouver comment déterminer les angles des mats mobiles
    id,url=bdd.bouton_devant(int(id))
    return render_template("streetview.html", parameter=[id,url])

@app.route("/photo_derriere/<id>")
def photo_derriere(id=None):
    angles_mats=[[0,0,0,0],[0,0,0,0]]
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    bdd.ajuster_cams_mats(id,angles_mats,angles_sherlocks) #Trouver comment déterminer les angles des mats mobiles
    id,url=bdd.bouton_derriere(int(id))
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
        session["infoRouge"]="Authentification refusée"
        return redirect("/login")
        
    else:
        print("Bienvenue, jeune utilisateur")
        data = bdd.get_membreData(login,motPasse)[0]
        session["login"] = data["login"]
        session["nom"] = data["nom"]
        session["prenom"]= data["prenom"]
        session["idUser"] = data["idUser"]
        session["statut"] = data["statut"]
        session["infoVert"]="Authentification réussie"
        return redirect("/")


#routes pour afficher le contenu des bases de données

@app.route("/Cameras")
def Cameras():
    L = []
    dictionnaires = bdd.get_cameras()
    for dictionnaire in dictionnaires :
        L.append([dictionnaire['camera_id'], dictionnaire['name'], dictionnaire['rover_id'], dictionnaire['full_name'], dictionnaire['orientation_hori'], dictionnaire['orientation_verti']])
    return render_template("Cameras.html", liste_de_listes = L)

@app.route("/Photos")
def Photos():
    L = []
    dictionnaires = bdd.get_photos()
    for dictionnaire in dictionnaires :
        L.append([dictionnaire['photo_id'], dictionnaire['sol'], dictionnaire['rover_id'], dictionnaire['camera_id'], dictionnaire['url']])
    return render_template("Photos.html", liste_de_listes = L[0:10])

@app.route("/Photos_range", methods=['GET'])
def Photos_range():
    start = int(request.args.get('start'))
    end = int(request.args.get('end'))
    L = []
    dictionnaires = bdd.get_photos()
    for dictionnaire in dictionnaires :
        L.append([dictionnaire['photo_id'], dictionnaire['sol'], dictionnaire['rover_id'], dictionnaire['camera_id'], dictionnaire['url']])
    return render_template("Photos.html", liste_de_listes = L[start:end])

@app.route("/Rovers")
def Rovers():
    L = [] 
    dictionnaires = bdd.get_rovers()
    for dictionnaire in dictionnaires :
        L.append([dictionnaire['rover_id'], dictionnaire['name'], dictionnaire['landing_date'], dictionnaire['launch_date'], dictionnaire['status']])
    return render_template("Rovers.html", liste_de_listes = L)

@app.route("/rovers-positions") #correspond à la table positions
def rovers_positions():
    L = [] 
    dictionnaires = bdd.get_positions()
    for dictionnaire in dictionnaires :
        L.append([dictionnaire['posi_id'], dictionnaire['rover_id'], dictionnaire['lat'], dictionnaire['longitude'], dictionnaire['cap']])
    return render_template("rovers-positions.html", liste_de_listes = L)


@app.route("/delete")
def delete():
    idUser = request.args.get("userDel")
    bdd.del_membreData(idUser)
    # la suppression a bien fonctionné
    if "errorDB" not in session:
        session["infoVert"] = "L'utilisateur a bien été supprimé"
    else:
        session["infoRouge"] = "Problème suppression utilisateur"
    return redirect("/login")