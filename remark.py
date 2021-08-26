import json
import os

from models import Card
from remark_generator import generate_remark

labels = {}


def load_from_card():
    with open('test.json', 'r', encoding='UTF-8') as source:
        loaded = json.loads(source.read())
        model = Card(**loaded)
        return model


def load_from_board():
    dirs = os.listdir('./board')
    dirs.remove('attachments')
    with open(f'board/{dirs[0]}', 'r', encoding='UTF-8') as source:
        loaded = json.loads(source.read())
        for label in loaded.get('labels'):
            labels[label.get('id')] = label.get('name')
        models = []
        for item in loaded.get('cards'):
            model = Card(labels=labels, **item)
            models.append(model)
        return models


# card = load_from_card()
# generate_remark(card)
cards = load_from_board()
for card in cards:
    generate_remark(card)
