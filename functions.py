import numpy as np
import pickle

import requests


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenue chez le bot Secret Santa de la P2022 !")


def chain(dict_names):

    list_ids = list(dict_names.keys())
    np.random.shuffle(list_ids)

    list_couples = []

    for i in range(len(list_ids) - 1):
        list_couples.append((list_ids[i], list_ids[i+1]))

    list_couples.append((list_ids[-1], list_ids[0]))

    dict_couples = {}
    cnt = 0
    for couple in list_couples:
        dict_couples[dict_names[couple[0]]] = dict_names[couple[1]]

    return dict_couples


def init(update, context):
    """
    Input: @ of all participants
    Output: Pickled dict {'giver': 'receiver'}
    """
    list_names = context.args
    dict_names = {}
    for i in range(len(list_names)):
        dict_names[i] = list_names[i]

    dict_couples = chain(dict_names)
    with open('data/chains.pkl', 'wb') as f:
        pickle.dump(dict_couples, f)


def get_name(update, context):
    """
    Output: Message sent to the client of the username that used /get_name, containing the name that was chosen.
    """
    with open('data/chains.pkl', 'rb') as f:
        dict_couples = pickle.load(f)

    username = update.message.from_user.username

    text = f'Tu dois donner un cadeau à {dict_couples["@" + username]}'

    context.bot.send_message(chat_id=update.message.chat_id,
                             text=text)
