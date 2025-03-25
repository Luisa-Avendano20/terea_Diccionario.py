# Crear un Diccionario
informacion_personal = {
    "nombre": "Eirikr Yaguachi",  # Nombre ficticio
    "edad": 3,              # Edad ficticia
    "ciudad": "Paris",      # Ciudad ficticia
    "profesion": "Ingeniero" # Profesión ficticia
}

# Acceder y Modificar Valores
# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Rusia"  # Cambiar la ciudad a Rusia

# Agregar una nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"  # Actualizar la profesión

# Verificar Existencia de Claves
# Verificar si la clave "numero de celular" existe en el diccionario
if "numero de celular" not in informacion_personal:
    informacion_personal["numero de celular"] = "0980185424"  # Agregar un número de celular ficticio

# Eliminar una Clave
# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el Diccionario Final
print("Información Personal Actualizada:")
print(informacion_personal)
