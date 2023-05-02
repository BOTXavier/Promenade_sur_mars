import urllib.request
import time

###################################################################################

# Construit les dictionnaires bien rangés des données des photos, pour toutes les photos
# ATTENTION : boucle de temps avec une pause de une heure pour ne pas trop en demander à l'API NASA

###################################################################################

ROVER=['spirit','opportunity','curiosity','perseverance']
API_KEY=['09r9lOKEqz9yGsPK6iiKDFFKRBLEvl7ZQKXyNaoS']

dico_photos={}
dico_rover={}
dico_camera={}

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
            
def check_NASA(compt,rover,sol,compt_api_key):
    url='https://api.nasa.gov/mars-photos/api/v1/rovers/'+rover+'/photos?sol='+str(sol)+'&api_key='+API_KEY[compt_api_key]
    with urllib.request.urlopen(url) as fichier:
         réordonnencement(fichier)
         compt+=1
         print(compt,len(dico_photos))
         return compt


def data_base():
    data={"photos":[0]}
    compt_api_key=0
    compt=0 # compteur pour limiter le nombre de requêtes à 1000 par heures
    for rover in ROVER:
        sol=-1
        while len(data["photos"])!=0:
            sol+=1
            # print(compt,sol)
            if compt==100 and compt_api_key<len(API_KEY)-1:
                compt_api_key+=1
                compt=0
            elif compt==100:
                time.sleep(10)
                compt=check_NASA(compt, rover, sol, compt_api_key)
            else:
                compt=check_NASA(compt, rover, sol, compt_api_key)

data_base()