import requests

class StarWarsGalaxyAPI:
    def __init__(self):
        self.base_url = "https://swapi.dev/api/"

    def get_person(self, person_id):
        url = f"{self.base_url}people/{person_id}/" 
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch data"}

    def get_film(self, film_id):
        url = f"{self.base_url}films/{film_id}/"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch data"}

    def search_person_by_name(self, name):
        url = f"{self.base_url}people/?search={name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch data"}
