import logging
import requests

import protocol_generator as writer
from models import Card, List, CustomField, CustomFieldValue, CheckList, CheckItem

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
    'token': API_TOKEN,
    'customFieldItems': 'true'
}
headers = {
    "Accept": "application/json"
}
logger = logging.getLogger('trello')

trigger_stop = 'Приост'

cards = []
cards_checklists = {}


class TrelloConnector:
    def __init__(self):
        self.checklists = {}

    def load_cards(self):
        response = requests.request(
            "GET",
            CARDS_URL,
            params=AUTH_PARAMS
        )
        loaded = response.json()
        for card in loaded:
            model = Card(**card)
            cards.append(model)
            cards_checklists[model.name] = []
            # cards.append(model)
            if model.check_lists:
                print('\n', model.name)
                self.load_checklists(model.name, model.id)
        print('Получено карточек:', len(cards))
        # return self.load_values(cards)
        return cards, cards_checklists

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
        # print('Получено колонок:', len(lists))
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
        # print('Получено полей:', len(fields))
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
                fields.append(CustomFieldValue(**field))
        return cards, fields

    def load_checklists(self, name, card_id):
        response = requests.request(
            "GET",
            f'{CARD_URL}/{card_id}/checklists',
            params=AUTH_PARAMS
        )
        loaded = response.json()
        for check_list in loaded:
            model = CheckList(**check_list)
            print(model.name)
            checklists = {model.name: []}
            for item in model.check_items:
                model_item = CheckItem(**item)
                checklists[model.name].append((model_item.name, model_item.due, model_item.state))
                print(model_item.name, model_item.due, model_item.state)
            cards_checklists[name].append(checklists)

    def load_card(self, card=None):
        if card:
            print(card.customFieldItems)
            for item in card.customFieldItems:
                field = CustomField(**item)
                url = f'https://api.trello.com/1/customFields/{field.id_custom_field}'
                response = requests.request(
                    "GET",
                    url,
                    params=AUTH_PARAMS,

                    headers=headers
                )
                loaded = response.json()
                extended_field = CustomField(**loaded)
                print(extended_field.__dict__)
