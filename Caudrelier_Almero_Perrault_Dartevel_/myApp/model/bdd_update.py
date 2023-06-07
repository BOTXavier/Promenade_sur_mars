#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:28:03 2023

@author: louis-yann
"""

import myApp.model.bdd_initiate as ini

##################################################################################

# Mise à jour des dictionnaires entre la dernier maj et aujourd'hui

###################################################################################

def deter_dernier_sol(dico_photos,dico_rovers):
    dernier_sol=[]
    for rover_id in range(len(ini.ROVER)):
        sol=0
        rover_id=ini.deter_rover_id_id(rover_id,dico_rovers)
        for photo_id in dico_photos:
            photo=dico_photos[photo_id]
            sol_photo=photo['sol']
            rover_id_photo=photo['rover_id']
            if sol<sol_photo and rover_id==rover_id_photo:
                sol=sol_photo
        dernier_sol.append(sol+1)
    return dernier_sol

def créer_dicos(deb,fin):
    N=fin-deb
    dicos123=ini.data_base(N,[deb,deb,deb,deb],{},{},{})
    dico_photos,dico_rovers,dico_cameras=dicos123[0],dicos123[1],dicos123[2]

    dico123=ini.data(deb,fin)

    DERNIER_SOL=deter_dernier_sol(dico_photos,dico_rovers)
    print(DERNIER_SOL)
    ini.data_base(N,DERNIER_SOL,dico_photos,dico_rovers,dico_cameras)

    dico_posi=ini.check_posi([deb,deb,deb,deb],dico_photos,dico_rovers,dico_cameras,{})
    return (dico_photos,dico_rovers,dico_cameras,dico_posi)

def créer_dicos_2(deb,fin):
    dicos123=ini.data(deb,fin)
    dico_photos,dico_rovers,dico_cameras=dicos123[0],dicos123[1],dicos123[2]

    dico_posi=ini.construire_posi(deb,fin,dico_rovers)
    return (dico_photos,dico_rovers,dico_cameras,dico_posi)

#dico_photos,dico_rovers,dico_cameras,dico_posi=créer_dicos()

##################################################################################

# Mise à jour de l'orientation des cameras sur bras au jour le jour

###################################################################################

def aligner_cams(camera_id,cam_name,cam_rov_id,angles_mats, angles_sherlocks):
        if cam_rov_id==8: # Perseverance
            angle_mat_hori=angles_mats[0][0]
            angle_mat_verti=angles_mats[1][0]
            angle_sherlock1=angles_sherlocks[0][0]
            angle_sherlock2=angles_sherlocks[1][0]
            if cam_name=="MCZ_LEFT":
                return [angle_mat_hori+1,angle_mat_verti-1]
            elif cam_name=="MCZ_RIGHT":
                return [angle_mat_hori-1,angle_mat_verti-1]
            elif cam_name=="NAVCAM _LEFT":
                return [angle_mat_hori+2,angle_mat_verti-1]
            elif cam_name=="NAVCAM _RIGHT":
                return [angle_mat_hori-2,angle_mat_verti-1]
            elif cam_name=="SUPERCAM_RMI":
                return [angle_mat_hori+1,angle_mat_verti]
            elif cam_name=="SHERLOC_WATSON":
                return [angle_sherlock1,angle_sherlock2]
        elif cam_rov_id==5: #Curiosity
             angle_mat_hori=angles_mats[0][1]
             angle_mat_verti=angles_mats[1][1]
             angle_sherlock1=angles_sherlocks[0][1]
             angle_sherlock2=angles_sherlocks[1][1]
             if cam_name=="MAST":
                return [angle_mat_hori,angle_mat_verti-1]
             elif cam_name=="CHEMCAM":
                return [angle_mat_hori,angle_mat_verti]
             elif cam_name=="NAVCAM":
                return [angle_mat_hori+1,angle_mat_verti-1]
        elif cam_rov_id==7: #Spirit
             angle_mat_hori=angles_mats[0][2]
             angle_mat_verti=angles_mats[1][2]
             angle_sherlock1=angles_sherlocks[0][2]
             angle_sherlock2=angles_sherlocks[1][2]
             if cam_name=="NAVCAM":
                return [angle_mat_hori,angle_mat_verti]
             elif cam_name=="PANCAM":
                return [angle_mat_hori+1,angle_mat_verti]
             elif cam_name=="MINITES":
                return [(angle_mat_hori+180)%360,angle_mat_verti]
        elif cam_rov_id==6: #Opportunity
             angle_mat_hori=angles_mats[0][3]
             angle_mat_verti=angles_mats[1][3]
             angle_sherlock1=angles_sherlocks[0][3]
             angle_sherlock2=angles_sherlocks[1][3]
             if cam_name=="NAVCAM":
                return [angle_mat_hori,angle_mat_verti]
             elif cam_name=="PANCAM":
                return [angle_mat_hori+1,angle_mat_verti]
             elif cam_name=="MINITES":
                return [(angle_mat_hori+180)%360,angle_mat_verti]
