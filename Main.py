import telegram
import requests

bot = telegram.Bot(token='6280672598:AAEClKBN-liRYpiR9xb_DLT6HLdYcWw6cUQ')
weather_api_key = 'https://api.freeconvert.com/v1/process/import/upload/'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}'
    response = requests.get(url).json()
    temperature = response['main']['temp']
    return f'The temperature in {city} is {temperature} Kelvin.'

def handle_message(update, context):
    message = update.message.text
    if message.startswith('/weather'):
        city = message.split(' ')[1]
        weather = get_weather(city)
        bot.send_message(chat_id=update.effective_chat.id, text=weather)

if __name__ == '__main__':
    updater = telegram.ext.Updater(token='6280672598:AAEClKBN-liRYpiR9xb_DLT6HLdYcWw6cUQ', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
    updater.start_polling()
