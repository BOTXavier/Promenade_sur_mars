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

def créer_dicos():
    N=2
    dicos123=ini.data_base(N,[0,0,0,0],{},{},{})
    dico_photos,dico_rovers,dico_cameras=dicos123[0],dicos123[1],dicos123[2]

    DERNIER_SOL=deter_dernier_sol(dico_photos,dico_rovers)
    ini.data_base(N,DERNIER_SOL,dico_photos,dico_rovers,dico_cameras)

    dico_posi=ini.check_posi([0,0,0,0],dico_photos,dico_rovers,dico_cameras,{})
    return (dico_photos,dico_rovers,dico_cameras,dico_posi)

#dico_photos,dico_rovers,dico_cameras,dico_posi=créer_dicos()