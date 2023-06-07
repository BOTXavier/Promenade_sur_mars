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

def get_membreData(login,mdp):
    cnx = connexion() 
    if cnx is None: return None
    
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM identification WHERE login = %s AND motPasse = %s"
        cursor.execute(sql, (login, mdp))
        listeMembre = cursor.fetchall()
        print(listeMembre)
        close_bd(cursor, cnx)
        #session['successDB'] = "OK get_membresData"
    except mysql.connector.Error as err:
        listeMembre = None
        session['errorDB'] = "Failed get membres data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return listeMembre

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
def add_membreData(nom, prenom, mail, login, motPasse, statut):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor()
        sql = "INSERT INTO identification (nom, prenom, mail, login, motPasse, statut) VALUES (%s, %s, %s, %s, %s, %s);"
        param = (nom, prenom, mail, login, motPasse, statut)
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
        return True
    except mysql.connector.Error as err:
        #session['errorDB'] = "Failed update membres data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
        return False
    

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
            sql = "INSERT INTO identification (nom, prenom, mail, login, motPasse, statut) VALUES (%s, %s, %s, %s, %s, %s);"
            param = (d['nom'], d['prenom'], d['mail'], d['login'], d['motPasse'], d['statut'])
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
            sql = "INSERT INTO Cameras (camera_id,name,rover_id,full_name,orientation_hori,orientation_verti) VALUES  (%s, %s, %s, %s, %s,%s);"
            param=(camera_id,camera['name'],camera['rover_id'],camera['full_name'], camera['orient_hori'], camera['orient_verti'])
            cursor.execute(sql,param)
            cnx.commit()
        for position_id in dico_posi:
            posi=dico_posi[position_id]
            print(position_id)
            sql = "INSERT INTO Positions (posi_id,rover_id,lat,longitude,cap,sol) VALUES  (%s, %s, %s, %s, %s,%s);"
            param=(position_id,posi['rover_id'],posi['lat'],posi['long'],posi['cap'],posi['sol'])
            cursor.execute(sql,param)
            cnx.commit()
        close_bd(cursor,cnx)
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed saveDataFromFile data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return 1

def order_data(deb,fin):
    dico_photos,dico_rovers,dico_cameras,dico_posi=bup.créer_dicos_2(deb,fin)
    saveDatafromNASA(dico_photos,dico_rovers,dico_cameras,dico_posi)

##########################################################################
### Boutons d'affichage des photos voisines de id

def bouton_droite(id):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)
        sql="SELECT sol,rover_id,camera_id FROM Photos WHERE photo_id=%s"
        param=([id])
        cursor.execute(sql,param)
        data=cursor.fetchall()
        sol,rover_id,camera_id=data[0]['sol'],data[0]['rover_id'], data[0]['camera_id'] #récuparation des données de la photo affichée

        sql="SELECT orientation_hori,orientation_verti FROM Cameras WHERE camera_id=%s"
        param=([camera_id])
        cursor.execute(sql,param)
        req=cursor.fetchall()[0]
        orient_hori,orient_verti=req['orientation_hori'],req['orientation_verti'] #orientation de la caméra de la photo affichée

        sql="SELECT camera_id, orientation_hori FROM Cameras WHERE %s>orientation_hori"
        param=([orient_hori])
        cursor.execute(sql,param)
        cameras_droite=cursor.fetchall()
        cameras_droite.sort(key = lambda cam: cam['orientation_hori'])
        camera_droite_id=cameras_droite[0]['camera_id']

        sql = "SELECT photo_id,url FROM Photos WHERE sol=%s AND rover_id=%s AND camera_id=%s"
        param=([sol,rover_id,camera_droite_id])
        cursor.execute(sql,param)
        req = cursor.fetchall()
        id_droite,url_droite=req[0]['photo_id'],req[0]['url']

        close_bd(cursor, cnx)
    except:
        session['errorDB'] = "Failed bouton_droite data"
        print(session['errorDB']) #le problème s'affiche dans le terminal
        return 0,0
    return id_droite, url_droite

def bouton_gauche(id):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT sol,rover_id,camera_id FROM Photos WHERE photo_id=%s"
        param=([id])
        cursor.execute(sql,param)
        data=cursor.fetchall()
        sol,rover_id,camera_id=data[0]['sol'],data[0]['rover_id'], data[0]['camera_id'] #récuparation des données de la photo affichée

        sql="SELECT orientation_hori,orientation_verti FROM Cameras WHERE camera_id=%s"
        param=([camera_id])
        cursor.execute(sql,param)
        req=cursor.fetchall()[0]
        orient_hori,orient_verti=req['orientation_hori'],req['orientation_verti']

        sql="SELECT camera_id, orientation_hori FROM Cameras WHERE %s<orientation_hori"
        param=([orient_hori])
        cursor.execute(sql,param)
        cameras_droite=cursor.fetchall()
        cameras_droite.sort(key = lambda cam: cam['orientation_hori'])
        camera_droite_id=cameras_droite[0]['camera_id']

        sql = "SELECT photo_id,url FROM Photos WHERE sol=%s AND rover_id=%s AND camera_id=%s"
        param=([sol,rover_id,camera_droite_id])
        cursor.execute(sql,param)
        req = cursor.fetchall()
        id_gauche,url_gauche=req[0]['photo_id'],req[0]['url']
        
        close_bd(cursor, cnx)
    except:
        session['errorDB'] = "Failed bouton_gauche data"
        print(session['errorDB']) #le problème s'affiche dans le terminal
        return 0,0
    return id_gauche, url_gauche

def bouton_haut(id):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT sol,rover_id,camera_id FROM Photos WHERE photo_id=%s"
        param=([id])
        cursor.execute(sql,param)
        data=cursor.fetchall()
        sol,rover_id,camera_id=data[0]['sol'],data[0]['rover_id'], data[0]['camera_id'] #récuparation des données de la photo affichée

        sql="SELECT orientation_hori,orientation_verti FROM Cameras WHERE camera_id=%s"
        param=([camera_id])
        cursor.execute(sql,param)
        req=cursor.fetchall()[0]
        orient_hori,orient_verti=req['orientation_hori'],req['orientation_verti']

        sql="SELECT camera_id, orientation_hori FROM Cameras WHERE orientation_verti<%s"
        param=([orient_verti])
        cursor.execute(sql,param)
        cameras_droite=cursor.fetchall()
        cameras_droite.sort(key = lambda cam: cam['orientation_hori'])
        camera_droite_id=cameras_droite[0]['camera_id']

        sql = "SELECT photo_id,url FROM Photos WHERE sol=%s AND rover_id=%s AND camera_id=%s"
        param=([sol,rover_id,camera_droite_id])
        cursor.execute(sql,param)
        req = cursor.fetchall()
        id_haut,url_haut=req[0]['photo_id'],req[0]['url']
        
        close_bd(cursor, cnx)
    except:
        session['errorDB'] = "Failed bouton_haut data"
        print(session['errorDB']) #le problème s'affiche dans le terminal
        return 0,0
    return id_haut, url_haut

def bouton_bas(id):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT sol,rover_id,camera_id FROM Photos WHERE photo_id=%s"
        param=([id])
        cursor.execute(sql,param)
        data=cursor.fetchall()
        sol,rover_id,camera_id=data[0]['sol'],data[0]['rover_id'], data[0]['camera_id'] #récuparation des données de la photo affichée
        print(sol,rover_id,camera_id)

        sql="SELECT orientation_hori,orientation_verti FROM Cameras WHERE camera_id=%s"
        param=([camera_id])
        cursor.execute(sql,param)
        req=cursor.fetchall()[0]
        orient_hori,orient_verti=req['orientation_hori'],req['orientation_verti']

        sql="SELECT camera_id, orientation_hori FROM Cameras  WHERE orientation_verti>%s"
        param=([orient_verti])
        cursor.execute(sql,param)
        cameras_droite=cursor.fetchall()
        cameras_droite.sort(key = lambda cam: cam['orientation_hori'])
        camera_droite_id=cameras_droite[0]['camera_id']

        sql = "SELECT photo_id,url FROM Photos WHERE sol=%s AND rover_id=%s AND camera_id=%s"
        param=([sol,rover_id,camera_droite_id])
        cursor.execute(sql,param)
        req = cursor.fetchall()
        id_bas,url_bas=req[0]['photo_id'],req[0]['url']
        
        close_bd(cursor, cnx)
    except:
        session['errorDB'] = "Failed bouton_bas data"
        print(session['errorDB']) #le problème s'affiche dans le terminal
        return 0,0
    return id_bas, url_bas

def bouton_avant(id):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT sol,rover_id,camera_id FROM Photos WHERE photo_id=%s"
        param=([id])
        cursor.execute(sql,param)
        data=cursor.fetchall()
        sol,rover_id,camera_id=data[0]['sol'],data[0]['rover_id'], data[0]['camera_id'] #récuparation des données de la photo affichée
        print(sol,rover_id,camera_id)

        sql="SELECT name FROM Rovers WHERE rover_id=%s"
        param=([rover_id])
        cursor.execute(sql,param)
        rover_name=cursor.fetchall()[0]['name']

        num_rover=bini.ROVER.index(rover_name.lower())
        posi_id=num_rover*(10**6)+sol

        sql="SELECT lat,longitude,cap FROM Positions WHERE posi_id=%s"
        param=([posi_id])
        cursor.execute(sql,param)
        data=cursor.fetchall()[0]
        lat,long,cap=data['lat'], data['long'], data['cap']

        sql = "SELECT photo_id,url FROM Photos WHERE rover_id=%s AND camera_id=%s AND posi_id<%s"
        param=([rover_id,camera_id,posi_id])
        cursor.execute(sql,param)
        req = cursor.fetchall()
        id_avant,url_avant = req[0]['photo_id'], req[1]['url']
        
        close_bd(cursor, cnx)
    except:
        session['errorDB'] = "Failed bouton_avant data"
        print(session['errorDB']) #le problème s'affiche dans le terminal
        return 0,0
    return id_avant, url_avant

def bouton_apres(id):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT sol,rover_id,camera_id FROM Photos WHERE photo_id=%s"
        param=([id])
        cursor.execute(sql,param)
        data=cursor.fetchall()
        sol,rover_id,camera_id=data[0]['sol'],data[0]['rover_id'], data[0]['camera_id'] #récuparation des données de la photo affichée
        print(sol,rover_id,camera_id)

        sql="SELECT name FROM Rovers WHERE rover_id=%s"
        param=([rover_id])
        cursor.execute(sql,param)
        rover_name=cursor.fetchall()[0]['name']

        num_rover=bini.ROVER.index(rover_name.lower())
        posi_id=num_rover*(10**6)+sol

        sql="SELECT lat,longitude,cap FROM Positions WHERE posi_id=%s"
        param=([posi_id])
        cursor.execute(sql,param)
        data=cursor.fetchall()[0]
        lat,long,cap=data['lat'], data['long'], data['cap']

        sql = "SELECT photo_id,url FROM Photos WHERE rover_id=%s AND camera_id=%s AND posi_id>%s"
        param=([rover_id,camera_id,posi_id])
        cursor.execute(sql,param)
        req = cursor.fetchall()
        id_apres,url_apres = req[0]['photo_id'], req[1]['url']
        
        close_bd(cursor, cnx)
    except:
        session['errorDB'] = "Failed bouton_arriere data"
        print(session['errorDB']) #le problème s'affiche dans le terminal
        return 0,0
    return id_apres, url_apres


##########################################################################
### Ajustement des angles des caméras montées sur des mats mobiles
def update_angle_cam(angles_mats, angles_sherlocks): # angles_mats=[[angle_mats_hori], [angle_mats_verti]], angles_sherlocks=[[angle_sherlocks_hori], [angle_sherlocks_verti]] dans le référentiel du rover
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT camera_id, rover_id, nom FROM Cameras"
        cursor.execute(sql)
        req=cursor.fetchall()[0]
        cameras=[]
        for cam in req: 
            cam_id,rover_id, nom=cam['camera_id'],cam['rover_id'],cam['nom']
            cameras.append([cam_id, rover_id, nom]) #liste de toutes les cameras

        for cam in cameras:
            sql="UPDATE Cameras SET orientation_hori = %s AND orientation_verti = %s WHERE camera_id = %s"
            camera_orients=bup.aligner_cams(cam[0],cam[2], cam[1],angles_mats, angles_sherlocks)
            param=[camera_orients[0], camera_orients[1], cam[0]]
            cursor.execute(sql,param)
        
        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        session['errorDB'] = "Failed saveDataFromFile data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return 1

def ajuster_cams_mats(photo_id,angles_mats,angles_sherlocks):
    cnx = connexion() 
    if cnx is None: 
        return None
    try:
        cursor = cnx.cursor(dictionary=True)

        sql="SELECT camera_id FROM Photos WHERE photo_id=%s"
        param=[photo_id]
        cursor.execute(sql,param)
        req=cursor.fetchall()[0]
        cam_id=req['camera_id']

        if cam_id in bini.LIST_CAM_MOBILES:
            update_angle_cam(angles_mats, angles_sherlocks)

    except mysql.connector.Error as err:
        session['errorDB'] = "Failed saveDataFromFile data : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return 1

#Les fonctions qui suivent servent à l'affichage des bases de données

def get_positions():
    cnx = connexion() 
    if cnx is None: return None
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM positions"
        cursor.execute(sql)
        positions = cursor.fetchall()
        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        positions = None
        session['errorDB'] = "Failed get positions : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return positions

def get_rovers():
    cnx = connexion() 
    if cnx is None: return None
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM rovers"
        cursor.execute(sql)
        rovers = cursor.fetchall()
        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        rovers = None
        session['errorDB'] = "Failed get rovers : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return rovers

def get_photos():
    cnx = connexion() 
    if cnx is None: return None
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM photos"
        cursor.execute(sql)
        photos = cursor.fetchall()
        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        photos = None
        session['errorDB'] = "Failed get rovers : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return photos

def get_cameras():
    cnx = connexion() 
    if cnx is None: return None
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM cameras"
        cursor.execute(sql)
        cameras = cursor.fetchall()
        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        cameras = None
        session['errorDB'] = "Failed get rovers : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return cameras

def latlongsol(photo_id):
    cnx = connexion() 
    if cnx is None: return None
    try:
        cursor = cnx.cursor(dictionary=True)
        
        sql = "SELECT rover_id,sol FROM photos WHERE photo_id=%s"
        params=[photo_id]
        cursor.execute(sql,params)
        data = cursor.fetchall()[0]
        rover_id,sol=data['rover_id'],data['sol']
        
        sql = "SELECT lat,longitude,sol FROM positions WHERE rover_id=%s AND sol=%s"
        params=[rover_id,sol]
        cursor.execute(sql,params)
        data = cursor.fetchall()[0]
        lat,longitude,sol=data['lat'],data['longitude'],data['sol']
        print(3,lat,longitude,sol)

        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        cameras = None
        session['errorDB'] = "Failed get rovers : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return lat,longitude,sol

def url_photoid(photo_id):
    cnx = connexion() 
    if cnx is None: return None
    try:
        cursor = cnx.cursor(dictionary=True)
        
        sql = "SELECT url FROM photos WHERE photo_id=%s"
        params=[photo_id]
        cursor.execute(sql,params)
        datas = cursor.fetchall()[0]
        url=datas['url']

        close_bd(cursor, cnx)
    except mysql.connector.Error as err:
        cameras = None
        session['errorDB'] = "Failed get rovers : {}".format(err)
        print(session['errorDB']) #le problème s'affiche dans le terminal
    return url

def recupphotoproche(lat,long):
    cnx = connexion() 
    if cnx is None: return None
    try:
        cursor = cnx.cursor(dictionary=True)
        
        sql = "SELECT sol,rover_id FROM positions WHERE lat-0.0001<=%s<=lat+0.0001 and longitude-0.0001<=%s<=longitude+0.0001"
        params=[lat,long]
        cursor.execute(sql,params)
        datas = cursor.fetchall()[0]
        sol,rover_id=datas['sol'],datas['rover_id']

        sql="SELECT url,photo_id FROM photos WHERE sol=%s AND rover_id=%s"
        params=[sol,rover_id]
        datas = cursor.fetchall()[0]
        url,id=datas['url'],datas['photo_id']

        close_bd(cursor, cnx)
    except:
        cameras = None
        session['errorDB'] = "Failed get rovers"
        print(session['errorDB']) #le problème s'affiche dans le terminal
        print('pasdephotosdanslecoin')
        return 0,0
    return url,id