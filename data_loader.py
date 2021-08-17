from db_connector import DBConnector
from trello_connector import TrelloConnector

def load_data():
    db = DBConnector()
    trello = TrelloConnector()
    lists = trello.load_lists()
    custom_fields = trello.load_fields()
    cards, values = trello.load_cards()

    for column in lists:
        db.set_list(column)

    for field in custom_fields:
        db.set_field(field)

    for card in cards:
        db.set_card(card)

    for value in values:
        db.set_value(value)
    print('All data has been successfully saved.')
