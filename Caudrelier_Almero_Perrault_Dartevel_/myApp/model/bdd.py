import mysql.connector
from flask import session
from ..config import DB_SERVER

import myApp.model.bdd_update as bup
import myApp.model.bdd_initiate as bini

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
            sql = "INSERT INTO Photos (photo_id,sol,rover_id,camera_id,url) VALUES  (%s, %s, %s, %s, %s);"
            param=(photo_id,photo['sol'],photo['rover_id'],photo['camera_id'],photo['url'])
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
            sql = "INSERT INTO Cameras (camera_id,name,rover_id,full_name,orientation) VALUES  (%s, %s, %s, %s, %s);"
            param=(camera_id,camera['name'],camera['rover_id'],camera['full_name'], camera['orientation'])
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

def bouton_droite(url):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT sol,rover_id,camera_id FROM Photos WHERE url=%s"
        param=(url)
        cursor.execute(sql,param)
        data=cursor.fetchall()
        sol,rover_id,camera_id=data[0]['sol'],data[1]['rover_id'], data[2]['camera_id']
        
        sql="SELECT orient_hori FROM Cameras WHERE camera_id=%s"
        param=(camera_id)
        cursor.execute(sql,param)
        orient_hori=cursor.fetchall()[0]['orient_hori']

        sql="SELECT camera_id FROM Cameras WHERE %s>orient_hori>(%s-180)%360"
        param=(orient_hori)
        cursor.execute(sql,param)
        camera_droite_id=cursor.fetchall()[0]['camera_id']

        sql = "SELECT url FROM Photos WHERE sol=%s AND rover_id=%s AND camera_id=%s"
        param=(sol,rover_id,camera_droite_id)
        cursor.execute(sql,param)
        url_droite = cursor.fetchall()[0]['url']

        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed saveDataFromFile data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return url_droite

def bouton_gauche(url):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT sol,rover_id,camera_id FROM Photos WHERE url=%s"
        param=(url)
        cursor.execute(sql,param)
        data=cursor.fetchall()
        sol,rover_id,camera_id=data[0]['sol'],data[1]['rover_id'], data[2]['camera_id']
        
        sql="SELECT orient_hori FROM Cameras WHERE camera_id=%s"
        param=(camera_id)
        cursor.execute(sql,param)
        orient_hori=cursor.fetchall()[0]['orient_hori']

        sql="SELECT camera_id FROM Cameras WHERE %s<orient_hori<(%s-180)%360"
        param=(orient_hori)
        cursor.execute(sql,param)
        camera_gauche_id=cursor.fetchall()[0]['camera_id']

        sql = "SELECT url FROM Photos WHERE sol=%s AND rover_id=%s AND camera_id=%s"
        param=(sol,rover_id,camera_gauche_id)
        cursor.execute(sql,param)
        url_gauche = cursor.fetchall()

        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed saveDataFromFile data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return url_gauche

def bouton_haut(url):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT sol,rover_id,camera_id FROM Photos WHERE url=%s"
        param=(url)
        cursor.execute(sql,param)
        data=cursor.fetchall()
        sol,rover_id,camera_id=data[0]['sol'],data[1]['rover_id'], data[2]['camera_id']
        
        sql="SELECT orient_hori FROM Cameras WHERE camera_id=%s"
        param=(camera_id)
        cursor.execute(sql,param)
        orient_verti=cursor.fetchall()[0]['orient_hori']

        sql="SELECT camera_id FROM Cameras WHERE (%s-180)%360>orient_verti>%s"
        param=(orient_verti)
        cursor.execute(sql,param)
        camera_haute_id=cursor.fetchall()[0]['camera_id']

        sql = "SELECT url FROM Photos WHERE sol=%s AND rover_id=%s AND camera_id=%s"
        param=(sol,rover_id,camera_haute_id)
        cursor.execute(sql,param)
        url_haute = cursor.fetchall()[0]['url']

        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed saveDataFromFile data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return url_haute

def bouton_bas(url):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT sol,rover_id,camera_id FROM Photos WHERE url=%s"
        param=(url)
        cursor.execute(sql,param)
        data=cursor.fetchall()
        sol,rover_id,camera_id=data[0]['sol'],data[1]['rover_id'], data[2]['camera_id']
        
        sql="SELECT orient_hori FROM Cameras WHERE camera_id=%s"
        param=(camera_id)
        cursor.execute(sql,param)
        orient_verti=cursor.fetchall()[0]['orient_hori']

        sql="SELECT camera_id FROM Cameras WHERE (%s-180)%360<orient_verti<%s"
        param=(orient_verti)
        cursor.execute(sql,param)
        camera_bas_id=cursor.fetchall()[0]['camera_id']

        sql = "SELECT url FROM Photos WHERE sol=%s AND rover_id=%s AND camera_id=%s"
        param=(sol,rover_id,camera_bas_id)
        cursor.execute(sql,param)
        url_bas = cursor.fetchall()[0]['url']

        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed saveDataFromFile data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return url_bas

def bouton_avant(url):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT sol,rover_id,camera_id FROM Photos WHERE url=%s"
        param=(url)
        cursor.execute(sql,param)
        data=cursor.fetchall()
        sol,rover_id,camera_id=sol,rover_id,camera_id=data[0]['sol'],data[1]['rover_id'], data[2]['camera_id']

        sql="SELECT name FROM Rovers WHERE rover_id=%s"
        param=(rover_id)
        cursor.execute(sql,param)
        rover_name=cursor.fetchall()[0]['name']

        num_rover=bini.ROVER.index(rover_name.lower())
        posi_id=num_rover*(10**6)+sol

        sql="SELECT lat,lon,cap FROM Positions WHERE posi_id=%s"
        param=(posi_id)
        cursor.execute(sql,param)
        data=cursor.fetchall()
        lat,long,cap=data[0]['lat'], data[1]['long'], data[2]['cap']

        sql = "SELECT url FROM Photos WHERE rover_id=%s AND camera_id=%s AND posi_id<%s AND (lat!=%s OR long!=%s OR cap!=%s)"
        param=(rover_id,camera_id,posi_id,lat,long,cap)
        cursor.execute(sql,param)
        url_avant = cursor.fetchall()[0]['url']

        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed saveDataFromFile data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return url_avant

def bouton_apres(url):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT sol,rover_id,camera_id FROM Photos WHERE url=%s"
        param=(url)
        cursor.execute(sql,param)
        data=cursor.fetchall()
        sol,rover_id,camera_id=sol,rover_id,camera_id=data[0]['sol'],data[1]['rover_id'], data[2]['camera_id']

        sql="SELECT name FROM Rovers WHERE rover_id=%s"
        param=(rover_id)
        cursor.execute(sql,param)
        rover_name=cursor.fetchall()[0]['name']

        num_rover=bini.ROVER.index(rover_name.lower())
        posi_id=num_rover*(10**6)+sol

        sql="SELECT lat,lon,cap FROM Positions WHERE posi_id=%s"
        param=(posi_id)
        cursor.execute(sql,param)
        data=cursor.fetchall()
        lat,long,cap=data[0]['lat'], data[1]['long'], data[2]['cap']

        sql = "SELECT url FROM Photos WHERE rover_id=%s AND camera_id=%s AND posi_id>%s AND (lat!=%s OR long!=%s OR cap!=%s)"
        param=(rover_id,camera_id,posi_id,lat,long,cap)
        cursor.execute(sql,param)
        url_apres = cursor.fetchall()[0]['url']

        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed saveDataFromFile data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return url_apres
