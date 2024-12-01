import telebot
from config import token
from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)


        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
     
        if pokemon.rarity == "ЛЕГА ААААА":
            bot.send_message(message.chat.id, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA LEOOOOON!!!!!!!! LEON!!!!!!!! AAAAAAAAAAAAAAAAA")
            bot.send_photo(message.chat.id, pokemon.show_img()) 
            bot.send_photo(message.chat.id, open('OIP.jpg', 'rb'))
            bot.send_message(message.chat.id, " JOOOOOHN CEEEENAAAAAA")
            bot.send_photo(message.chat.id, pokemon.show_img()) 
            bot.send_photo(message.chat.id, open('456841065-min-1200x834.jpg', 'rb'))
            bot.send_photo(message.chat.id, pokemon.show_img()) 
            bot.send_photo(message.chat.id, open('john-cena-1553-x-1336-picture-ve1c97sbz4cg9wpw.jpg', 'rb'))
            bot.send_message(message.chat.id, " JOOOOOHN CEEEENAAAAAA") 
            bot.send_photo(message.chat.id, open('th.jpg', 'rb'))
            bot.send_photo(message.chat.id, pokemon.show_img()) 
            bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=WPZ6BR9w-qg&t=10s")
            bot.send_message(message.chat.id, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA LEOOOOON!!!!!!!! LEON!!!!!!!! AAAAAAAAAAAAAAAAA")  
            bot.send_photo(message.chat.id, pokemon.show_img())
            bot.send_photo(message.chat.id, open('R.jpg', 'rb'))
            bot.send_message(message.chat.id, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA LEOOOOON!!!!!!!! LEON!!!!!!!! AAAAAAAAAAAAAAAAA")
            bot.send_photo(message.chat.id, pokemon.show_img())
            bot.send_photo(message.chat.id, open('456841065-min-1200x834.jpg', 'rb'))
            bot.send_photo(message.chat.id, open('OIP.jpg', 'rb'))
            bot.send_message(message.chat.id, " JOOOOOHN CEEEENAAAAAA")
            bot.send_photo(message.chat.id, open('john-cena-1553-x-1336-picture-ve1c97sbz4cg9wpw.jpg', 'rb'))
            bot.send_photo(message.chat.id, open('th.jpg', 'rb'))
            bot.send_photo(message.chat.id, pokemon.show_img())
            bot.send_message(message.chat.id, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=aVB1EY3w3lc&t=52s")  
            

    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

bot.infinity_polling(none_stop=True)