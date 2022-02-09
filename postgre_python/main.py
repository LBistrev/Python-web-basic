import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="db_demos",
    user="postgres",
    password="1123QwER")

cursor = connection.cursor()
cursor.execute('SELECT name FROM cities')


class Employee:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager

    def __repr__(self):
        return f'{self.name} - {self.manager}'


employees = [Employee(*row) for row in cursor.fetchall()]

connection.close()
