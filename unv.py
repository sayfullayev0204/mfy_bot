import telebot
from telebot import types

TOKEN = '7081823411:AAGiyFtPzMbYwdkIQMTXxqCBk6lCgq4DH8w'
bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['admin'])
def help(message):
    bot.send_message(message.chat.id, "Savollar bo'lsa @sayfullayev_0204 ga yozing")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("MFY haqida 🏠")
    btn2 = types.KeyboardButton("Bog'chalar 🚸")
    btn4 = types.KeyboardButton("O'quv markazlar 📚")
    btn5 = types.KeyboardButton("Restoran/Cafelar 🍴")
    btn6 = types.KeyboardButton("Avto servislar 🚗")
    btn7 = types.KeyboardButton("Bozor 🛒")
    markup.add(btn1, btn2, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id, "Assalomu alaykum! Quyidagi bo'limlardan birini tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Bozor 🛒")
def mfy_info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Elon berish 📄")
    btn2 = types.KeyboardButton("Harid qilish 🛍️")
    btn3 = types.KeyboardButton("ortga 🔙")
    markup.add(btn1, btn2,btn3)
    bot.send_message(message.chat.id, "MFY haqida qanday ma'lumotga ega bo'lishni xohlaysiz?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Harid qilish 🛍️")
def mfy_raisi(message):
    bot.send_photo(message.chat.id, photo=open('shop.jpg', 'rb'), caption="MFY ning telegramdagi online bozori bu yerda: https://t.me/testalibek")

@bot.message_handler(func=lambda message: message.text == "Elon berish 📄")
def send_welcome(message):
    try:
        msg = bot.reply_to(message, "Salom! Ismingizni kiriting, iltimos: \nmasalan: Alibek")
        bot.register_next_step_handler(msg, ask_name)
    except Exception as e:
        print(e)

def ask_name(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user_data[chat_id] = {'name': name}
        msg = bot.reply_to(message, 'Rahmat! Endi telefon raqamingizni kiriting: \nmasalan: +998911234567')
        bot.register_next_step_handler(msg, ask_phone)
    except Exception as e:
        print(e)

def ask_phone(message):
    try:
        chat_id = message.chat.id
        phone = message.text
        user_data[chat_id]['phone'] = phone
        msg = bot.reply_to(message, 'Iltimos, elon nomini kiriting:\nmasalan: telefon')
        bot.register_next_step_handler(msg, ask_advert_name)
    except Exception as e:
        print(e)

def ask_advert_name(message):
    try:
        chat_id = message.chat.id
        advert_name = message.text
        user_data[chat_id]['advert_name'] = advert_name
        msg = bot.reply_to(message, 'Iltimos, elon narxini kiriting: \nmasalan: 200 000 so\'m')
        bot.register_next_step_handler(msg, ask_price)
    except Exception as e:
        print(e)

def ask_price(message):
    try:
        chat_id = message.chat.id
        price = message.text
        user_data[chat_id]['price'] = price
        msg = bot.reply_to(message, 'Elon rasmini yuboring: \nshu elonga tegishli rasmni jo\'nating')
        bot.register_next_step_handler(msg, send_to_channel)
    except Exception as e:
        print(e)

@bot.message_handler(content_types=['photo'])
def send_to_channel(message):
    try:
        chat_id = message.chat.id
        if chat_id in user_data:
            advert_data = user_data.pop(chat_id)
            advert_text = f"Ism: {advert_data['name']}\nTelefon: {advert_data['phone']}\nElon nomi: {advert_data['advert_name']}\nNarxi: {advert_data['price']}"
            bot.send_photo("@testalibek", message.photo[-1].file_id, caption=advert_text)
            bot.send_message(chat_id, "Eloningiz muvaffaqiyatli kanalga yuborildi. 😊 \n xabarni ushbu kanalda ko\'rasiz: @testalibek")
        else:
            bot.send_message(chat_id, "Kechirasiz, qandaydir xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
    except Exception as e:
        print(e)


# "MFY haqida" bosilganda
@bot.message_handler(func=lambda message: message.text == "MFY haqida 🏠")
def mfy_info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("MFY Raisi 👨🏻‍💼")
    btn2 = types.KeyboardButton("MFY noziri 👮🏻‍♂️")
    btn3 = types.KeyboardButton("Yoshlar yetakchisi 👨🏻‍💻")
    btn4 = types.KeyboardButton("Manzil 📍")
    btn5 = types.KeyboardButton("ortga 🔙")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, "MFY haqida qanday ma'lumotga ega bo'lishni xohlaysiz?", reply_markup=markup)

# "MFY Raisi" bosilganda
@bot.message_handler(func=lambda message: message.text == "MFY Raisi 👨🏻‍💼")
def mfy_raisi(message):
    bot.send_photo(message.chat.id, photo=open('a.png', 'rb') , caption="Alibek Valiyev \nTEL: +998912223332")

@bot.message_handler(func=lambda message: message.text == "MFY noziri 👮🏻‍♂️")
def mfy_raisi(message):
    bot.send_photo(message.chat.id, photo=open('a.png', 'rb'), caption="Alibek Valiyev \nTEL: +998912223332")

@bot.message_handler(func=lambda message: message.text == "Yoshlar yetakchisi 👨🏻‍💻")
def mfy_raisi(message):
    bot.send_photo(message.chat.id, photo=open('a.png', 'rb'), caption="Alibek Valiyev \nTEL: +998912223332")

@bot.message_handler(func=lambda message: message.text == "Manzil 📍")
def mfy_raisi(message):
    if message.text == "Manzil 📍":
        bot.send_location(message.chat.id, 38.825079, 65.717177)




@bot.message_handler(func=lambda message: message.text == "Bog'chalar 🚸")
def bogchalar(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ortga 🔙")
    btn2 = types.KeyboardButton("Bog'cha 1")
    btn3 = types.KeyboardButton("Bog'cha 2")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_photo(message.chat.id, photo=open('bog.jpg', 'rb'), caption="MFYda mavjud Bog'chalar ro'yxati!")
    bot.send_message(message.chat.id,"Pastagi menudagi bog\'chalardan birin tanlang.",  reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Bog'cha 1")
def bogcha(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn4 = types.KeyboardButton("Manzil📍")
    btn = types.KeyboardButton("orqaga🔙")
    markup.add( btn4, btn)
    bot.send_photo(message.chat.id, photo=open('a.png', 'rb'), caption="Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium cumque eligendi ut neque aliquam vitae, \n TEL: +998912223332 ", reply_markup=markup)
   
@bot.message_handler(func=lambda message: message.text == "Bog'cha 2")
def bogcha(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn4 = types.KeyboardButton("Manzil📍")
    btn = types.KeyboardButton("orqaga🔙")
    markup.add( btn4, btn)
    bot.send_photo(message.chat.id, photo=open('a.png', 'rb'), caption="Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium cumque eligendi ut neque aliquam vitae, \n TEL: +998912223332 ", reply_markup=markup)
   

@bot.message_handler(func=lambda message: message.text == "Manzil📍")
def bogcha(message):
    if message.text == "Manzil📍":
        bot.send_location(message.chat.id, 39.825079, 65.717177)

@bot.message_handler(func=lambda message: message.text.lower() == "orqaga🔙")
def go_back(message):
    bogchalar(message)

@bot.message_handler(func=lambda message: message.text == "Avto servislar 🚗")
def Serivces(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("MegaService")
    btn5 = types.KeyboardButton("ortga 🔙")
    markup.add(btn1, btn5)
    bot.send_message(message.chat.id, "MFYda mavjuda AvtoServislar ro'yxati", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "MegaService")
def bogcha(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn4 = types.KeyboardButton("servis manzil📍")
    btn = types.KeyboardButton("🔙")
    markup.add( btn4, btn)
    bot.send_photo(message.chat.id, photo=open('a.png', 'rb'), caption="Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium cumque eligendi ut neque aliquam vitae, \n TEL: +998912223332 ", reply_markup=markup)
    

@bot.message_handler(func=lambda message: message.text == "servis manzil📍")
def bogcha(message):
    if message.text == "servis manzil📍":
        bot.send_location(message.chat.id, 39.825079, 65.717177)

@bot.message_handler(func=lambda message: message.text.lower() == "🔙")
def go_back(message):
    Serivces(message)

@bot.message_handler(func=lambda message: message.text.lower() == "ortga 🔙")
def go_back(message):
    start(message)

# Botni ishga tushurish
bot.polling()