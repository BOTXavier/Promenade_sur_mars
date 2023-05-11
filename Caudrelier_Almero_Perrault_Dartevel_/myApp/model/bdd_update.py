#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:28:03 2023

@author: louis-yann
"""

import bdd_login as logi

##################################################################################

# Mise à jour des dictionnaires entre la dernier maj et aujourd'hui

###################################################################################

N=3

def deter_dernier_sol(dico_photos,dico_rover):
    dernier_sol=[]
    for rover_id in range(len(logi.ROVER)):
        sol=0
        rover_id=logi.deter_rover_id_id(rover_id,dico_rover)
        for photo_id in dico_photos:
            photo=dico_photos[photo_id]
            sol_photo=photo['sol']
            rover_id_photo=photo['rover']
            if sol<sol_photo and rover_id==rover_id_photo:
                sol=sol_photo
        dernier_sol.append(sol)
    return dernier_sol

dicos123=logi.data_base(N,[0,0,0,0],{},{},{})
dico_photos,dico_rover,dico_camera=dicos123[0],dicos123[1],dicos123[2]

DERNIER_SOL=deter_dernier_sol(dico_photos,dico_rover)
logi.data_base(3,[N,N,N,N],dico_photos,dico_rover,dico_camera)

# for i in range(7):
#     compt=0
#     for photo_id in dico_photos:
#         if dico_photos[photo_id]['sol']==i:
#             compt+=1
#     print(compt)