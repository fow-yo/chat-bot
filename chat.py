from logging import StringTemplateStyle
import telebot
import random


data = {
    "number": [],
}


@bot.message_handler(commands=['s'])
def start_command(message):
    bot.send_message(message.chat.id, "Введите четырехзначное число!")
    data["number"] = random.sample("0123456789", 4)
    bot.send_message(message.chat.id, str(data["number"]))


@bot.message_handler(content_types=['text'])
def send_text(message):
    cows = 0
    bulls = 0
    user = message.text
    if len(user)!=4:
        bot.send_message(message.chat.id, "Число не четырехзначное.")
    elif user.isdigit() != True:
        bot.send_message(message.chat.id, "Вы ввели не число.")
    else: 
        for i in data["number"]:
            if i in user:
                cows += 1

        for i in range(4):
            if data["number"][i] == user[i]:
                bulls += 1
    String = ''.join(data["number"])
    bot.send_message(message.chat.id, "Коровы: " +
                     str(cows)+", Быки: "+str(bulls)+"\nЗагаданное число: "+String)

    if user == data["number"]:
        bot.send_message(message.chat.id, "Вы угадали число!")


bot.polling()
