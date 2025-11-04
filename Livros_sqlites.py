import sqlite3

banco = sqlite3.connect('livros.db')

cursor = banco.cursor()

#criar uma tabela chamada livros com id titulo autoe ano genero e disponivel
cursor.execute("""CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT, 
               titulo TEXT, 
               autor TEXT, 
               ano INTEGER, 
               genero TEXT, 
               disponivel BOOLEAN)""")
banco.commit()