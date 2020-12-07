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

reset_handler = CommandHandler('reset', reset, filters=Filters.user(username="@MassInfect"))
dispatcher.add_handler(reset_handler)

add_handler = CommandHandler('add', add, filters=Filters.user(username="@MassInfect"))
dispatcher.add_handler(add_handler)

assign_handler = CommandHandler('assign', assign, filters=Filters.user(username="@MassInfect"))
dispatcher.add_handler(assign_handler)

list_participants_handler = CommandHandler('list', list_participants)
dispatcher.add_handler(list_participants_handler)

join_handler = CommandHandler('join', join)
dispatcher.add_handler(join_handler)

get_name_handler = CommandHandler('get_name', get_name)
dispatcher.add_handler(get_name_handler)

get_all_handler = CommandHandler('get_all', get_all, filters=Filters.user(username="@MassInfect"))
dispatcher.add_handler(get_all_handler)

updater.start_polling()
