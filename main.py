from config import TOKEN
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telebot import types
import telebot
bot = TeleBot(TOKEN)
    
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Огэ")
    btn2 = types.KeyboardButton("Егэ")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот для подготовке к экзаменам. Выбери экзамен:".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Привет"):
        bot.send_message(message.chat.id, text="Привеет..)")
    elif(message.text == "Огэ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Математика")
        btn2 = types.KeyboardButton("Русский язык писм.")
        btn4 = types.KeyboardButton("Информатика")
        btn5 = types.KeyboardButton("Английский язык")
        btn9 = types.KeyboardButton("Физика")
        btn10 = types.KeyboardButton("Химия")
        btn11 = types.KeyboardButton("Биология")
        btn12 = types.KeyboardButton("География")
        btn13 = types.KeyboardButton("Обществознание")
        btn14 = types.KeyboardButton("Литература")
        btn15 = types.KeyboardButton("История")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn4, btn5, btn9, btn10, btn11, btn12, btn13, btn14, btn15, back)
        bot.send_message(message.chat.id, text="выбери предмет:", reply_markup=markup)
    
    elif(message.text == "Математика"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        M1_5 = types.KeyboardButton("№1-5_Математика_ОГЭ")
        M6 = types.KeyboardButton("№6_Математика_ОГЭ")
        M7 = types.KeyboardButton("№7_Математика_ОГЭ")
        M8 = types.KeyboardButton("№8_Математика_ОГЭ")
        M9 = types.KeyboardButton("№9_Математика_ОГЭ")
        M10 = types.KeyboardButton("№10_Математика_ОГЭ")
        M11 = types.KeyboardButton("№11_Математика_ОГЭ")
        M12 = types.KeyboardButton("№12_Математика_ОГЭ")
        M13 = types.KeyboardButton("№13_Математика_ОГЭ")
        M14 = types.KeyboardButton("№14_Математика_ОГЭ")
        M15 = types.KeyboardButton("№15_Математика_ОГЭ")
        M16 = types.KeyboardButton("№16_Математика_ОГЭ")
        M17 = types.KeyboardButton("№17_Математика_ОГЭ")
        M18 = types.KeyboardButton("№18_Математика_ОГЭ")
        M19 = types.KeyboardButton("№19_Математика_ОГЭ")
        M20 = types.KeyboardButton("№20_Математика_ОГЭ")
        M21 = types.KeyboardButton("№21_Математика_ОГЭ")
        M22 = types.KeyboardButton("№22_Математика_ОГЭ")
        M23 = types.KeyboardButton("№23_Математика_ОГЭ")
        M24 = types.KeyboardButton("№24_Математика_ОГЭ")
        M25 = types.KeyboardButton("№25_Математика_ОГЭ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(M1_5, M6, M7, M8, M9, M10, M11, M12, M13, M14, M15, M16, M17, M18, M19, M20, M21, M22, M23, M24, M25, back)
        bot.send_message(message.chat.id, "выбери задание:", reply_markup=markup)

    elif (message.text == "№1-5_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор заданий 1-5](https://rutube.ru/video/ead65c8f1a5ab0c4d3e4c3405afe6d16/)', parse_mode='Markdown')
        markup.add(back)
    
    elif (message.text == "№6_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 6](https://rutube.ru/video/d48089f8bba1519e9a575ebb35fdb399/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№7_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 7](https://rutube.ru/video/0103967ec097f9c3459120b3fed62c6f/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№8_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 8](https://rutube.ru/video/cdc6b147992dac13462f28298781f441/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№9_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 9](https://rutube.ru/video/5de7fe83e334280b48e4d3eecdc2bc5a/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№10_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 10](https://rutube.ru/video/a94c401e41854eece3cc321ea8f09fc2/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№11_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 11](https://rutube.ru/video/fbf135808176c7fda912a8f13b739a71/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№12_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 12](https://rutube.ru/video/d99b125444e71815279642622330af3f/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№13_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 13](https://rutube.ru/video/2582973b5d0f21973f41000cf276a18a/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№14_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 14](https://rutube.ru/video/3b6234e3a246a5103f94016ef8705af2/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№15_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 15](https://rutube.ru/video/f60d58c1d6a9e0f7610e2da17e4e880f/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№16_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 16](https://rutube.ru/video/83fd24669e3e9fd912a497d1e6050e9f/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№17_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 17](https://rutube.ru/video/f1c72cb83587ea05ed83aace2f5a47f9/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№18_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 18](https://rutube.ru/video/9fe7e087b36627e6b7455836d844d799/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№19_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 19](https://rutube.ru/video/ee154643b286f1ce9049e575a8882b44/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№20_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 20](https://rutube.ru/video/53e783d1774d0f2b277b099da228e1b9/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№21_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 21](https://rutube.ru/video/61c30f713e2cd6ade0035398e9efc821/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№22_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 22](https://rutube.ru/video/2bea4de1b63ed6fd21bc40f37ab2cb65/)', parse_mode='Markdown')
        markup.add(back)     

    elif (message.text == "№23_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 23](https://rutube.ru/video/3a2a3929d15d4f9994c0f5c8ce42d65d/)', parse_mode='Markdown')
        markup.add(back) 

    elif (message.text == "№24_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 24](https://rutube.ru/video/9bc72c04bf65693d683582015bfe23c4/)', parse_mode='Markdown')
        markup.add(back) 

    elif (message.text == "№25_Математика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 25](https://rutube.ru/video/9af5b7b67ea567436e882db2a2902d58/)', parse_mode='Markdown')
        markup.add(back) 

    elif message.text == "Русский язык писм.":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        RP1 = types.KeyboardButton("№1_Русский язык писм._ОГЭ")
        RP2_3 = types.KeyboardButton("№2-3_Русский язык писм._ОГЭ")
        RP4 = types.KeyboardButton("№4_Русский язык писм._ОГЭ")
        RP5 = types.KeyboardButton("№5_Русский язык писм._ОГЭ")
        RP6_7 = types.KeyboardButton("№6-7_Русский язык писм._ОГЭ")
        RP8 = types.KeyboardButton("№8_Русский язык писм._ОГЭ")
        RP9 = types.KeyboardButton("№9_Русский язык писм._ОГЭ")
        RP10 = types.KeyboardButton("№10_Русский язык писм._ОГЭ")
        RP11 = types.KeyboardButton("№11_Русский язык писм._ОГЭ")
        RP12 = types.KeyboardButton("№12_Русский язык писм._ОГЭ")
        RP13 = types.KeyboardButton("№13_Русский язык писм._ОГЭ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(RP1, RP2_3, RP4, RP5, RP6_7, RP8, RP9, RP10, RP11, RP12, RP13, back)
        bot.send_message(message.chat.id, "выбери задание:", reply_markup=markup)

    elif (message.text == "№1_Русский язык писм._ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 1](https://rutube.ru/video/5381ea1e03f366ba5b49b7dcc1c3087f/)', parse_mode='Markdown')
        markup.add(back) 

    elif (message.text == "№2-3_Русский язык писм._ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 2-3](https://rutube.ru/video/b867e10b13c58e8e11d02e2ac87717a2/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№4_Русский язык писм._ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 4](https://rutube.ru/video/7a17c44296bdb4f290430269c86d6144/)', parse_mode='Markdown')
        markup.add(back) 

    elif (message.text == "№5_Русский язык писм._ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 5](https://rutube.ru/video/6d9aa9994c398056daf14cf83efcfa09/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№6-7_Русский язык писм._ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 6-7](https://rutube.ru/video/d07798818c6eb1e0d0e29f936d8d375b/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№8_Русский язык писм._ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 8](https://rutube.ru/video/28a43da489f1385149162d69fc8f4186/)', parse_mode='Markdown')
        markup.add(back)  

    elif (message.text == "№9_Русский язык писм._ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 9](https://rutube.ru/video/d2b8a9888a18d71ab04f5d94e303c928/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№10_Русский язык писм._ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 10](https://rutube.ru/video/30de40359a1f2f23c7c08f185b3d6a4f/)', parse_mode='Markdown')
        markup.add(back) 

    elif (message.text == "№11_Русский язык писм._ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 11](https://rutube.ru/video/0d1af21c8c0fb4e5cadb886edcf3d589/)', parse_mode='Markdown')
        markup.add(back) 

    elif (message.text == "№12_Русский язык писм._ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 12](https://rutube.ru/video/9760f181fe7e851240f18b93531bf81e/)', parse_mode='Markdown')
        markup.add(back) 

    elif (message.text == "№13_Русский язык писм._ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 13](https://rutube.ru/video/3bb42e36926e0e1b0b93be24bb3690a2/)', parse_mode='Markdown')
        markup.add(back)

    elif message.text == "Информатика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        I1 = types.KeyboardButton("№1_Информатика_ОГЭ")
        I2 = types.KeyboardButton("№2_Информатика_ОГЭ")
        I3 = types.KeyboardButton("№3_Информатика_ОГЭ")
        I4 = types.KeyboardButton("№4_Информатика_ОГЭ")
        I5 = types.KeyboardButton("№5_Информатика_ОГЭ")
        I6 = types.KeyboardButton("№6_Информатика_ОГЭ")
        I7 = types.KeyboardButton("№7_Информатика_ОГЭ")
        I8 = types.KeyboardButton("№8_Информатика_ОГЭ")
        I9 = types.KeyboardButton("№9_Информатика_ОГЭ")
        I10 = types.KeyboardButton("№10_Информатика_ОГЭ")
        I11 = types.KeyboardButton("№11_Информатика_ОГЭ")
        I12 = types.KeyboardButton("№12_Информатика_ОГЭ")
        I13 = types.KeyboardButton("№13_Информатика_ОГЭ")
        I14 = types.KeyboardButton("№14_Информатика_ОГЭ")
        I15 = types.KeyboardButton("№15_Информатика_ОГЭ")
        I16 = types.KeyboardButton("№16_Информатика_ОГЭ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(I1, I2, I3, I4, I5, I6, I7, I8, I9, I10, I11, I12, I13, I14, I15, I16, back)
        bot.send_message(message.chat.id, "выбери задание:", reply_markup=markup)

    elif (message.text == "№1_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 1](https://rutube.ru/video/02cc7d3702c8d2c91cca0551e690a403/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№2_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 2](https://rutube.ru/video/d54de8fb0caa0338bd7acf8579954bf5/)', parse_mode='Markdown')
        markup.add(back)
    
    elif (message.text == "№3_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 3](https://rutube.ru/video/27976bc130d97d71335ae8e19cb51564/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№4_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 4](https://rutube.ru/video/86a7eb4ea7bc074823dfea1d5bcf3e72/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№5_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 5](https://rutube.ru/video/59c2bfecde3ffd39746e8a878e1c80a3/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№6_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 6](https://rutube.ru/video/33b4a319a2b7d965981e75caa08e76b6/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№7_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 7](https://rutube.ru/video/a0d990963cc5993465eb89c8095506cb/)', parse_mode='Markdown')
        markup.add(back)
        
    elif (message.text == "№8_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 8](https://rutube.ru/video/1e923a3edbf0500bb610b9037321fee2/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№9_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 9](https://rutube.ru/video/ec4bde02fbf226f0b2121f36c30357a4/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№10_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 10](https://rutube.ru/video/f62033329ab90ce2af109c1083d1e5d8/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№11_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 11](https://rutube.ru/video/fb8e022d788b085f0ef7e0011f5efe23/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№12_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 12](https://rutube.ru/video/78246f9e62a69f0fa0221e43f09c3646/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№13_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 13](https://rutube.ru/video/07c9827f3b75a371be99a7ce12913233/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№14_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 14](https://rutube.ru/video/bc95d6d320c5c18d33e3db0b02d81163/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№15_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 15](https://rutube.ru/video/0dcd82a2cba1585d7ea15a2fc50fffb6/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№16_Информатика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 16](https://rutube.ru/video/5181f8a02807d59976fbd6112da5c29c/)', parse_mode='Markdown')
        markup.add(back)

    elif message.text == "Английский язык":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        E1 = types.KeyboardButton("разбор всех заданий_Английский язык_ОГЭ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(E1, back)
        bot.send_message(message.chat.id, "выбери задание:", reply_markup=markup)

    elif (message.text == "разбор всех заданий_Английский язык_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор всех заданий](https://vkvideo.ru/video-184095735_456249043?ref_domain=yastatic.net)', parse_mode='Markdown')
        markup.add(back)

    elif message.text == "Физика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        F1 = types.KeyboardButton("№1-5_Физика_ОГЭ")
        E6 = types.KeyboardButton("№6_Физика_ОГЭ")
        E7 = types.KeyboardButton("№7_Физика_ОГЭ")
        E8 = types.KeyboardButton("№8_Физика_ОГЭ")
        E9 = types.KeyboardButton("№9_Физика_ОГЭ")
        E10 = types.KeyboardButton("№10_Физика_ОГЭ")
        E11 = types.KeyboardButton("№11_Физика_ОГЭ")
        E12 = types.KeyboardButton("№12_Физика_ОГЭ")
        E13 = types.KeyboardButton("№13_Физика_ОГЭ")
        E14 = types.KeyboardButton("№14_Физика_ОГЭ")
        E15 = types.KeyboardButton("№15_Физика_ОГЭ")
        E16 = types.KeyboardButton("№16_Физика_ОГЭ")
        E17 = types.KeyboardButton("№17_Физика_ОГЭ")
        E18 = types.KeyboardButton("№18_Физика_ОГЭ")
        E19_20 = types.KeyboardButton("№19-20_Физика_ОГЭ")
        E21_22 = types.KeyboardButton("№21-22_Физика_ОГЭ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(F1, E6, E7, E8, E9, E10, E11, E12, E13, E14, E15, E16, E17, E18, E19_20, E21_22, back)
        bot.send_message(message.chat.id, "выбери задание:", reply_markup=markup)

    elif (message.text == "№1-5_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 1 и 5](https://rutube.ru/video/6c1cba33baa36c4b96692f772bd99182/?&utm_source=embed&utm_medium=referral&utm_campaign=logo&utm_content=6c1cba33baa36c4b96692f772bd99182&utm_term=yastatic.net%2F&referrer=appmetrica_tracking_id%3D1037600761300671389%26ym_tracking_id%3D12089387566106007575)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№6_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 6](https://rutube.ru/video/7caa8b3960c62d672bc9f9d3fe876e01/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№7_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 7](https://rutube.ru/video/fb9cd492524ec6556ef89c513b2e23ca/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№8_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 8](https://rutube.ru/video/7e3ed8412365c18e2262616ebe46476c/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№9_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 9](https://rutube.ru/video/e0d59f4f48f0e44aab5d395dc251af5e/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№10_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 10](https://rutube.ru/video/b893db6cc8a58ca7bdda74f8df1ab492/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№11_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 11](https://rutube.ru/video/d44a7086d837f61290570f06487838e3/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№12_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 12](https://rutube.ru/video/32495dd8b454dcae9b9196bf5d3ee9db/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№13_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 13](https://rutube.ru/video/32495dd8b454dcae9b9196bf5d3ee9db/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№14_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 14](https://rutube.ru/video/c798e8d30d3e2d3a090c69b8ed8f99cc/?&utm_source=embed&utm_medium=referral&utm_campaign=logo&utm_content=c798e8d30d3e2d3a090c69b8ed8f99cc&utm_term=yastatic.net%2F&referrer=appmetrica_tracking_id%3D1037600761300671389%26ym_tracking_id%3D2092084270573016738)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№15_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 15](https://rutube.ru/video/b0df5c2092bf88b1216489910b62e8cc/?&utm_source=embed&utm_medium=referral&utm_campaign=logo&utm_content=b0df5c2092bf88b1216489910b62e8cc&utm_term=yastatic.net%2F&referrer=appmetrica_tracking_id%3D1037600761300671389%26ym_tracking_id%3D15809098077351468154)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№16_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 16](https://rutube.ru/video/fb0d65e4ec5d0207fdc4f4bd09b29144/?&utm_source=embed&utm_medium=referral&utm_campaign=logo&utm_content=fb0d65e4ec5d0207fdc4f4bd09b29144&utm_term=yastatic.net%2F&referrer=appmetrica_tracking_id%3D1037600761300671389%26ym_tracking_id%3D7782523435803287461)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№17_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 17](https://rutube.ru/video/d29039538731b5f48cd7e0a0efdeb0a4/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№18_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 18](https://rutube.ru/video/65777ac367b09ad3cf0177cfca247bdd/?&utm_source=embed&utm_medium=referral&utm_campaign=logo&utm_content=65777ac367b09ad3cf0177cfca247bdd&utm_term=yastatic.net%2F&referrer=appmetrica_tracking_id%3D1037600761300671389%26ym_tracking_id%3D12981176785117094553)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№19-20_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 19 и 20](https://rutube.ru/video/d63dd4659433bc484bd00d725079df75/?&utm_source=embed&utm_medium=referral&utm_campaign=logo&utm_content=d63dd4659433bc484bd00d725079df75&utm_term=yastatic.net%2F&referrer=appmetrica_tracking_id%3D1037600761300671389%26ym_tracking_id%3D10235392034544309673)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№21-22_Физика_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 20 и 22](https://rutube.ru/video/8d30d4cb9acb263e3a0c35a0fe7a8a4d/)', parse_mode='Markdown')
        markup.add(back)

    elif message.text == "Химия":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        x1 = types.KeyboardButton("№1_Химия_ОГЭ")
        x2 = types.KeyboardButton("№2_Химия_ОГЭ")
        x3 = types.KeyboardButton("№3_Химия_ОГЭ")
        x4 = types.KeyboardButton("№4_Химия_ОГЭ")
        x5 = types.KeyboardButton("№5_Химия_ОГЭ")
        x6 = types.KeyboardButton("№6_Химия_ОГЭ")
        x7 = types.KeyboardButton("№7_Химия_ОГЭ")
        x8 = types.KeyboardButton("№8_Химия_ОГЭ")
        x9 = types.KeyboardButton("№9_Химия_ОГЭ")
        x10 = types.KeyboardButton("№10_Химия_ОГЭ")
        x11 = types.KeyboardButton("№11_Химия_ОГЭ")
        x12 = types.KeyboardButton("№12_Химия_ОГЭ")
        x13 = types.KeyboardButton("№13_Химия_ОГЭ")
        x14 = types.KeyboardButton("№14_Химия_ОГЭ")
        x15 = types.KeyboardButton("№15_Химия_ОГЭ")
        x16 = types.KeyboardButton("№16_Химия_ОГЭ")
        x17 = types.KeyboardButton("№17_Химия_ОГЭ")
        x18 = types.KeyboardButton("№18_Химия_ОГЭ")
        x19 = types.KeyboardButton("№19_Химия_ОГЭ")
        x20 = types.KeyboardButton("№20_Химия_ОГЭ")
        x21 = types.KeyboardButton("№21_Химия_ОГЭ")
        x22 = types.KeyboardButton("№22_Химия_ОГЭ")
        x23 = types.KeyboardButton("№23_Химия_ОГЭ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, back)
        bot.send_message(message.chat.id, "выбери задание:", reply_markup=markup)

    elif (message.text == "№1_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 1](https://rutube.ru/video/d273a78325686500dea8a16df51d887c/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№2_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 3](https://rutube.ru/video/d5ca132fc063a2ab16e3bcbc60c948e8/)', parse_mode='Markdown')
        markup.add(back)
        
    elif (message.text == "№3_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 3](https://rutube.ru/video/8830468d46f297625d0d9e232b128b78/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№4_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 4](https://rutube.ru/video/31df7aff8e3967ef887d2b7ad8cf380a/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№5_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 5](https://rutube.ru/video/241b8308c9244b34af3b43ac3d8c9137/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№6_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 6](https://rutube.ru/video/57c3eac22e46c3dd0999319885f2994b/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№7_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 7](https://rutube.ru/video/abce4f4adacc7d12a186170dc0bfa675/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№8_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 8](https://rutube.ru/video/91d81000a79a9436721dd454a11d8b6a/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№9_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 9](https://rutube.ru/video/1980e813013f4ce822bd7aee24b9861b/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№10_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 10](https://rutube.ru/video/28489e4cd7b71ecdbaff982a3264da1f/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№11_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 11](https://rutube.ru/video/ad3b3e6ef77989fce67109c642cb7095/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№12_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 12](https://rutube.ru/video/4f5d823be3b411813ae812e3035aa411/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№13_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 13](https://rutube.ru/video/93d592eea987d746bdf4e9b426ab2b0a/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№14_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 14](https://rutube.ru/video/81a39107993125dc7ec6a6b3df60f721/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№15_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 15](https://rutube.ru/video/67dd30e4ab8f3459f1e427ea4f90c1ea/)', parse_mode='Markdown')
        markup.add(back)
    
    elif (message.text == "№16_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 16](https://rutube.ru/video/20459792ae91c4a9a7c0182fb0f61c8d/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№17_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 17](https://rutube.ru/video/7bae166b6513aa1727a5b77167ad0b0f/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№18_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 18](https://rutube.ru/video/d5d7ab60629292df4452bd9043ec4d54/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№19_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 19](https://rutube.ru/video/5317d127ef387182a9bbef078dd9e6b7/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№20_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 20](https://rutube.ru/video/24f3334d8add7a6e32da28e162414f16/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№21_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 21](https://rutube.ru/video/36fd345fa377f17d9d16e908d4430c84/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№22_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 22](https://rutube.ru/video/166393e51725175fe3ddb0837366e57c/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№23_Химия_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 23](https://rutube.ru/video/9a8d0df8466641cb469fe86c20709d23/)', parse_mode='Markdown')
        markup.add(back)

    elif message.text == "Биология":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton("№1_Биология_ОГЭ")
        b2 = types.KeyboardButton("№2_Биология_ОГЭ")
        b3 = types.KeyboardButton("№3_Биология_ОГЭ")
        b4 = types.KeyboardButton("№4_Биология_ОГЭ")
        b5 = types.KeyboardButton("№5_Биология_ОГЭ")
        b6 = types.KeyboardButton("№6_Биология_ОГЭ")
        b7 = types.KeyboardButton("№7_Биология_ОГЭ")
        b8 = types.KeyboardButton("№8_Биология_ОГЭ")
        b9 = types.KeyboardButton("№9_Биология_ОГЭ")
        b10 = types.KeyboardButton("№10_Биология_ОГЭ")
        b11 = types.KeyboardButton("№11_Биология_ОГЭ")
        b12 = types.KeyboardButton("№12_Биология_ОГЭ")
        b13 = types.KeyboardButton("№13_Биология_ОГЭ")
        b14 = types.KeyboardButton("№14_Биология_ОГЭ")
        b15 = types.KeyboardButton("№15_Биология_ОГЭ")
        b16 = types.KeyboardButton("№16_Биология_ОГЭ")
        b17 = types.KeyboardButton("№17_Биология_ОГЭ")
        b18 = types.KeyboardButton("№18_Биология_ОГЭ")
        b19 = types.KeyboardButton("№19_Биология_ОГЭ")
        b20 = types.KeyboardButton("№20_Биология_ОГЭ")
        b21 = types.KeyboardButton("№21_Биология_ОГЭ")
        b22 = types.KeyboardButton("№22_Биология_ОГЭ")
        b23 = types.KeyboardButton("№23_Биология_ОГЭ")
        b24 = types.KeyboardButton("№24_Биология_ОГЭ")
        b25 = types.KeyboardButton("№25_Биология_ОГЭ")
        b26 = types.KeyboardButton("№26_Биология_ОГЭ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add( b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, back)
        bot.send_message(message.chat.id, "выбери задание:", reply_markup=markup)

    elif (message.text == "№1_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 1](https://rutube.ru/video/fef0d12b92d6f0cdaffcbd5542d73cf2/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№2_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 2](https://rutube.ru/video/ff335ef5d5a7dcb6f2038632843095dd/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№3_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 3](https://rutube.ru/video/14c310327baf75a9535f90b1c91a6a85/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№4_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 4](https://rutube.ru/video/0ccd8073393efe905cc5723fa38dd81b/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№5_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 5](https://rutube.ru/video/bc62a25f04e72f5641370f960af834f1/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№6_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 6](https://rutube.ru/video/9f52713c23db60e40ffaf31d0d390bff/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№7_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 7](https://rutube.ru/video/8456bd2e9636ce14fbdd2470959cd247/)', parse_mode='Markdown')
        markup.add(back)
    
    elif (message.text == "№8_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 8](https://rutube.ru/video/c69f23064e3b8ff7a8a8cb159864683a/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№9_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 9](https://rutube.ru/video/14e8a8cb4c12422f982c7e9dd7c036e1/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№10_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 10](https://rutube.ru/video/43d0c3e1afd079d89b548dde50dfe9b5/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№11_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 11](https://rutube.ru/video/80647e7fba7c0cb1d3c5c7b9f3261954/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№12_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 12](https://rutube.ru/video/f6947ce826e52961d83c79e991430279/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№13_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 13](https://rutube.ru/video/319cb5cb5ccde926c5a108af1550a6ff/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№14_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 14](https://rutube.ru/video/3044b43fe9021bf2e533a62b94875107/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№15_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 15](https://rutube.ru/video/afa0bdb638396555038ab15ae5fafbf0/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№16_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 16](https://rutube.ru/video/ec14a926aba6f07df65eeae6cb12947b/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№17_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 17](https://rutube.ru/video/21c55e8e253debec8efcdbf34ed63d49/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№18_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 18](https://rutube.ru/video/f4ecbe75c4fb722d16b8a4f87511829b/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№19_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 19](https://rutube.ru/video/8e939f04824a1a4f5851e171f35e60ad/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№20_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 20](https://rutube.ru/video/d70586d05cd2fcf33066cda2860baf28/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№21_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 21](https://rutube.ru/video/72a55d0e72f9313c538bcd40951bed99/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№22_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 22](https://rutube.ru/video/fe8be9b259beaee4fe29d7192fefd177/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№23_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 23](https://rutube.ru/video/8c7beaabec16d3ffc137c23edf8e7700/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№24_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 24](https://rutube.ru/video/a626c38ac8d715ee7c1abe88d10d9437/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№25_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 25](https://rutube.ru/video/42281b4821e7ae82443ff908fc364551/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№26_Биология_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 26](https://rutube.ru/video/612b228bdb85f70c080848035de523b6/)', parse_mode='Markdown')
        markup.add(back)

    elif message.text == "География":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        g1 = types.KeyboardButton("№1_География_ОГЭ")
        g2 = types.KeyboardButton("№2_География_ОГЭ")
        g3 = types.KeyboardButton("№3_География_ОГЭ")
        g4 = types.KeyboardButton("№4_География_ОГЭ")
        g5 = types.KeyboardButton("№5_География_ОГЭ")
        g6 = types.KeyboardButton("№6_География_ОГЭ")
        g7 = types.KeyboardButton("№7_География_ОГЭ")
        g8 = types.KeyboardButton("№8_География_ОГЭ")
        g9 = types.KeyboardButton("№9_География_ОГЭ")
        g10 = types.KeyboardButton("№10_География_ОГЭ")
        g11 = types.KeyboardButton("№11_География_ОГЭ")
        g12 = types.KeyboardButton("№12_География_ОГЭ")
        g13 = types.KeyboardButton("№13_География_ОГЭ")
        g14 = types.KeyboardButton("№14_География_ОГЭ")
        g15 = types.KeyboardButton("№15_География_ОГЭ")
        g16 = types.KeyboardButton("№16_География_ОГЭ")
        g17 = types.KeyboardButton("№17_География_ОГЭ")
        g18 = types.KeyboardButton("№18_География_ОГЭ")
        g19 = types.KeyboardButton("№19_География_ОГЭ")
        g20 = types.KeyboardButton("№20_География_ОГЭ")
        g21 = types.KeyboardButton("№21_География_ОГЭ")
        g22 = types.KeyboardButton("№22_География_ОГЭ")
        g23 = types.KeyboardButton("№23_География_ОГЭ")
        g24 = types.KeyboardButton("№24_География_ОГЭ")
        g25 = types.KeyboardButton("№25_География_ОГЭ")
        g26 = types.KeyboardButton("№26_География_ОГЭ")
        g27 = types.KeyboardButton("№27_География_ОГЭ")
        g28 = types.KeyboardButton("№28_География_ОГЭ")
        g29 = types.KeyboardButton("№29_География_ОГЭ")
        g30 = types.KeyboardButton("№30_География_ОГЭ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add( g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22, g23, g24, g25, g26, g27, g28, g29, g30, back)
        bot.send_message(message.chat.id, "выбери задание:", reply_markup=markup)

    elif (message.text == "№1_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 1](https://rutube.ru/video/aefd6625da90d3e709f59e56f901a7a6/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№2_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 2](https://rutube.ru/video/3aabbea6f04bba40e08537c90c1ef888/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№3_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 3](https://rutube.ru/video/29f988a456956686a42eae4c1fac8cc9/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№4_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 4](https://rutube.ru/video/363f694481b9b5c39a9e7648c5269762/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№5_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 5](https://rutube.ru/video/97d0d257e33c16461640ac79dd0e0782/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№6_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 6](https://rutube.ru/video/c5de68acd7a3fe95481cf38e0943019b/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№7_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 7](https://rutube.ru/video/3833d111763fe86eb431ca5c43d39027/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№8_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 8](https://rutube.ru/video/3940b8ea9553951b6a30a71f8870d9ee/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№9_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 9](https://rutube.ru/video/9a4afa51c1e7ea9e49fe28f85bf18ab9/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№10_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 10](https://rutube.ru/video/b2cb5628c13abb61cbdd6c504f83f98a/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№11_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 11](https://rutube.ru/video/f5f54d0ad82e1ac8aa431fad9a34cc43/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№12_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 12](https://rutube.ru/video/6ab87cf30811ae8d95f3c4cf8bd0db78/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№13_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 13](https://rutube.ru/video/71e4df4dc696bf761f787b2a33a2ce8a/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№14_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 14](https://rutube.ru/video/74de486c7d2eea4d775260225b6270be/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№15_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 15](https://rutube.ru/video/60a9c08db0b2c6ab038885e7041df231/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№16_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 16](https://rutube.ru/video/219b67686748fba971d16407ccc923d3/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№17_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 17](https://rutube.ru/video/87b4c79474ddcfb10388e326f08d91bd/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№18_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 18](https://rutube.ru/video/ebef0c9d2c419cb5e104caea940b7188/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№19_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 19](https://rutube.ru/video/d16634c07ed07222516cfac2257a4198/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№20_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 20](https://rutube.ru/video/0fae0cdeb881cf892769eea6b83f2d37/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№21_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 21](https://rutube.ru/video/938ea8fd20f6b3fad45165346a0c431a/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№22_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 22](https://rutube.ru/video/835c2d9e1a229c0c525bfc7eb5991481/)', parse_mode='Markdown')
        markup.add(back)
        
    elif (message.text == "№23_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 23](https://rutube.ru/video/69c84e316ef3804b1b2009b3ab31f1e4/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№24_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 24](https://rutube.ru/video/1685642478c30190bf95bac3dfb72c70/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№25_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 25](https://rutube.ru/video/9297b117d7f67a09fe07a032381b63dc/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№26_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 26](https://rutube.ru/video/1b789eed865adc7a6ff88aa705a09174/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№27_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 27](https://rutube.ru/video/35e4e6695fa1789491a50442be687cf0/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№28_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 28](https://rutube.ru/video/dc55636d3cb62834acd6bcb71a8f3405/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№29_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 29](https://rutube.ru/video/0d0226d8b68741bd9d966ecf02e0616b/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№30_География_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 30](https://rutube.ru/video/b2a6ed48beabd0b5ae7715c12f5fce0e/)', parse_mode='Markdown')
        markup.add(back)

    elif message.text == "Обществознание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        o1 = types.KeyboardButton("№1_Обществознание_ОГЭ")
        o2 = types.KeyboardButton("№2_Обществознание_ОГЭ")
        o3 = types.KeyboardButton("№3_Обществознание_ОГЭ")
        o4 = types.KeyboardButton("№4_Обществознание_ОГЭ")
        o5 = types.KeyboardButton("№5_Обществознание_ОГЭ")
        o6 = types.KeyboardButton("№6_Обществознание_ОГЭ")
        o7 = types.KeyboardButton("№7_Обществознание_ОГЭ")
        o8 = types.KeyboardButton("№8_Обществознание_ОГЭ")
        o9 = types.KeyboardButton("№9_Обществознание_ОГЭ")
        o10 = types.KeyboardButton("№10_Обществознание_ОГЭ")
        o11 = types.KeyboardButton("№11_Обществознание_ОГЭ")
        o12 = types.KeyboardButton("№12_Обществознание_ОГЭ")
        o13 = types.KeyboardButton("№13_Обществознание_ОГЭ")
        o14 = types.KeyboardButton("№14_Обществознание_ОГЭ")
        o15 = types.KeyboardButton("№15_Обществознание_ОГЭ")
        o16 = types.KeyboardButton("№16_Обществознание_ОГЭ")
        o17 = types.KeyboardButton("№17_Обществознание_ОГЭ")
        o18 = types.KeyboardButton("№18_Обществознание_ОГЭ")
        o19 = types.KeyboardButton("№19_Обществознание_ОГЭ")
        o20 = types.KeyboardButton("№20_Обществознание_ОГЭ")
        o21_24 = types.KeyboardButton("№21_24_Обществознание_ОГЭ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add( o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12, o13, o14, o15, o16, o17, o18, o19, o20, o21_24, back)
        bot.send_message(message.chat.id, "выбери задание:", reply_markup=markup)

    elif (message.text == "№1_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 1](https://rutube.ru/video/21edac328cf863cdbe5a4cbffd1f0826/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№2_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 2](https://rutube.ru/video/8147cf7fbf18b8a52e8ca03362d9ae82/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№3_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 3](https://rutube.ru/video/d33a0c4f6ff85ba2aac2c6ad2ecbe9e1/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№4_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 4](https://rutube.ru/video/847cb209db02fb458008b82627f4d11a/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№5_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 5](https://rutube.ru/video/9b88daaa8ca78f8be7f0d278f79713ad/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№6_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 6](https://rutube.ru/video/33af3517185f23c72513537f1e347511/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№7_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 7](https://rutube.ru/video/b4d373bb9be694b56b27abb914f25fb7/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№8_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 8](https://rutube.ru/video/0d9340bdd9b693cdab4d0a9b6d09b408/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№9_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 9](https://rutube.ru/video/e5e5c87895ff7c75e25946d8d842ab21/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№10_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 10](https://rutube.ru/video/fea5e1445f34ceb17efd23d09a908af5/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№11_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 11](https://rutube.ru/video/7fc8822dec4a8717ba820efda272d3b1/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№12_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 12](https://rutube.ru/video/601a66f9a23e59536de5c7cb3178a632/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№13_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 13](https://rutube.ru/video/3d49c48146433736e0ae8b6c04bc4bc5/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№14_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 14](https://rutube.ru/video/5f41ac855ca0738eb9113eb4faba8799/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№15_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 15](https://vkvideo.ru/video511985415_456239574)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№16_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 16](https://rutube.ru/video/022f9bea598276d868578406f2972331/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№17_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 17](https://rutube.ru/video/111edbf831574d8d39bea0ef123daa2f/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№18_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 18](https://rutube.ru/video/8f619b97dba2b7214ea0e3709c4bb6c6/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№19_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 19](https://rutube.ru/video/a30d6b45d56e6db0e3c0895681bc0fb0/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№20_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 20](https://rutube.ru/video/11807fc41a42a029f698d345a5bdb6d7/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "№21_24_Обществознание_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор задания 21, 22, 23, 24](https://rutube.ru/video/54ce8c309da271c842e5de6f0b806c74/)', parse_mode='Markdown')
        markup.add(back)

    elif message.text == "История":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ei1 = types.KeyboardButton("Все задания_История_ОГЭ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(ei1, back)
        bot.send_message(message.chat.id, "выбери задание:", reply_markup=markup)

    elif (message.text == "Все задания_История_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор всех заданий](https://rutube.ru/video/6e7e6013ab41a8a26b1d8a513ea2ecc3/)', parse_mode='Markdown')
        markup.add(back)

    elif message.text == "Литература":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        lit1 = types.KeyboardButton("Все задания_Литература_ОГЭ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(lit1, back)
        bot.send_message(message.chat.id, "выбери задание:", reply_markup=markup)

    elif (message.text == "Все задания_Литература_ОГЭ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        bot.send_message(message.chat.id, '[разбор всех заданий](https://rutube.ru/video/edefb2e6d9bc6a3b84a09169019f6d77/)', parse_mode='Markdown')
        markup.add(back)

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Огэ")
        button2 = types.KeyboardButton("Егэ")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")

bot.polling(none_stop=True)


if __name__ == '__main__':
    bot.infinity_polling()
