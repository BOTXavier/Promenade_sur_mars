import mysql.connector
from flask import session
from ..config import DB_SERVER

import myApp.model.bdd_update as bup

###################################################################################
# connexion au serveur de la base de données

def connexion():
    try:
        cnx = mysql.connector.connect(**DB_SERVER)
        return cnx
    except mysql.connector.Error as err:
        session['errorDB'] = format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
        return None
    
#################################################################################
# fermeture de la connexion au serveur de la base de données

def close_bd(cursor, cnx):
    cursor.close()
    cnx.close()
       

#################################################################################
# Retourne les données de la table identification
def get_membresData():
    cnx = connexion() 
    if cnx is None: return None
    
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM identification"
        cursor.execute(sql)
        listeMembres = cursor.fetchall()
        close_bd(cursor, cnx)
        #session['successDB'] = "OK get_membresData"
    except mysql.connector.Error as err:
        listeMembres = None
        session['errorDB'] = "Failed get membres data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return listeMembres

#################################################################################
#suppression d'un membre
def del_membreData(idUser):
    cnx = connexion()
    if cnx is None: return None
    try:
        cursor = cnx.cursor()
        sql = "DELETE FROM identification WHERE idUser=%s;"
        param = (idUser,)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        #session['successDB'] = "OK del_membreData"
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed del membres data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return 1

#################################################################################
#ajout d'un membre
def add_membreData(nom, prenom, mail, login, motPasse, statut, avatar):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor()
        sql = "INSERT INTO identification (nom, prenom, mail, login, motPasse, statut, avatar) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        param = (nom, prenom, mail, login, motPasse, statut, avatar)
        cursor.execute(sql, param)
        lastId = cursor.lastrowid  # récupère le dernier idUser, généré par le serveur sql
        cnx.commit()
        close_bd(cursor, cnx)
        #session['successDB'] = "OK add_membreData"
    except mysql.connector.Error as err:
        lastId = None
        session['errorDB'] = "Failed add membres data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return lastId

#################################################################################
#modification d'une donnée dans la table identification
def update_membreData(champ, idUser, newvalue):
    cnx = connexion() 
    if cnx is None: return None
    
    try:
        cursor = cnx.cursor()
        sql = "UPDATE identification SET "+champ+" = %s WHERE idUser = %s;"
        param = (newvalue, idUser)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        #session['successDB'] = "OK update_membreData"
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed update membres data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return 1

#################################################################################
#authentification des utilisateurs
def verifAuthData(login, mdp):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM identification WHERE login=%s and motPasse=%s"
        param=(login, mdp)
        cursor.execute(sql, param)
        user = cursor.fetchone()
        close_bd(cursor, cnx)
        #session['successDB'] = "OK verifAuthData"
    except mysql.connector.Error as err:
        user = None
        session['errorDB'] = "Failed verif Auth data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return user

##########################################################################
###  enregistrement des données provenant du fichier excel
def saveDataFromFile(data):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor()
        # suppression des données précédentes
        sql1 = "TRUNCATE TABLE identification;"
        cursor.execute(sql1)
        # insertion des nouvelles données
        for d in data:
            sql = "INSERT INTO identification (nom, prenom, mail, login, motPasse, statut, avatar) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            param = (d['nom'], d['prenom'], d['mail'], d['login'], d['motPasse'], d['statut'], d['avatar'])
            cursor.execute(sql, param)
            cnx.commit()
        close_bd(cursor, cnx)
        #session['successDB'] = "OK saveDataFromFile"
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed saveDataFromFile data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return 1

#Ajout d'une photo à la table photos
def add_photo(id_photo, sol, rover, camera, lien):
    cnx = connexion()
    if cnx is None: return None
    try:
        cursor = cnx.cursor()
        sql = "INSERT INTO photos (id_photo, sol, rover, camera, url) VALUES (%s, %s, %s, %s, %s)"
        param = (id_photo, sol, rover, camera, lien)
        cursor.execute(sql, param)
        lastId = cursor.lastrowid # dernier idUser généré
        cnx.commit()
        close_bd(cursor, cnx)
        #session['successDB'] = "OK add_membreData"
    except mysql.connector.Error as err:
        lastId = None
        session['errorDB'] = "Failed add membres data : {}".format(err)
    return lastId

##########################################################################
### enregistrement des données de la NASA dans la base de données
def saveDatafromNASA(dico_photos,dico_rovers,dico_cameras,dico_posi):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor()
        # insertion des données
        for photo_id in dico_photos:
            photo=dico_photos[photo_id]
            sql = "INSERT INTO Photos (photo_id,sol,rover,camera,url) VALUES  (%s, %s, %s, %s);"
            param=(photo_id,photo['sol'],photo['rover_id'],photo['camera_id'],photo['lien_img'])
            cursor.execute(sql,param)
            cnx.commit()
        for rover_id in dico_rovers:
            rover=dico_rovers[rover_id]
            sql = "INSERT INTO Rovers (rover_id,name,landing_date,launch_date,status) VALUES  (%s, %s, %s, %s, %s);"
            param=(rover_id,rover['name'],rover['landing_date'],rover['launch_date'],rover['status'])
            cursor.execute(sql,param)
            cnx.commit()
        for camera_id in dico_cameras:
            camera=dico_cameras[camera_id]
            sql = "INSERT INTO Cameras (camera_id,name,rover_id,full_name) VALUES  (%s, %s, %s, %s);"
            param=(camera_id,camera['name'],camera['rover_id'],camera['full_name'])
            cursor.execute(sql,param)
            cnx.commit()
        for position_id in dico_posi:
            posi=dico_posi[position_id]
            sql = "INSERT INTO Positions (posi_id,rover_id,lat,long,cap) VALUES  (%s, %s, %s, %s, %s);"
            param=(position_id,posi['rover_id'],posi['lat'],posi['long'],posi['cap'])
            cursor.execute(sql,param)
            cnx.commit()
        close_bd(cursor,cnx)
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed saveDataFromFile data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return 1

def order_data():
    dico_photos,dico_rovers,dico_cameras,dico_posi=bup.créer_dicos()
    saveDatafromNASA(dico_photos,dico_rovers,dico_cameras,dico_posi)