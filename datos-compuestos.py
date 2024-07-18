# El primer tipo de dato compuesto que veremos será la lista

lista = ["Jheyson Galvis", "tecnotutoriales Jheyson Galvis", True, 1.69]
print(lista[1])
lista[3] = "Jheysonsaurio"
print(lista[3])

# La tupla es una lista que no se puede modificar

tupla = ("Jheyson Galvis", "tecnotutoriales Jheyson Galvis", True, 1.69)
print(tupla[1])
#tupla[1] = "Tips TIC al paso"
#print(tupla[1])

# Creando un conjunto o set
# Un conjunto no admite elementos duplicados

conjunto = {"Jheyson Galvis", "tecnotutoriales Jheyson Galvis", True, 1.69, 1.69}
print (conjunto)

# Creando un diccionario
diccionario = {
    "nombre": "Jheyson",
    "apellido" : "Galvis",
    "estatura" : 1.69,
    "esta feliz" : True
}

print(diccionario["esta feliz"])
print(diccionario["nombre"])
print(diccionario["apellido"])
print(diccionario["estatura"])






