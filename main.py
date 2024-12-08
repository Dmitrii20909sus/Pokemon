import telebot
from config import token
from logic import Pokemon, Wizard, Fighter
from random import randint, choice

bot = telebot.TeleBot(token) 
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message, """
 /go - create a pokemon
 /fight - fight with an other pokemon
 /train - train your pokemon
 /feed - feed your pokemon
 /show - show your pokemon statistics                   
""")
@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)


        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
     
        if pokemon.rarity == "Легендарный":
            bot.send_message(message.chat.id, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA LEOOOOON!!!!!!!! LEON!!!!!!!! AAAAAAAAAAAAAAAAA")
            bot.send_photo(message.chat.id, pokemon.show_img()) 
            bot.send_photo(message.chat.id, open('OIP.jpg', 'rb'))
            bot.send_message(message.chat.id, " JOOOOOHN CEEEENAAAAAA")
            bot.send_photo(message.chat.id, pokemon.show_img()) 
            bot.send_photo(message.chat.id, open('456841065-min-1200x834.jpg', 'rb'))
            bot.send_photo(message.chat.id, pokemon.show_img()) 
            bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=WPZ6BR9w-qg&t=10s")
            bot.send_photo(message.chat.id, open('john-cena-1553-x-1336-picture-ve1c97sbz4cg9wpw.jpg', 'rb'))
            bot.send_message(message.chat.id, " JOOOOOHN CEEEENAAAAAA") 
            bot.send_photo(message.chat.id, open('th.jpg', 'rb'))
            bot.send_photo(message.chat.id, pokemon.show_img()) 
            bot.send_message(message.chat.id, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA LEOOOOON!!!!!!!! LEON!!!!!!!! AAAAAAAAAAAAAAAAA")  
            bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=aVB1EY3w3lc&t=52s")  
            bot.send_message(message.chat.id, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA LEOOOOON!!!!!!!! LEON!!!!!!!! AAAAAAAAAAAAAAAAA")
            bot.send_photo(message.chat.id, pokemon.show_img()) 
            bot.send_photo(message.chat.id, open('OIP.jpg', 'rb'))
            bot.send_message(message.chat.id, " JOOOOOHN CEEEENAAAAAA")
            bot.send_photo(message.chat.id, pokemon.show_img()) 
            bot.send_photo(message.chat.id, open('456841065-min-1200x834.jpg', 'rb'))
            bot.send_photo(message.chat.id, pokemon.show_img()) 
            bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=WPZ6BR9w-qg&t=10s")
            bot.send_photo(message.chat.id, open('john-cena-1553-x-1336-picture-ve1c97sbz4cg9wpw.jpg', 'rb'))
            bot.send_message(message.chat.id, " JOOOOOHN CEEEENAAAAAA") 
            bot.send_photo(message.chat.id, open('th.jpg', 'rb'))
            bot.send_photo(message.chat.id, pokemon.show_img()) 
            bot.send_message(message.chat.id, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA LEOOOOON!!!!!!!! LEON!!!!!!!! AAAAAAAAAAAAAAAAA")  
            bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=aVB1EY3w3lc&t=52s")  

    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['fight'])
def start_fight(message):
    if message.from_user.username in Pokemon.pokemons:
        player_pokemon = Pokemon.pokemons[message.from_user.username]

        
        enemy_classes = [Pokemon, Wizard, Fighter]
        enemy_class = choice(enemy_classes)
        enemy_pokemon = enemy_class("Случайный противник")

        bot.send_message(message.chat.id, f"Ваш покемон:\n{player_pokemon.info()}")
        bot.send_photo(message.chat.id, player_pokemon.show_img())
        bot.send_message(message.chat.id, f"Противник:\n{enemy_pokemon.info()}")
        bot.send_photo(message.chat.id, enemy_pokemon.show_img())


        round_counter = 1
        while player_pokemon.health > 0 and enemy_pokemon.health > 0:
            bot.send_message(message.chat.id, f"Раунд {round_counter}!")


            bot.send_message(message.chat.id, f"{player_pokemon.name} атакует {enemy_pokemon.name}!")
            enemy_pokemon.health -= player_pokemon.power
            if enemy_pokemon.health <= 0:
                bot.send_message(message.chat.id, f"Ваш {player_pokemon.name} победил {enemy_pokemon.name}!")
                return

          
            bot.send_message(message.chat.id, f"{enemy_pokemon.name} атакует {player_pokemon.name}!")
            player_pokemon.health -= enemy_pokemon.power
            if player_pokemon.health <= 0:
                bot.send_message(message.chat.id, f"{enemy_pokemon.name} победил вашего {player_pokemon.name}!")
                return

            round_counter += 1
            bot.send_message(message.chat.id, f"{player_pokemon.name}: {player_pokemon.health} здоровья")
            bot.send_message(message.chat.id, f"{enemy_pokemon.name}: {enemy_pokemon.health} здоровья")

@bot.message_handler(commands=["train"])
def train(message):
    if message.from_user.username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[message.from_user.username]
        
       
        increase_power = randint(10, 25)
        increase_health = randint(1, 6)
        pokemon.power += increase_power
        pokemon.health -= increase_health

        bot.send_message(
            message.chat.id,
            f"Ваш покемон {pokemon.name} потренировался! 💪\n"
           
            f"Текущие характеристики:\n"
            f"Сила: {pokemon.power}, Здоровье: {pokemon.health}"
        )
    else:
        bot.send_message(
            message.chat.id,
            "У вас пока нет покемона. Введите /go, чтобы создать его!"
        )

@bot.message_handler(commands=["feed"])
def feed(message):
    if message.from_user.username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[message.from_user.username]
        

        restored_health = randint(20, 50)
        pokemon.health += restored_health

        bot.send_message(
            message.chat.id,
            f"Ваш покемон {pokemon.name} поел! 🍎\n"
            f"⬆️ Здоровье восстановилось на {restored_health}!\n"
            f"Текущее здоровье: {pokemon.health}"
        )
    else:
        bot.send_message(
            message.chat.id,
            "У вас пока нет покемона. Введите /go, чтобы создать его!"
        )

@bot.message_handler(commands=["show"])
def show_pokemon(message):
    if message.from_user.username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[message.from_user.username]
        

        bot.send_message(
            message.chat.id,
            f"👾 Ваш покемон:\n"
            f"Имя: {pokemon.name}\n"
            f"Способность: {pokemon.abilities}\n"
            f"Редкость: {pokemon.rarity}\n"
            f"Здоровье: {pokemon.health}\n"
            f"Атака: {pokemon.power}"
        )
        
        
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.send_message(
            message.chat.id,
            "У вас пока нет покемона. Введите /go, чтобы создать его!"
        )
bot.infinity_polling(none_stop=True)