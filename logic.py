from random import randint
import requests

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)
        self.abilities = self.get_abilities()
        self.img = self.get_img()
        self.name = self.get_name()
        self.rarity = self.get_rarity()

        Pokemon.pokemons[pokemon_trainer] = self

    def get_abilities(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data['abilities'][0]['ability']['name']
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data['sprites']['front_shiny']
        except requests.exceptions.RequestException as e:
            return "th.jpg"

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data['forms'][0]['name']
        except requests.exceptions.RequestException as e:
            return "Pikachu"

    def get_rarity(self):
        if self.pokemon_number <= 100:
            return "Редкий"
        elif self.pokemon_number <= 500:
            return "Сверхредкий"
        elif self.pokemon_number <= 900:
            return "Эпический"
        else:
            return "ЛЕГА ААААА"

    def info(self):
        return f"Имя твоего покемона: {self.name}, способность: {self.abilities}, редкость: {self.rarity}"

    def show_img(self):
            return self.img

    def get_music(self):
        if self.rarity == "ЛЕГА ААААА":
            return "https://www.youtube.com/watch?v=UbQKpQ7n2Mw"
        else:
            return None
