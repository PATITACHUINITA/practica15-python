import requests

def obtener_pokemon():
    nombre = input("Ingresa el nombre del Pokémon: ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza un error si la solicitud falla
        
        datos = respuesta.json()
        nombre_pokemon = datos["name"].capitalize()
        altura = datos["height"] / 10  # Convertir a metros
        peso = datos["weight"] / 10  # Convertir a kg
        numero_pokedex = datos["id"]
        tipos = [tipo["type"]["name"].capitalize() for tipo in datos["types"]]
        habilidades = [hab["ability"]["name"].capitalize() for hab in datos["abilities"]]

        print("\nPOKÉDEX")
        print(f"Número: {numero_pokedex}")
        print(f"Nombre: {nombre_pokemon}")
        print(f"Altura: {altura} metros")
        print(f"Peso: {peso} kg")
        print(f"Tipo(s): {', '.join(tipos)}")
        print(f"Habilidades: {', '.join(habilidades)}")

    except requests.exceptions.HTTPError:
        print("Pokémon no encontrado. Intenta nuevamente.")
    except requests.exceptions.RequestException:
        print("Error de conexión con la API.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Llamar a la función
obtener_pokemon()
