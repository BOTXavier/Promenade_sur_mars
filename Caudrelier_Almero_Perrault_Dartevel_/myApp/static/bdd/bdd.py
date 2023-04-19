import urllib.request

DATA=[]

#for i in range(2001):
#    with urllib.request.urlopen('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol='+str(i)+'&api_key=DEMO_KEY') as f:
#        DATA.append(eval(f.read().decode('utf-8')))


with urllib.request.urlopen('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY') as f:
    data=f.read().decode('utf-8')
    print(type(data))
    datadico=eval(data)
    print(type(datadico))

