from flask import Flask, render_template, redirect, request, session
from .controller import function 
from werkzeug.utils import secure_filename
import myApp.model.bdd as bdd
import myApp.config as config

app = Flask(__name__)
app.config.from_object('myApp.config')

app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'

# <Routes vers les différentes pages du site> #
@app.route("/")
def index():
    params = function.messageInfo(None)
    return render_template("index.html",**params)


@app.route("/map")
def map():
    return render_template("map.html",parameter=[round(18.444631884771205,8),round(77.45088815689088,8),0])


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


@app.route("/profil")
def profil():
    return render_template("profil.html")


@app.route("/Membres/HugoA")
def HugoA():
    return render_template("HugoA.html")


@app.route("/Membres/Louis-Yann")
def LouisYann():
    return render_template("Louis-Yann.html")


@app.route("/Membres/Xavier")
def xavier():
    return render_template("xavier.html")

@app.route("/Membres/HugoP")
def HugoP():
    return render_template("HugoP.html")


@app.route("/streetview")
def streetview():
    return render_template("streetview.html", parameter=[812589,'https://mars.nasa.gov/mars2020-raw-images/pub/ods/surface/sol/00004/ids/fdr/browse/zcam/ZRF_0004_0667303396_000FDR_N0010052AUT_04096_110085J01_1200.jpg'])

@app.route("/localisationmap/<id>")
def locmap(id=None):
    latlongsol=bdd.latlongsol(int(id))
    lat,long,sol=latlongsol[0],latlongsol[1],latlongsol[2]
    print(lat,long,sol)
    return render_template("map.html",parameter=[lat,long])

@app.route("/localisationstreet/<lat>,<long>")
def locstreet(lat=None,long=None):
    data=bdd.recupphotoproche(lat,long)
    url,id=data[0],data[1]
    if url==0 and id==0:
        return render_template("map.html",parameter=[lat,long])
    return render_template("streetview.html",parameter=[id,url])

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/data", methods=['GET'])
def data():
    deb = int(request.args.get('deb'))
    fin = int(request.args.get('fin'))
    bdd.order_data(deb,fin)
    print('succès des données')
    return render_template("streetview.html",parameter=[811204,'https://mars.nasa.gov/mars2020-raw-images/pub/ods/surface/sol/00001/ids/edr/browse/fcam/FRR_0001_0667035458_958ECM_N0010052AUT_04096_00_2I3J01_1200.jpg'])

@app.route("/photo_droite/<id>")
def photo_droite(id=None):
    angles_mats=[[0,0,0,0],[0,0,0,0]]
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    url=bdd.url_photoid(id)
    bdd.ajuster_cams_mats(id,angles_mats,angles_sherlocks) #Trouver comment déterminer les angles des mats mobiles
    id_n,url_n=bdd.bouton_droite(int(id))
    if id_n==0 and url_n==0:
        print('capassapas')
        return render_template("streetview.html", parameter=[id,url])
    return render_template("streetview.html", parameter=[id_n,url_n])

@app.route("/photo_gauche/<id>")
def photo_gauche(id=None):
    angles_mats=[[0,0,0,0],[0,0,0,0]]
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    url=bdd.url_photoid(id)
    bdd.ajuster_cams_mats(id,angles_mats,angles_sherlocks) #Trouver comment déterminer les angles des mats mobiles
    id_n,url_n=bdd.bouton_gauche(int(id))
    if id_n==0 and url_n==0:
        print('capassapas')
        return render_template("streetview.html", parameter=[id,url])
    return render_template("streetview.html", parameter=[id_n,url_n])

@app.route("/photo_haut/<id>")
def photo_haut(id=None):
    angles_mats=[[0,0,0,0],[0,0,0,0]]
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    url=bdd.url_photoid(id)
    bdd.ajuster_cams_mats(id,angles_mats,angles_sherlocks) #Trouver comment déterminer les angles des mats mobiles
    id_n,url_n=bdd.bouton_haut(int(id))
    if id_n==0 and url_n==0:
        print('capassapas')
        return render_template("streetview.html", parameter=[id,url])
    return render_template("streetview.html", parameter=[id_n,url_n])

@app.route("/photo_bas/<id>")
def photo_bas(id=None):
    angles_mats=[[0,0,0,0],[0,0,0,0]]
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    url=bdd.url_photoid(id)
    bdd.ajuster_cams_mats(id,angles_mats,angles_sherlocks) #Trouver comment déterminer les angles des mats mobiles
    id_n,url_n=bdd.bouton_bas(int(id))
    if id_n==0 and url_n==0:
        print('capassapas')
        return render_template("streetview.html", parameter=[id,url])
    return render_template("streetview.html", parameter=[id_n,url_n])

@app.route("/photo_devant/<id>")
def photo_devant(id=None):
    angles_mats=[[0,0,0,0],[0,0,0,0]]
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    url=bdd.url_photoid(id)
    bdd.ajuster_cams_mats(id,angles_mats,angles_sherlocks) #Trouver comment déterminer les angles des mats mobiles
    id_n,url_n=bdd.bouton_apres(int(id))
    if id_n==0 and url_n==0:
        print('capassapas')
        return render_template("streetview.html", parameter=[id,url])
    return render_template("streetview.html", parameter=[id_n,url_n])

@app.route("/photo_derriere/<id>")
def photo_derriere(id=None):
    angles_mats=[[0,0,0,0],[0,0,0,0]]
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    url=bdd.url_photoid(id)
    bdd.ajuster_cams_mats(id,angles_mats,angles_sherlocks) #Trouver comment déterminer les angles des mats mobiles
    id_n,url_n=bdd.bouton_avant(int(id))
    if id_n==0 and url_n==0:
        print('capassapas')
        return render_template("streetview.html", parameter=[id,url])
    return render_template("streetview.html", parameter=[id_n,url_n])

# <Routes des différents outils utiles à la gestion de compte> #
@app.route("/login")
def login():
    params = function.messageInfo(None)
    return render_template("login.html",**params)

# ajout d'un membre
@app.route("/addMembre", methods=['POST'])
def addMembre():
    nom = request.form['nom']
    prenom = request.form['prenom']
    mail = request.form['mail']
    login = request.form['login']
    motPasse = request.form['mdp']
    statut = request.form['statut']
    code_admin = request.form['code_admin']
    lastId = bdd.add_membreData(nom, prenom, mail, login, motPasse, statut, code_admin)
    print(lastId)  # dernier id créé par la BDD
    if "errorDB" not in session:    
        session["infoVert"] = "Nouveau membre inséré"
    else:
        session["infoRouge"] = "Problème ajout utilisateur"
    return redirect("/login")


@app.route('/connecter', methods=['POST'])
def connecter():
    """
    vérifie si les informations des champs sont cohérentes avec la bdd, et connecte l'utilisateur, le cas échéant
    """
    login = request.form['login']
    motPasse = request.form['mdp']
    user = bdd.verifAuthData(login,motPasse)
    if user == None:
        session["infoRouge"]="Authentification refusée"
        return redirect("/login")
        
    else:
        data = bdd.get_membreData(login,motPasse)[0]
        session["login"] = data["login"]
        session["nom"] = data["nom"]
        session["prenom"]= data["prenom"]
        session["idUser"] = data["idUser"]
        session["statut"] = data["statut"]
        session['mdp'] = motPasse
        session["infoVert"]="Authentification réussie"
        return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    session["infoBleu"] = "Vous êtes déconnecté, merci de votre visite"
    params = function.messageInfo(None)
    return render_template("index.html",**params)

#routes pour afficher le contenu des bases de données


@app.route("/Photos_range", methods=['GET'])
def Photos_range():
    start = int(request.args.get('start'))
    end = int(request.args.get('end'))
    L = []
    dictionnaires = bdd.get_photos()
    for dictionnaire in dictionnaires :
        L.append([dictionnaire['photo_id'], dictionnaire['sol'], dictionnaire['rover_id'], dictionnaire['camera_id'], dictionnaire['url']])
    return render_template("Photos.html", liste_de_listes = L[start:end])



@app.route("/delete")
def delete():
    """
    Supprime un utilisateur de la base de donnée
    """
    idUser = session["idUser"]
    bdd.del_membreData(idUser)
    print(idUser)
    # la suppression a bien fonctionné
    if "errorDB" not in session:
        session["infoVert"] = "L'utilisateur a bien été supprimé"
        session.clear()
    else:
        session["infoRouge"] = "Problème suppression utilisateur"
    return redirect("/login")


@app.route('/updatepassword', methods=['POST'])
def update_password():
    idUser = session['idUser']  # ID de l'utilisateur
    ancienmdp = request.form.get('mdp')
    if ancienmdp == session['mdp']:

        newvalue = request.form.get('newmdp')  # Nouvelle valeur du champ
        newvalueConfirm = request.form.get('newmdpconfirm')  # Nouvelle valeur du champ

        if newvalue == newvalueConfirm:
            # Appel de la fonction pour mettre à jour la base de données
            result = bdd.update_membreData("motPasse", idUser, newvalue)
            
            if result:
                # La mise à jour a réussi
                session["infoVert"] = 'Mot de passe mis à jour avec succès.'
            else:
                # La mise à jour a échoué
                session["infoRouge"] =  'Échec de la mise à jour du mot de passe.'
        else : 
            session["infoRouge"] =  'Les mots de passe de sont pas identiques'
    
    else:
        session["infoRouge"] =  'Mot de passe incorrect'
    
    params = function.messageInfo(None)
    
    return render_template("profil.html",**params)


# <Routes des différents outils utiles à la gestion des photos et de la carte> #  

# <Routes pour afficher le contenu des bases de données> #

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


@app.route("/visubdd") 
def visu():
    return render_template("VisuBDD.html")
