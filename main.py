import mysql.connector

conexao = mysql.connector.connect(      #conexão com bancos de dados
  # host='localhost',
  # user='root',
  # password='123456',
  # database='bdyoutube',
)


cursor = conexao.cursor()    
  


# CRUD  

nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados


cursor.close()
conexao.close()

# CREATE          

nome_produto = "chocolate"       # cria itens dentro do banco
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados


# READ                             # Lê o dados no banco
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)

 
# UPDATE                     # Atualiza o banco
nome_produto = "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

# DELETE                       # Exclui itens
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados
