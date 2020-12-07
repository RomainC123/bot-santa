from telegram.ext import CommandHandler
from functions import *
import logging
from telegram.ext import Updater, Filters

with open('data/token.txt', 'r') as f:
    updater = Updater(token='1215340378:AAH4IqZkkl1hfDFsEgxGKKpLWgQnfgNJt9w', use_context=True)

dispatcher = updater.dispatcher

# ------------------------------------------------------------------------------

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# ------------------------------------------------------------------------------

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

init_handler = CommandHandler('init', init, filters=Filters.user(username="@MassInfect"))
dispatcher.add_handler(init_handler)

get_name_handler = CommandHandler('get_name', get_name)
dispatcher.add_handler(get_name_handler)

updater.start_polling()
