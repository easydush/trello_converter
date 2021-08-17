# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3

from models import Card, List, CustomField, CustomFieldValue


class DBConnector:
    def __init__(self):
        self.db_file = 'local.sqlite'
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS lists
                            (id text NOT NULL PRIMARY KEY, name text, closed boolean, board_id text)
                       """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS fields
                                   (id text NOT NULL PRIMARY KEY, name text, field_group text, id_model text)
                              """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS cards
                                           (id text NOT NULL PRIMARY KEY, desc text, name text,closed boolean, due text, short_url text,
                                            board_id integer, list_id text)
                                      """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS field_values
                                                   (id text NOT NULL PRIMARY KEY, value text, id_custom_field text)
                                              """)

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

    def get_field(self, field_id):
        sql = """
                     SELECT * FROM fields
                     WHERE id = ?
                     """
        self.cursor.execute(sql, (field_id,))
        return self.cursor.fetchone()

    def set_list(self, column: List):
        sql = """
                INSERT OR IGNORE INTO lists(id, name, closed, board_id) VALUES (?, ?, ?, ?)
                """
        self.cursor.execute(sql, (column.id, column.name, column.closed, column.board_id))
        return self.connection.commit()

    def set_card(self, card: Card):
        sql = """
                INSERT OR IGNORE INTO cards(id, desc, name, closed, due, short_url, board_id, list_id) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """
        self.cursor.execute(sql, (
            card.id, card.desc, card.name, card.closed, card.due, card.short_url, card.board_id, card.list_id))
        self.connection.commit()

    def set_field(self, field: CustomField):
        sql = """
                INSERT OR IGNORE INTO fields(id, name, field_group, id_model) 
                VALUES (?, ?, ?, ?)
                """
        self.cursor.execute(sql, (field.id, field.name, field.field_group, field.id_model))
        self.connection.commit()

    def set_value(self, value: CustomFieldValue):
        sql = """
                INSERT OR IGNORE INTO field_values(id, value, id_custom_field) 
                VALUES (?, ?, ?)
                """
        self.cursor.execute(sql, (value.id, str(value.value), value.id_custom_field))
        self.connection.commit()

    def close(self):
        self.connection.close()
