NV = "development"
DEBUG = True
SEND_FILE_MAX_AGE_DEFAULT = 0 #vider le cache
SECRET_KEY="maCleSuperSecurisee"

#Configuration du serveur web
WEB_SERVER = {
    "host": "localhost",
    "port":8080,
}
#Configuration du serveur de BDD
DB_SERVER = {
    "user": "root",
<<<<<<< HEAD
#    "password": "8uYb9apMj", #8uYb9apMj
=======
#   "password": "8uYb9apMj", #8uYb9apMj
>>>>>>> 2ae450a985b7af3d6de6100d5865c62d65ef435e
    "host": "localhost",
    "port": 3306, #8889 si MAC
    "database": "promenade_sur_mars", #nom de la BDD
    "raise_on_warnings": True
}
