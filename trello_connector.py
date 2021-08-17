import logging

import requests

from models import Card, List, CustomField, CustomFieldValue

import os
from dotenv import load_dotenv

load_dotenv()

BOARD_ID = os.getenv('BOARD_ID')
API_URL = 'https://api.trello.com/1/boards'
CARD_URL = 'https://api.trello.com/1/cards'
CARDS_URL = f'{API_URL}/{BOARD_ID}/cards'
LISTS_URL = f'{API_URL}/{BOARD_ID}/lists'
CUSTOM_FIELDS_URL = f'{API_URL}/{BOARD_ID}/customFields'
API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')
AUTH_PARAMS = {
    'key': API_KEY,
    'token': API_TOKEN
}
logger = logging.getLogger('trello')


class TrelloConnector:
    def __init__(self):
        pass

    def load_cards(self):
        response = requests.request(
            "GET",
            CARDS_URL,
            params=AUTH_PARAMS
        )
        loaded = response.json()
        cards = []
        for card in loaded:
            cards.append(Card(**card))
        print('Got cards:', len(cards))
        return self.load_values(cards)

    def load_lists(self):
        response = requests.request(
            "GET",
            LISTS_URL,
            params=AUTH_PARAMS
        )
        loaded = response.json()
        lists = []
        for column in loaded:
            lists.append(List(**column))
            print(column)
        print('Got lists:', len(lists))
        return lists

    def load_fields(self):
        response = requests.request(
            "GET",
            CUSTOM_FIELDS_URL,
            params=AUTH_PARAMS
        )
        loaded = response.json()
        fields = []
        for field in loaded:
            fields.append(CustomField(**field))
        print('Got fields:', len(fields))
        return fields

    def load_values(self, cards: []):
        fields = []
        for card in cards:
            url = f'{CARD_URL}/{card.id}/customFieldItems'
            response = requests.request(
                "GET",
                url,
                params=AUTH_PARAMS
            )
            loaded = response.json()
            for field in loaded:
                print(field)
                fields.append(CustomFieldValue(**field))
        return cards, fields
