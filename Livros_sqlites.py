import sqlite3

banco = sqlite3.connect('livros.db')

cursor = banco.cursor()

#criar uma tabela chamada livros com id titulo autoe ano genero e disponivel
cursor.execute("""CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT, 
               titulo TEXT, 
               autor TEXT, 
               ano INTEGER, 
               genero TEXT, 
               disponivel BOOLEAN DEFAULT 1)""") 
banco.commit()

#inserir 5 livros na tabela
cursor.execute("SELECT COUNT(*) FROM livros")       #verifica se ja existem livros cadastrados
if cursor.fetchone()[0] == 0:                       #se nao houver livros cadastrados, insere os livros, evitando duplicatas
    cursor.execute("INSERT INTO livros (titulo, autor, ano, genero) VALUES ('Abuela', 'Daniel Pinheiro', 2025, 'Ficção')")
    cursor.execute("INSERT INTO livros (titulo, autor, ano, genero) VALUES ('O Assassino da Faca de Pão', 'Ana Maria Braga', 1870, 'Suspense')")
    cursor.execute("INSERT INTO livros (titulo, autor, ano, genero) VALUES  ('O Mago Holandes', 'Michael Jackson', 2035, 'Fantasia')")
    cursor.execute("INSERT INTO livros (titulo, autor, ano, genero) VALUES  ('Queijo Quente', 'Mikey Mouse', 1920, 'Terror')")
    cursor.execute("INSERT INTO livros (titulo, autor, ano, genero) VALUES  ('Salsicha Gigante', 'Cachorro da Esquina', 2000,'Comédia')")
banco.commit()

#consultar todos os livros disponiveis
cursor.execute("SELECT * FROM livros WHERE disponivel = 1")

#atualizar o status de disponibilidade de um livro utilizando o id
cursor.execute("UPDATE livros SET disponivel = 0 WHERE id = 3")
banco.commit()

#consultar todos os livros ordenados pelo ano de publicação em ordem decrescente
cursor.execute("SELECT * FROM livros ORDER BY ano DESC")

#deletar livros publicados antes de 1940
cursor.execute("DELETE FROM LIVROS WHERE ano < 1940")
banco.commit()

#criando a tabela usuarios
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT)""")
banco.commit()

#adicionando a coluna idade na tabela usuarios
cursor.execute("PRAGMA table_info(usuarios)")           #verifica se a coluna idade ja existe
cols = [r[1] for r in cursor.fetchall()]                #cria uma lista com os nomes das colunas
if 'idade' not in cols:                                 #se a coluna idade nao existir, cria a coluna
    cursor.execute("ALTER TABLE usuarios ADD COLUMN idade INTEGER")
banco.commit()

#inserindo usuarios na tabela usuarios
cursor.execute("SELECT COUNT(*) FROM usuarios")        #verifica se ja existem usuarios cadastrados
if cursor.fetchone()[0] == 0:                          #se nao houver usuarios cadastrados, insere os usuarios, evitando duplicatas
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Jalin Mamei', 22)")
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Deide Costas', 31)")
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Fabio Santos', 18)")
banco.commit()

cursor.execute("DROP TABLE IF EXISTS usuarios")          #deleta a tabela usuarios
banco.commit()