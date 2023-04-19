import urllib.request
with urllib.request.urlopen('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY') as f:
    print(f.read())