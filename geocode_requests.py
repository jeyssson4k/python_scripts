import requests

def readfile(filename, separator):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [float(line.split(separator)[0]) for line in lines], [float(line.split(separator)[1]) for line in lines]

def obtener_nombre_ciudad(latitud, longitud, key):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={latitud}%2C{longitud}&key={key}"
    response = requests.get(url)
    data = response.json()
    if 'results' in data:
        return data['results'][0].get('formatted', 'NA')
    else:
        return 'NA'

key = 'your key here'
fpath = 'file path'
separator = ','
init = 0

lat, lon = readfile(fpath, separator)

for i in range(init,len(lat)):
    ciudad = obtener_nombre_ciudad(lat[i], lon[i], key)
    print(ciudad)
