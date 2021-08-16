class CustomField:
    def __init__(self, id, name, value, **other):
        self.id = id
        self.name = name
        self.value = value
        self.other = other


class Card:
    def __init__(self, id, closed, desc, name, due, shortUrl, idBoard, idList, customFieldItems=None, **other):
        self.id = id
        self.closed = closed
        self.desc = desc
        self.name = name
        self.due = due
        self.short_url = shortUrl
        self.board_id = idBoard
        self.list_id = idList
        self.customFieldItems = customFieldItems
        self.other = other


class List:
    def __init__(self, id, name, closed, idBoard, **other):
        self.id = id
        self.name = name
        self.closed = closed
        self.board_id = idBoard
        self.other = other
