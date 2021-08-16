# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3

from models import Card, List


class DBConnector:
    def __init__(self):
        self.db_file = 'local.sqlite'
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()

    def get_all_lists(self, board_id):
        sql = """
                SELECT * FROM lists
                WHERE board_id = ?
                """
        self.cursor.execute(sql, (board_id,))
        return self.cursor.fetchall()

    def get_all_cards(self, board_id):
        sql = """
                SELECT * FROM cards
                WHERE board_id = ?
                """
        self.cursor.execute(sql, (board_id,))
        return self.cursor.fetchall()

    def get_cards_from_list(self, list_id):
        sql = """
                  SELECT * FROM cards
                  WHERE list_id = ?
                  ORDER BY id DESC
                  """
        self.cursor.execute(sql, (list_id,))
        return self.cursor.fetchone()

    def get_card(self, card_id):
        sql = """
                  SELECT * FROM cards
                  WHERE id = ?
                  """
        self.cursor.execute(sql, (card_id,))
        return self.cursor.fetchone()

    def get_list(self, list_id):
        sql = """
              SELECT * FROM lists 
              WHERE id = ?
              ORDER BY id DESC
              """
        self.cursor.execute(sql, (list_id,))
        return self.cursor.fetchone()

    def set_list(self, column: List):
        sql = """
                INSERT INTO lists(id, name, closed, board_id) VALUES (?, ?, ?, ?)
                """
        self.cursor.execute(sql, (column.id, column.name, column.closed, column.board_id))
        return self.connection.commit()

    def set_card(self, card: Card):
        sql = """
                INSERT INTO cards(id, desc, name, closed, due, short_url, board_id, list_id) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """
        self.cursor.execute(sql, (
            card.id, card.desc, card.name, card.closed, card.due, card.short_url, card.board_id, card.list_id))
        self.connection.commit()

    def close(self):
        self.connection.close()
