import telebot

from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru' 

owm = OWM( 'c013bceecaf42f043ec20835856f1745', config_dict )

mgr = owm.weather_manager()
bot = telebot.TeleBot("1529143885:AAH6dZrvwKJxugyFFk4saQLQxl5KMGGtc8I", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place('Москва,RU')
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    answer = 'В городе ' + message.text + ' сейчас ' + w.detailed_status + '\n'
    answer += 'Температура воздуха ' + str(temp) + '\n\n'
    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )


