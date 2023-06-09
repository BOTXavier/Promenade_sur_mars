#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""

Created on Thu May 11 10:17:43 2023



@author: louis-yann

"""



import urllib.request

import json

import time



###################################################################################



# Construit les dictionnaires bien rangés des données des photos, pour toutes les photos

# ATTENTION : boucle de temps avec une pause de une heure pour ne pas trop en demander à l'API NASA



###################################################################################



ROVER=['perseverance','curiosity','spirit','opportunity']

API_KEY=['09r9lOKEqz9yGsPK6iiKDFFKRBLEvl7ZQKXyNaoS', 'uFPg2xAvVYtXreHwgx9swNodGOnuqRCsqRX426T6']

LIENS_POSI=['https://mars.nasa.gov/mmgis-maps/M20/Layers/json/M20_waypoints.json','https://mars.nasa.gov/mmgis-maps/MSL/Layers/json/MSL_waypoints.json'] # A ordonner dans le même ordre que ROVER

LIST_CAM_MOBILES=[41,40,38,39,22,23,26,29,30,31,16,17,18,47] # missing : SHERLOC_WATSON rover8, 



def réordonnencement(fichier,dico_photos,dico_rovers,dico_cameras):

    data=fichier.read().decode('utf-8')

    liste_data=eval(data)["photos"] # Conversion de la chaine de caractère en la liste de dictionnaires de chaques photos

    for photos in liste_data:

        rover=photos['rover']

        rover_id=rover['id']

        camera=photos['camera']

        camera_id=camera['id']

        dico_photos[photos['id']]={'sol':photos['sol'],'rover_id':rover_id,'camera_id':camera_id,'url':photos['img_src']}

        if rover_id not in dico_rovers:

            rover.pop('id')

            dico_rovers[rover_id]=rover

        if camera_id not in dico_cameras:

            camera.pop('id')

            dico_cameras[camera_id]=camera

            dico_cameras[camera_id]['orient_hori']=0 # coordonnée spérique regardant vers l'avant du rover, horizontalement

            dico_cameras[camera_id]['orient_verti']=0 # coordonnée spérique regardant vers l'avant du rover, verticalement

        

            

def check_NASA(compt_req,rover,sol,compt_api_key,dico_photos,dico_rovers,dico_cameras):

    url='https://api.nasa.gov/mars-photos/api/v1/rovers/'+rover+'/photos?sol='+str(sol)+'&api_key='+API_KEY[compt_api_key]

    with urllib.request.urlopen(url) as fichier:

         réordonnencement(fichier,dico_photos,dico_rovers,dico_cameras)

         compt_req+=1 # une requête  a été effectuée

    return compt_req



def data_base(n,dernier_sol,dico_photos,dico_rovers,dico_cameras):

    data={"photos":[0]}

    compt_api_key=0

    compt_req=0 # compteur pour limiter le nombre de requêtes à 1000 par heures

    for rover in ROVER:

        compt_rover=ROVER.index(rover)

        sol=dernier_sol[compt_rover]-1

        while len(data["photos"])!=0:

            sol+=1

            if sol==n+dernier_sol[compt_rover] and rover!='opportunity':

                break

            if rover=='opportunity' and sol==dernier_sol[compt_rover]+2:

                break

            print(sol)

            if compt_req==1000 and compt_api_key<len(API_KEY)-1: # Si on a atteint le nombre de requête maximale pour la clé, on passe à la suivante

                compt_api_key+=1

                compt_req=0

            elif compt_req==1000: # Si on a atteint le nombre maximal de requête pour toutes les clés, on attend 1h

                time.sleep(86400)

                compt_req=check_NASA(compt_req, rover, sol,compt_api_key,dico_photos,dico_rovers,dico_cameras)

            else:

                compt_req=check_NASA(compt_req, rover, sol,compt_api_key,dico_photos,dico_rovers,dico_cameras)

    angles_mats=[[0,0,0,0],[0,0,0,0]] # On suppose les bras initialement orienté vers l'avant

    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]

    orient_cams(dico_cameras,angles_mats,angles_sherlocks)

    return [dico_photos,dico_rovers,dico_cameras]

def data(deb,fin):
    print('start')
    dernier_sol=[deb,deb,deb,deb]
    dico_photos,dico_rovers,dico_cameras={},{},{}
    data={"photos":[0]}
    compt_api_key=0
    compt_req=0 # compteur pour limiter le nombre de requêtes à 1000 par heures
    n=fin-deb
    for rover in ROVER:
        compt_rover=ROVER.index(rover)
        sol=dernier_sol[compt_rover]-1
        while len(data["photos"])!=0:
            sol+=1
            if sol==n+dernier_sol[compt_rover]:
                break
            print(sol)
            if compt_req==1000 and compt_api_key<len(API_KEY)-1: # Si on a atteint le nombre de requête maximale pour la clé, on passe à la suivante
                compt_api_key+=1
                compt_req=0
            elif compt_req==1000: # Si on a atteint le nombre maximal de requête pour toutes les clés, on attend 1h
                time.sleep(86400)
                compt_req=check_NASA(compt_req, rover, sol,compt_api_key,dico_photos,dico_rovers,dico_cameras)
            else:
                compt_req=check_NASA(compt_req, rover, sol,compt_api_key,dico_photos,dico_rovers,dico_cameras)
    angles_mats=[[0,0,0,0],[0,0,0,0]] # On suppose les bras initialement orienté vers l'avant
    angles_sherlocks=[[0,0,0,0],[0,0,0,0]]
    orient_cams(dico_cameras,angles_mats,angles_sherlocks)
    return [dico_photos,dico_rovers,dico_cameras]

##################################################################################



# Donne la position des caméras dans le référentiel du rover



###################################################################################

           

def orient_cams(dico_cameras,angles_mats,angles_sherlocks):

    for camera_id in dico_cameras:

        cam_rov_id=dico_cameras[camera_id]['rover_id']

        cam_name=dico_cameras[camera_id]['name']

        if cam_rov_id==8: # Perseverance

            angle_mat_hori=angles_mats[0][0]

            angle_mat_verti=angles_mats[1][0]

            angle_sherlock1=angles_sherlocks[0][0]

            angle_sherlock2=angles_sherlocks[1][0]

            if cam_name=="FRONT_HAZCAM_LEFT_A":

                dico_cameras[camera_id]['orient_hori']=1

                dico_cameras[camera_id]['orient_verti']=0

            elif cam_name=="FRONT_HAZCAM_RIGHT_A":

                dico_cameras[camera_id]['orient_hori']=359

                dico_cameras[camera_id]['orient_verti']=0

            elif cam_name=="REAR_HAZCAM_LEFT":

                dico_cameras[camera_id]['orient_hori']=179

                dico_cameras[camera_id]['orient_verti']=0

            elif cam_name=="REAR_HAZCAM_RIGHT":

                dico_cameras[camera_id]['orient_hori']=181

                dico_cameras[camera_id]['orient_verti']=0

            elif cam_name=="SKYCAM": # caméra vers le haut

                dico_cameras[camera_id]['orient_hori']=0

                dico_cameras[camera_id]['orient_verti']=90

            elif cam_name=="MCZ_LEFT":

                dico_cameras[camera_id]['orient_hori']=angle_mat_hori+1

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti-1

            elif cam_name=="MCZ_RIGHT":

                dico_cameras[camera_id]['orient_hori']=angle_mat_hori-1

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti-1

            elif cam_name=="NAVCAM _LEFT":

                dico_cameras[camera_id]['orient_hori']=angle_mat_hori+2

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti-1

            elif cam_name=="NAVCAM _RIGHT":

                dico_cameras[camera_id]['orient_hori']=angle_mat_hori-2

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti-1

            elif cam_name=="EDL_RUCAM": # caméra vers le haut

                dico_cameras[camera_id]['orient_hori']=0

                dico_cameras[camera_id]['orient_verti']=90

            elif cam_name=="EDL_DDCAM": # caméra vers le haut

                dico_cameras[camera_id]['orient_hori']=0

                dico_cameras[camera_id]['orient_verti']=90

            elif cam_name=="EDL_RDCAM": # caméra vers le bas

                dico_cameras[camera_id]['orient_hori']=0

                dico_cameras[camera_id]['orient_verti']=270

            elif cam_name=="EDL_PUCAM1": # caméra vers le bas

                dico_cameras[camera_id]['orient_hori']=0

                dico_cameras[camera_id]['orient_verti']=270

            elif cam_name=="EDL_PUCAM1": # caméra vers le bas

                dico_cameras[camera_id]['orient_hori']=0

                dico_cameras[camera_id]['orient_verti']=270

            elif cam_name=="SUPERCAM_RMI":

                dico_cameras[camera_id]['orient_hori']=angle_mat_hori+1

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti

            elif cam_name=="SHERLOC_WATSON":

                dico_cameras[camera_id]['orient_hori']=angle_sherlock1

                dico_cameras[camera_id]['orient_verti']=angle_sherlock2

        elif cam_rov_id==5: #Curiosity

             angle_mat_hori=angles_mats[0][1]

             angle_mat_verti=angles_mats[1][1]

             angle_sherlock1=angles_sherlocks[0][1]

             angle_sherlock2=angles_sherlocks[1][1]

             if cam_name=="FHAZ":

                dico_cameras[camera_id]['orient_hori']=0

                dico_cameras[camera_id]['orient_verti']=0

             elif cam_name=="RHAZ":

                dico_cameras[camera_id]['orient_hori']=180

                dico_cameras[camera_id]['orient_verti']=0

             elif cam_name=="MAST":

                dico_cameras[camera_id]['orient_hori']=angle_mat_hori

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti-1

             elif cam_name=="CHEMCAM":

                dico_cameras[camera_id]['orient_hori']=angle_mat_hori

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti

             elif cam_name=="MAHLI":

                dico_cameras[camera_id]['orient_hori']=135

                dico_cameras[camera_id]['orient_verti']=0

             elif cam_name=="MARDI":

                dico_cameras[camera_id]['orient_hori']=10

                dico_cameras[camera_id]['orient_verti']=270

             elif cam_name=="NAVCAM":

                dico_cameras[camera_id]['orient_hori']=angle_mat_hori+1

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti-1

        elif cam_rov_id==7: #Spirit

             angle_mat_hori=angles_mats[0][2]

             angle_mat_verti=angles_mats[1][2]

             angle_sherlock1=angles_sherlocks[0][2]

             angle_sherlock2=angles_sherlocks[1][2]

             if cam_name=="FHAZ":

                 dico_cameras[camera_id]['orient_hori']=0

                 dico_cameras[camera_id]['orient_verti']=0

             elif cam_name=="RHAZ":

                dico_cameras[camera_id]['orient_hori']=180

                dico_cameras[camera_id]['orient_verti']=0

             elif cam_name=="NAVCAM":

                dico_cameras[camera_id]['orient_hori']=angle_mat_hori

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti

             elif cam_name=="PANCAM":

                dico_cameras[camera_id]['orient_hori']=angle_mat_hori+1

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti

             elif cam_name=="MINITES":

                dico_cameras[camera_id]['orient_hori']=(angle_mat_hori+180)%360

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti

             elif cam_name=="ENTRY":

                dico_cameras[camera_id]['orient_hori']=10

                dico_cameras[camera_id]['orient_verti']=270

        elif cam_rov_id==6: #Opportunity

             angle_mat_hori=angles_mats[0][3]

             angle_mat_verti=angles_mats[1][3]

             angle_sherlock1=angles_sherlocks[0][3]

             angle_sherlock2=angles_sherlocks[1][3]

             if cam_name=="FHAZ":

                 dico_cameras[camera_id]['orient_hori']=0

                 dico_cameras[camera_id]['orient_verti']=0

             elif cam_name=="RHAZ":

                dico_cameras[camera_id]['orient_hori']=180

                dico_cameras[camera_id]['orient_verti']=0

             elif cam_name=="NAVCAM":

                dico_cameras[camera_id]['orient_hori']=angle_mat_hori

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti

             elif cam_name=="PANCAM":

                dico_cameras[camera_id]['orient_hori']=angle_mat_hori+1

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti

             elif cam_name=="MINITES":

                dico_cameras[camera_id]['orient_hori']=(angle_mat_hori+180)%360

                dico_cameras[camera_id]['orient_verti']=angle_mat_verti

             elif cam_name=="ENTRY":

                dico_cameras[camera_id]['orient_hori']=10

                dico_cameras[camera_id]['orient_verti']=270

                





##################################################################################



# Construit le dictionnaire des positions chaque jour de chaque rover



###################################################################################





def sol_max(rover_id,dico_photos):

    sol_max_rov=0

    for photos_id in dico_photos:

        photo=dico_photos[photos_id]

        sol_photo=photo['sol']

        if photo['rover_id']==rover_id and sol_photo>sol_max_rov:

            sol_max_rov=sol_photo

    return sol_max_rov



def deter_rover_id_nom(rover,dico_rovers):

    for rover_id_l in dico_rovers:

        if dico_rovers[rover_id_l]['name']==rover:

            return rover_id_l



def deter_rover_id_id(rover_id,dico_rovers):

    for rover_id_l in dico_rovers:

        if dico_rovers[rover_id_l]['name']==ROVER[rover_id].title():

            return rover_id_l



    

def réordonnencement_posi(fichier,rover_id,dernier_sol,dico_photos,dico_rovers,dico_cameras,dico_posi):

    data=json.load(fichier)

    dico_posi_interm={}

    dico_posi_interm[rover_id]={}

    dico_posi_rov=dico_posi_interm[rover_id]

    sol_max_rov=sol_max(rover_id,dico_photos)

    data_posi_0=data['features'][0]['properties']

    dico_posi_rov[0]={'rover_id':rover_id,'lat':data_posi_0['lat'],'long':data_posi_0['lon'],'cap':data_posi_0['yaw']}

    for d in range(1+dernier_sol[ROVER.index(dico_rovers[rover_id]['name'].lower())],sol_max_rov):

        dico_posi_rov[d]=dico_posi_rov[d-1]

        data_posi_d=data['features'][d]['properties']

        if data_posi_d['lat']!=dico_posi_rov[d]['lat'] or data_posi_d['lon']!=dico_posi_rov[d]['long'] or data_posi_d['yaw']!=dico_posi_rov[d]['cap']:

            dico_posi_rov[d]={'rover_id':rover_id,'lat':data_posi_d['lat'],'long':data_posi_d['lon'],'cap':data_posi_d['yaw']}

    for rover_id in dico_posi_interm:

        num_rover=ROVER.index(dico_rovers[rover_id]['name'].lower())

        posi_rover=dico_posi_interm[rover_id]

        for posi_id in posi_rover:

            posi=posi_rover[posi_id]

            dico_posi[num_rover*(10**6)+posi_id]=posi
            dico_posi[num_rover*(10**6)+posi_id]['sol']=posi_id
            
    return dico_posi



def check_posi(dernier_sol,dico_photos,dico_rovers,dico_cameras,dico_posi):

    rover_id=0

    for lien in LIENS_POSI:

        with urllib.request.urlopen(lien) as fichier_posi:

            dico_posi=réordonnencement_posi(fichier_posi,deter_rover_id_id(rover_id,dico_rovers),dernier_sol,dico_photos,dico_rovers,dico_cameras,dico_posi)

        rover_id+=1
    return dico_posi

def construire_posi(deb,fin,dico_rovers):
    dico_posi={}
    for lien in LIENS_POSI:
        dico_posi_interm={}
        with urllib.request.urlopen(lien) as fichier_posi:
            data=json.load(fichier_posi)['features']
        rover_id=deter_rover_id_id(LIENS_POSI.index(lien),dico_rovers)
        for s in range(deb,fin+1):
            posi_id=LIENS_POSI.index(lien)*(10**6)+s
            dico_posi_interm[posi_id]={'rover_id':rover_id,'lat':0,'long':0,'cap':0,'sol':s}

        for posi_id in dico_posi_interm:

            sol=dico_posi_interm[posi_id]['sol']
            compt=-1
            sol_data=-1
            while sol_data<sol:
                compt+=1
                sol_data=data[compt]['properties']['sol']
            info_posi_id=data[compt]['properties']
            #print(info_posi_id['lat'],info_posi_id['lon'],info_posi_id['yaw'])
            dico_posi_interm[posi_id]['lat']=info_posi_id['lat']
            dico_posi_interm[posi_id]['long']=info_posi_id['lon']
            dico_posi_interm[posi_id]['cap']=info_posi_id['yaw']
        for posi_id in dico_posi_interm:
            dico_posi[posi_id]=dico_posi_interm[posi_id]
    return dico_posi