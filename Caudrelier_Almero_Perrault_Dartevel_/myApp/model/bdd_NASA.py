import urllib.request
import json
import time

###################################################################################

# Construit les dictionnaires bien rangés des données des photos, pour toutes les photos
# ATTENTION : boucle de temps avec une pause de une heure pour ne pas trop en demander à l'API NASA

###################################################################################

ROVER=['perseverance','curiosity','spirit','opportunity']
API_KEY=['uFPg2xAvVYtXreHwgx9swNodGOnuqRCsqRX426T6','09r9lOKEqz9yGsPK6iiKDFFKRBLEvl7ZQKXyNaoS']
LIENS_POSI=['https://mars.nasa.gov/mmgis-maps/M20/Layers/json/M20_waypoints.json','https://mars.nasa.gov/mmgis-maps/MSL/Layers/json/MSL_waypoints.json'] # A ordonner dans le même ordre que ROVER

dico_photos={}
dico_rover={}
dico_camera={}
dico_posi={}

def réordonnencement(fichier):
    data=fichier.read().decode('utf-8')
    liste_data=eval(data)["photos"] # Conversion de la chaine de caractère en la liste de dictionnaires de chaques photos
    for photos in liste_data:
        rover=photos['rover']
        rover_id=rover['id']
        camera=photos['camera']
        camera_id=camera['id']
        dico_photos[photos['id']]={'sol':photos['sol'],'rover':rover_id,'camera':camera_id,'lien_img':photos['img_src']}
        if rover_id not in dico_rover:
            rover.pop('id')
            dico_rover[rover_id]=rover
        if camera_id not in dico_camera:
            camera.pop('id')
            dico_camera[camera_id]=camera
            
def check_NASA(compt_req,rover,sol,compt_api_key):
    url='https://api.nasa.gov/mars-photos/api/v1/rovers/'+rover+'/photos?sol='+str(sol)+'&api_key='+API_KEY[compt_api_key]
    with urllib.request.urlopen(url) as fichier:
         réordonnencement(fichier)
         compt_req+=1 # une requête  a été effectuée
    return compt_req

def data_base():
    data={"photos":[0]}
    compt_api_key=0
    compt_req=0 # compteur pour limiter le nombre de requêtes à 1000 par heures
    for rover in ROVER:
        sol=-1
        while len(data["photos"])!=0:
            sol+=1
            if compt_req==5 and compt_api_key<len(API_KEY)-1: # Si on a atteint le nombre de requête maximale pour la clé, on passe à la suivante
                compt_api_key+=1
                compt_req=0
            elif compt_req==5: # Si on a atteint le nombre maximal de requête pour toutes les clés, on attend 1h
                time.sleep(10)
                compt_req=check_NASA(compt_req, rover, sol, compt_api_key)
            else:
                compt_req=check_NASA(compt_req, rover, sol, compt_api_key)
                



def sol_max(rover_id):
    sol_max_rov=0
    for photos_id in dico_photos:
        photo=dico_photos[photos_id]
        sol_photo=photo['sol']
        if photo['rover']==rover_id and sol_photo>sol_max_rov:
            sol_max_rov=sol_photo
    return sol_max_rov

def deter_rover_id_nom(rover):
    for rover_id_l in dico_rover:
        if dico_rover[rover_id_l]['name']==rover:
            return rover_id_l

def deter_rover_id_id(rover_id):
    for rover_id_l in dico_rover:
        if dico_rover[rover_id_l]['name']==ROVER[rover_id].title():
            return rover_id_l

    
def réordonnencement_posi(fichier,rover_id):
    data=json.load(fichier)
    dico_posi[rover_id]={}
    dico_posi_rov=dico_posi[rover_id]
    sol_max_rov=sol_max(rover_id)
    data_posi_0=data['features'][0]['properties']
    dico_posi_rov[0]={'lat':data_posi_0['lat'],'long':data_posi_0['lon'],'cap':data_posi_0['yaw']}
    for d in range(1,sol_max_rov):
        dico_posi_rov[d]=dico_posi_rov[d-1]
        data_posi_d=data['features'][d]['properties']
        if data_posi_d['lat']!=dico_posi_rov[d]['lat'] or data_posi_d['lon']!=dico_posi_rov[d]['long'] or data_posi_d['yaw']!=dico_posi_rov[d]['cap']:
            dico_posi_rov[d]={'lat':data_posi_d['lat'],'long':data_posi_d['lon'],'cap':data_posi_d['yaw']}
    
def check_posi():
    rover_id=0
    for lien in LIENS_POSI:
        with urllib.request.urlopen(lien) as fichier_posi:
            réordonnencement_posi(fichier_posi,deter_rover_id_id(rover_id))
        rover_id+=1


#data_base()
#check_posi()
