import requests
import json

p = open('data/propietarios.csv', "r").readlines()
d = open('data/departamentos.csv', "r").readlines()
e = open('data/edificios.csv', "r").readlines()

def create_propietario(cedula, nombre, apellido):
    data = {
        'cedula': cedula,
        'nombre': nombre,
        'apellido': apellido
    }
    response = requests.post('http://127.0.0.1:8000/propietarios/', data=data, auth=('roger1', '1'))
    
    if response.status_code == 201:
        print(f"Propietario '{nombre} {apellido}' creado exitosamente.")
    else:
        print(f"Error al crear el propietario '{nombre} {apellido}'. Error {response.status_code}: {response.text}")

#for line in p:
    #cedula = line.split('|')[0]
    #nombre = line.split('|')[1]
    #apellido = line.split('|')[2]
   # create_propietario(cedula, nombre, apellido)


# Function to create an edificio (building) using HTTP POST request
def create_edificio(nombre, direccion, ciudad, tipo):
    data = {
        'nombre': nombre,
        'direccion': direccion,
        'ciudad': ciudad,
        'tipo': tipo
    }
    response = requests.post('http://127.0.0.1:8000/edificios/', data=data, auth=('roger1', '1'))
    
    if response.status_code == 201:
        print(f"Edificio '{nombre}' creado exitosamente.")
    else:
        print(f"Error al crear el edificio '{nombre}'. Error {response.status_code}: {response.text}")


#for line in e:
    #nombre = line.split('|')[0]
    #direccion = line.split('|')[1]
    #iudad = line.split('|')[2]
    #tipo = line.split('|')[3]
    #create_edificio(nombre, direccion, ciudad, tipo)


def create_departamento(propietario, costo, num_cuartos,edificio):
    data = {
        'propietario': [i["url"] for i in pro if i['cedula'] == propietario ][0],
        'edificio': [j["url"] for j in edi if j['nombre'] == edificio ][0],
        'costo': costo,
        'num_cuartos': num_cuartos
    }
    print(data)
    response = requests.post('http://127.0.0.1:8000/departamentos/', data=data, auth=('roger1', '1'))
    
    if response.status_code == 201:
        print(f"Departamento '{edificio}' creado exitosamente.")
    else:
        print(f"Error al crear el departamento '{edificio}'. Error {response.status_code}: {response.text}")

edi = requests.get("http://127.0.0.1:8000/edificios/", auth = ("roger1", "1")).json()
pro = requests.get("http://127.0.0.1:8000/propietarios/", auth = ("roger1", "1")).json()



for line in d:
    propietario = line.split('|')[0]
    costo = line.split('|')[1]
    num_cuartos = line.split('|')[2]
    edificio = line.split('|')[3]

    create_departamento(propietario, costo, num_cuartos, edificio)

"""

    urlpropietario = None
    for i in pro:
        if i['cedula'] == propietario:
            urlpropietario = i["url"]
            break

    urledificio = None
    for i in edi:
        if i['nombre'] == edificio:
            urledificio = i["url"]
            break

"""       



  

