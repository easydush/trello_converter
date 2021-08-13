from models import Card

output_file = 'trello_card.doc'


def upload(card: Card):
    with open(output_file, 'w', encoding='UTF-8') as word:
        word.write(f'{card.name} \n {card.desc}')
        print('В файле должно быть написано ', card.name, card.desc)
        word.close()
