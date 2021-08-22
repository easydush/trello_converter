from datetime import datetime as dt


class CustomField:
    def __init__(self, id, idModel, fieldGroup, name, **other):
        self.id = id
        self.id_model = idModel
        self.field_group = fieldGroup
        self.name = name
        self.other = other


class CustomFieldValue:
    def __init__(self, id, idCustomField, value=None, **other):
        self.id = id
        self.id_custom_field = idCustomField
        self.value = value
        self.other = other


class CheckItem:
    def __init__(self, id, idChecklist, state, name, due, **other):
        self.id = id
        self.check_list_id = idChecklist
        self.state = 'Выполнено' if state == 'complete' else 'Не выполнено'
        self.name = name
        self.due = (dt.strptime(due, "%Y-%m-%dT%H:%M:%S.%fZ") if due else dt.today()).__format__('%d.%m.%Y г.')
        self.other = other


class CheckList:
    def __init__(self, idCard, id, name, checkItems, **other):
        self.id = id
        self.card_id = idCard
        self.name = name
        self.check_items = checkItems
        self.other = other


class Card:
    def __init__(self, id, closed, desc, name, due, shortUrl, idBoard, idList, idChecklists, customFieldItems=None,
                 **other):
        self.id = id
        self.closed = closed
        self.desc = desc
        self.name = name
        self.due = due
        self.short_url = shortUrl
        self.board_id = idBoard
        self.list_id = idList
        self.customFieldItems = customFieldItems
        self.check_lists = idChecklists
        self.other = other


class List:
    def __init__(self, id, name, closed, idBoard, **other):
        self.id = id
        self.name = name
        self.closed = closed
        self.board_id = idBoard
        self.other = other
