import json

from models import Card

input_file = 'trello.json'


def load():
    with open(input_file, 'r', encoding='utf-8') as info:
        loaded = json.load(info)
        card = Card(**loaded)
        info.close()
        return card
