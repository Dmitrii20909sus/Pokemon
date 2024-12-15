from random import randint, choice
import requests
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(900, 1000) 
        self.abilities = self.get_abilities()
        self.img = self.get_img()
        self.name = self.get_name()
        self.rarity = self.get_rarity()
        self.health = self.get_health()
        self.power = self.get_power()
        self.last_fed = datetime.now() - timedelta(minutes=16)
        Pokemon.pokemons[pokemon_trainer] = self

    def attack(self, enemy):
        if enemy.health > self.power:
            enemy.health -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.health = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!"

    def get_abilities(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            if response.status_code == 200:
                data = response.json()
                return data['abilities'][0]['ability']['name']
        except requests.exceptions.RequestException:
            return "Неизвестная способность"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            if response.status_code == 200:
                data = response.json()
                return data['sprites']['front_shiny']
        except requests.exceptions.RequestException:
            return "th.jpg" 

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            if response.status_code == 200:
                data = response.json()
                return data['forms'][0]['name']
        except requests.exceptions.RequestException:
            return f"Pokemon#{self.pokemon_number}"

    def get_rarity(self):
        if self.pokemon_number <= 300:
            return "Редкий"
        elif self.pokemon_number <= 720:
            return "Сверхредкий"
        elif self.pokemon_number <= 900:
            return "Эпический"
        else:
            return "Легендарный"

    def get_health(self):
        if self.rarity == "Легендарный":
            return randint(150, 250)
        elif self.rarity == "Эпический":
            return randint(120, 200)
        else:
            return randint(80, 150)

    def get_power(self):
        if self.rarity == "Легендарный":
            return randint(100, 150)
        elif self.rarity == "Эпический":
            return randint(80, 120)
        elif self.rarity == "Сверхредкий":
            return randint(60, 100)
        else:
            return randint(50, 80)

    def info(self):
        return (f"Имя: {self.name}, Способность: {self.abilities}, "
                f"Редкость: {self.rarity}, Здоровье: {self.health}, Атака: {self.power}")

    def show_img(self):
        return self.img
    def can_feed(self):
        time_since_last_fed = datetime.now() - self.last_fed
        return time_since_last_fed >= timedelta(minutes=15)
    
    def feed(self):
     now = datetime.now()
     feed_interval = timedelta(minutes=15) 
     next_feed_time = self.last_fed + feed_interval

     if now >= next_feed_time:
        self.last_fed = now
        health_increase = randint(20, 40)  
        self.health += health_increase
        return health_increase, None 
     else:
        remaining_time = next_feed_time - now
        return None, remaining_time 

class Fighter(Pokemon):
    def feed(self):
        now = datetime.now()
        feed_interval = timedelta(minutes=15) 
        next_feed_time = self.last_fed + feed_interval

        if now >= next_feed_time:
            self.last_fed = now
            health_increase = randint(40, 70)
            self.health += health_increase
            return health_increase, None
        else:
            remaining_time = next_feed_time - now
            return None, remaining_time

class Wizard(Pokemon):
    def feed(self):
        now = datetime.now()
        feed_interval = timedelta(minutes=15)
        next_feed_time = self.last_fed + feed_interval

        if now >= next_feed_time:
            self.last_fed = now
            health_increase = randint(20, 40)
            self.health += health_increase
            return health_increase, None
        else:
            remaining_time = next_feed_time - now
            return None, remaining_time