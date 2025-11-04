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

#inserir 5 livros na tabela
cursor.execute("INSERT INTO livros (titulo, autor, ano, genero) VALUES ('Abuela', 'Daniel Pinheiro', 2025, 'Ficção')")
cursor.execute("INSERT INTO livros (titulo, autor, ano, genero) VALUES ('O Assassino da Faca de Pão', 'Ana Maria Braga', 1870, 'Suspense')")
cursor.execute("INSERT INTO livros (titulo, autor, ano, genero) VALUES  ('O Mago Holandes', 'Michael Jackson', 2035, 'Fantasia')")
cursor.execute("INSERT INTO livros (titulo, autor, ano, genero) VALUES  ('Queijo Quente', 'Mikey Mouse', 1920, 'Terror')")
cursor.execute("INSERT INTO livros (titulo, autor, ano, genero) VALUES  ('Salsicha Gigante', 'Cachorro da Esquina', 2000,'Comédia')")
banco.commit()



