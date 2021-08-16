import logging

import requests

from models import Card, List

import os
from dotenv import load_dotenv

load_dotenv()

BOARD_ID = os.getenv('BOARD_ID')
API_URL = 'https://api.trello.com/1/boards'
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


def load_cards():
    response = requests.request(
        "GET",
        CARDS_URL,
        params=AUTH_PARAMS
    )
    loaded = response.json()
    cards = []
    for card in loaded:
        cards.append(Card(**card))
    print(f'Got cards:', cards)


def load_lists():
    response = requests.request(
        "GET",
        LISTS_URL,
        params=AUTH_PARAMS
    )
    loaded = response.json()
    lists = []
    for column in loaded:
        lists.append(List(**column))
    print(f'Got lists:', lists)


def load_fields():
    response = requests.request(
        "GET",
        CUSTOM_FIELDS_URL,
        params=AUTH_PARAMS
    )
    loaded = response.json()
    # lists = []
    # for column in loaded:
    #     lists.append(List(**column))
    print(loaded)


load_fields()
