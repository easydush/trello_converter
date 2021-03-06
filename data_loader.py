from protocol_generator import ProtocolGenerator
from trello_connector import TrelloConnector


def load_data():
    trello = TrelloConnector()

    # lists = trello.load_lists()
    # custom_fields = trello.load_fields()
    cards, checklists = trello.load_cards()
    print('Все данные были успешно обновлены.\n')
    for value in cards:
        writer = ProtocolGenerator(value)
        writer.head()
        writer.meta()
        info = checklists.get(value.name)
        if info:
            writer.content(info)
        writer.save()
