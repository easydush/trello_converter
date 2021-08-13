class Card:
    def __init__(self, id, closed, desc, name, due, shortUrl, customFieldItems, **other):
        self.id = id
        self.closed = closed
        self.desc = desc
        self.name = name
        self.due = due
        self.shortUrl = shortUrl
        self.customFieldItems = customFieldItems
        self.other = other
