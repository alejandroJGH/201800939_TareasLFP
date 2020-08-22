import json

def CargarDatos(ruta):
    with open(ruta) as contenido:
        DatosJson = json.load(contenido)
        for atributo in DatosJson:
            print(atributo.get('nombre'))
            print(atributo.get('Carnet'))
            print(atributo.get('Carrera'))
            print(atributo.get('Escuela'))
            print('----------------------')

