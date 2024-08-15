numbers = {1:"uno", 2:"dos", 3:"tres"} #en llaves
print(numbers)
print(numbers[1])
print(numbers[2])
print(numbers[3])
information = {"nombre" : "Jheyson",
               "apellidos" : "Galvis",
               "estatura" : 1.69,
               "esta feliz" : True}
print(information)
#del information ["apellidos"]
print(information)
claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Jheyson": {"Apellido": "Galvis",
                        "Altura": 1.69,
                        "Edad": 32,
                        "Teléfono": 3167417556,
                        "Signo Zodiacal": "Piscis",
                        "Serie Favorita": "Silicon Valley",
                        "Canción favorita": "Todo irá bien - Chenoa",
                        "Comida favorita": "Frijoles, carne",
                        "Lugar soñado vacaciones": "Silicon Valley",
                        "Habilidad secreta": "repetir el día para salvar muertos",
                        "Pasatiempo":"Caminar con mis perros",
                        "Heroe o persona que admiras": "Elon Musk",
                        "Libro que más me ha impactado": "Salvese quien pueda",
                        "Cenar con alguien": "Freddy Vega CEO Platzi",
                        "Superpoder": "viajar por multiversos",
                        "Que logro personal te enorgullese": "Aprender Python",},
            "Aurelio": {"Apellido": "Cheveroni",
                        "Altura": 1.20,
                        "Edad": 8}}
print(contacts)