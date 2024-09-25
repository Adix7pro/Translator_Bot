import telebot
from deep_translator import GoogleTranslator
from forward import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def startfunc(message):
    bot.send_message(message.chat.id,"Assalom alaykum !!!")


def translate_text(text,target_lang):
    translater = GoogleTranslator(source='auto',target = target_lang)
    return translater.translate(text)


@bot.message_handler(func=lambda message: True)
def messagefunc(message):
    text = message.text
    en_translation = translate_text(text,"en")
    ru_translation = translate_text(text,"ru")
    fr_translation = translate_text(text,"fr")
    uz_translation = translate_text(text,"uz")

    response = (
        f"Tarjimalar: \n"
        f" English : {en_translation}\n"
        f" Russian : {ru_translation}\n"
        f" French : {fr_translation}\n"
        f" Uzbekish : {uz_translation}\n"
    )

    bot.send_message(message.chat.id,response)

bot.polling(non_stop=True)
