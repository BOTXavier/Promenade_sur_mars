import urllib.request
import json


#url pour retrouver les positions des rovers
url_heli_Perseverance = "https://mars.nasa.gov/mmgis-maps/M20/Layers/json/m20_heli_waypoints.json" #heli_Perseverance
url_Perseverance = "https://mars.nasa.gov/mmgis-maps/M20/Layers/json/M20_waypoints.json#"#Perseverance

url = url_Perseverance
# Télécharger le contenu JSON à partir de l'URL
with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

# Afficher le dictionnaire créé à partir du contenu JSON
print(data)