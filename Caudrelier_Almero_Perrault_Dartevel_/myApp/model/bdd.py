import mysql.connector
from flask import session
from ..config import DB_SERVER

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
    
