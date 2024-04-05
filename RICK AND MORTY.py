import requests  # Importamos la biblioteca requests para realizar solicitudes HTTP

def obtener_personajes_rick_morty():
    # URL de la API de Rick and Morty para obtener la lista de personajes
    url = "https://rickandmortyapi.com/api/character"
    
    # Realizamos la solicitud GET a la API de Rick and Morty
    respuesta = requests.get(url)
    
    # Verificamos si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Devolvemos los datos de los personajes en formato JSON
        return respuesta.json()["results"]
    else:
        # Si la solicitud no fue exitosa, imprimimos un mensaje de error
        print("Error al obtener los personajes de Rick and Morty:", respuesta.status_code)
        return None

def ordenar_personajes_por_nombre(personajes):
    # Utilizamos la función sorted para ordenar los personajes por su nombre
    return sorted(personajes, key=lambda x: x["name"])

def mostrar_personajes(personajes):
    # Iteramos sobre la lista de personajes y mostramos su nombre
    for personaje in personajes:
        print(personaje["name"])

# Función principal
def main():
    # Obtenemos la lista de personajes de Rick and Morty
    personajes = obtener_personajes_rick_morty()
    
    # Si se obtuvieron los personajes correctamente, los ordenamos y los mostramos
    if personajes:
        personajes_ordenados = ordenar_personajes_por_nombre(personajes)
        print("Personajes de Rick and Morty ordenados por nombre:")
        mostrar_personajes(personajes_ordenados)

if __name__ == "__main__":
    main()
