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
    "password": "8uYb9apMj", #8uYb9apMj
>>>>>>> 032304c41986a4230181518467348ed4b2be2cd0
    "host": "localhost",
    "port": 3306, #8889 si MAC
    "database": "promenade_sur_mars", #nom de la BDD
    "raise_on_warnings": True
}
