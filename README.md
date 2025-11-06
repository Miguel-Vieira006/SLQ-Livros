# COMO EXECUTAR O PROJETO

# 1. Clone o repositorio
    git clone https://github.com/Miguel-Vieira006/SLQ-Livros.git

# 2. Crie e ative o ambiente virtual
    python -m venv venv
    venv\Scripts\activate

# 3. Baixe dependencias (se houver)
    pip install -r requirements.txt

# 4. Execute o escript
    python Livros_sqlites.py


# TABELA DE LIVROS
|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|
| COLUNA    | TIPO      | RESTRIÇÂO/DEFAULT         | DESCRIÇÃO                          |
|-+-+-+-+-+-|-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-|-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|
| id        | INTEGER   | PRIMARY KEY AUTOINCREMENT | Identificador único do livro       |
|-+-+-+-+-+-|-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-|-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|
| titulo    | TEXT      |                           | Título do livro                    |
|-+-+-+-+-+-|-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-|-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|
| autor     | TEXT      |                           | Autor do livro                     |
|-+-+-+-+-+-|-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-|-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|
|ano        | INTEGER   |                           | Ano de publicação                  |
|-+-+-+-+-+-|-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-|-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|
|genero     | TEXT      |                           | Gênero literário                   |
|-+-+-+-+-+-|-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-|-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|
|disponivel | BOLEAN    |                           | 1 = disponível, 0 = indisponível   |
|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|


# TABELA DE USUARIOS
|-+-+-+-+-+-|-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|
| COLUNA    | TIPO      | RESTRIÇÂO/DEFAULT           | DESCRIÇÃO                          |
|-+-+-+-+-+-|-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|
| id        | INTEGER   | PRIMARY KEY AUTOINCREMENT   | Identificador único do usuario     |
|-+-+-+-+-+-|-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|
| nome      | TEXT      |                             | Nome do usuario                    |
|-+-+-+-+-+-|-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|
| idade     | INTEGER   | (adicionada se não existir) | Idade de usuario                   |
|-+-+-+-+-+-|-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-|

# QUESTÕES TEORICAS

# 1. Por que os bancos de dados são essenciais em aplicações modernas?
    Eles organizam os dados de maneira que facilita a busca e a manipulação dos dados, protege os dados contra acessos não autorizados, permitem acessar e manipular gandes quantidades de dados e garante precisão e consistencia dos dados

Fonte: recantodev
Link: https://recantodev.com.br/introducao-a-bancos-de-dados-o-que-sao-e-por-que-sao-importantes/

# 2. Quais são as duas principais categorias de bancos de dados existentes?
    SQL e NoSQL. SQL lida com bancos de dados bem estruturados e menos flexiveis que permite que os usuários se comuniquem com os bancos de dados e realizem consultas enormes e complexas em seus dados. Já o NoSQL lidam com dados não estruturados é mais flexíveis permitindo uma maior variedade de combinações de banco de dados.

Fonte: learnsql
Link: https://learnsql.com.br/blog/explicacao-dos-tipos-de-bancos-de-dados/

# 3. Em quais cenários é recomendado utilizar um banco de dados relacional
    Em cenarios de registro de usuarios ou clientes ou em casos de gerenciamento de dados transacionais no setor financeiro. Exemplo: uma empresa que guarda as informações
    de usuarios em tabelas relacionadas com o historico de comprar e etc

Fonte: learnsql
Link: https://learnsql.com.br/blog/explicacao-dos-tipos-de-bancos-de-dados/

# 4. De que forma os recursos de hardware (CPU, memória, disco) afetam a performance de um banco de dados?
    Um banco de dados apesar de ser algo acessivel online tem o local onde eles são hospedados e os recursos de hardware do local afetam a performace pois eles estão em constante uso para manter os bancos de dados ativos e seguros. Exemplos: CPU afeta velocidade de processamento de queries, memória ram impacta no cache e na velocidade de acesso a dados e disco na velocidade de leitura e escrita além da capacidade de armazenamento.

Fonte: hostragons
Link: https://www.hostragons.com/pt/blog/otimizacao-e-desempenho-de-banco-de-dados/

# 5. O que significa escalabilidade no contexto de bancos de dados?
    A escalabilidade de banco de dados é a capacidade de um banco de dados lidar com mais carga além de melhorar seu desempenho de formas variadas, o escalonamento pode ser horizontal ou vertical 

    Escalonamento Horizontal: Funciona melhor em sistemas não relacionais, refere-se à adição de mais nós para compartilhar uma carga maior de dados, esses nós fazem parte de um cluster que pode ser distribuido entre varios servidores diminuindo a carga de dados por servidor.
    
    Escalonamento Vertical: Esse tipo de escalonamento envolve apenas um servidor ele utiliza de recursos físicos ou virtuais para melhorar a capacidade e desempenho do banco de dados.

Fonte: couchbase
Dados: https://www.couchbase.com/pt/resources/concepts/database-scalability/

# 6. Qual a relevância de organizar corretamente os dados em bancos relacionais?
    É importante organizar corretamente os dados em bancos relacionais pois dessa maneira é mais fácil acessar e manipular os dados armazenados além de facilitar a leitura desses dados

Fonte: IBM
Link: https://www.ibm.com/br-pt/think/topics/relational-database

# 7. Como escolher entre SQL e NoSQL para um novo projeto?
    Enquanto SQL é um tipo de banco de dados mais estruturado com tabelas predefinidas com esquemas fixos, as tabelas se interligam por chaves primarias e estrangeiras, tornando mais fácil e eficiente o acesso aos dados, já o NoSQL não funciona atraves de esquemas fixos e podem armazenar dados em uma variedade de formatos, como documentos, grafos, chave-valor ou colunas. Eles priorizam a disponibilidade e a tolerância a particionamento. Portanto se o projeto utiliza de dados pouco variados e preza por uma melhor organização e fácil acesso a melhor opçãio é o tipo SQL, mas se o projeto precisar de uma maior flexibilidade no armazenamento de dados o ideal é o NoSQL.

Fonte: Dicas de Programação
Link: https://dicasdeprogramacao.com.br/sql-vs-nosql-guia-completo-para-escolher-o-banco-de-dados-certo-para-seu-projeto/

# COMANDOS SQL

# 1. Qual é a finalidade do comando SELECT em SQL?
    Seleciona dados, colunas e etc para serem exibidas

Fonte: FreeCodecamp
Link: https://www.freecodecamp.org/portuguese/news/comandos-basicos-em-sql-a-lista-de-consultas-e-instrucoes-de-banco-de-dados-que-voce-deve-conhecer/

# 2. O que significam as siglas DML e DDL em bancos de dados?
    DML e DDL são "sub-línguas" do SQL. A DML é a sub-língua responsável pela adição, edição ou exclusão de dados de um banco de dados. Em SQL, isto corresponde ao INSERT, UPDATE, e DELETE, já a DDL é a sub-língua responsável pela definição da forma como os dados são estruturados em um banco de dados. Em SQL, isto corresponde à manipulação de tabelas através do CREATE TABLE, ALTER TABLE, e DROP TABLE

Fonte: learnsql.com.br
Link: https://learnsql.com.br/blog/o-que-sao-ddl-dml-dql-e-dcl-em-sql/

# 3. Para que serve a cláusula WHERE em consultas SQL?
    Em português "where" significa "onde", essa cláusula é usada junto de outros comandos para filtrar seus resultados e ter mais precisão na manipulação de dados

Fonte: learnsql.com.br
Link: https://learnsql.com.br/blog/o-guia-completo-da-clausula-sql-where/

# 4. Por que é fundamental estabelecer uma chave primária (PRIMARY KEY) em tabelas?
    Chaves primarias são essenciais para garantir a integridade dos dados em uma tabela além disso elas possibilitam buscas eficientes por isso elas tem caracteristicas relevantes como, exclusividade para garantir que não exista nenhuma chave igual e evitar confusões, não nunalidade pois as chaves primarias não podem ser nulas e geralmente são imutaveis para evitar confusões

Fonte: DataCamp
Link: https://www.datacamp.com/pt/tutorial/sql-primary-key

# 5. Como funciona o comando UPDATE e qual sua sintaxe básica?
    O comando UPDATE é utilizado para atualizar uma ou mais informações de uma tabela. 

    Exemplo: UPDATE nome_da_tabela
    SET coluna1 = valor1, 
        coluna2 = valor2, ...
    WHERE condição;

Fonte: HostGator Brasil
Link: https://www.hostgator.com.br/blog/sql-update/

# 6. Qual a função do comando DELETE em SQL? (Diferença entre DELETE e DROP)
    O comando DELETE permite a remoção de registros de uma tabela de forma seletiva e eficaz, o comando DELETE remove registros especifico, pode ser revertido e pode usar WHERE para filtrar, já o drop remove toda a estrutura, não podeser revertido e não pode usar WHERE para filtrar

Fonte: Didática Tech
Linl: https://didatica.tech/tudo-sobre-o-comando-delete-em-sql/

# 7. Como a cláusula ORDER BY organiza os resultados de uma consulta?
    A cláusula ORDER BY é usada para ordenar os resultados de uma consulta SQL com base em uma ou mais colunas. Você pode organizar tanto em ordem crescente (ASC) ou decrescente (DESC)

Fonte: Criandobits
Link: https://www.criandobits.com.br/clausula-order-by/

# 8. Para que serve o comando LIMIT em consultas SQL?
    O comando LIMIT é utilizado na linguagem SQL para especificar o número máximo de registros que devem ser retornados por uma consulta.

Fonte: Didática Tech
Link: https://didatica.tech/para-que-serve-e-como-usar-os-comandos-limit-e-offset-em-sql/

# OUTROS CONCEITOS

# 1. Por que é importante integrar o banco de dados com a camada de back end da aplicação? 
    É importante para armazenar dados gerados apartir de cadastros, transações, chave de validação

Fonte: Awari
Link: https://awari.com.br/aprenda-tudo-sobre-banco-de-dados-back-end-e-se-torne-um-especialista-em-tecnologia/

# 2. O que são views (visões) em bancos de dados e quais suas vantagens?
    As views em SQL são consultas nomeadas que podem ser usadas como tabelas virtuais. Elas não armazenam dados propriamente ditos, mas sim uma definição de consulta que é executada sempre que a view é acessada

Fontes: comoprogramarjava
Link: https://comoprogramarjava.com.br/views-em-sql/

# 3. Quais são as propriedades ACID e por que são cruciais para transações?
    As transações ACID referem-se a quatro propriedades que garantem o processamento confiável das transações do banco de dados. Os quatro princípios são, Atomicidade, Consistência, Isolação e Durabilidade 

Fonte: DataCamp
Link: https://www.datacamp.com/pt/blog/acid-transactions

# 4. O que estabelece o Princípio do Privilégio Mínimo em segurança de bancos de dados?
    O princípio do privilégio mínimo concede o acesso minimamente necessario para que as pessoas ou sistemas que estão acessando os dados façam o seu trabalho, esse metodo reduz os riscos e aumenta a segurança do sistema.
 
Fonte: DataCamp
Link: https://www.datacamp.com/pt/tutorial/principle-of-least-privilege