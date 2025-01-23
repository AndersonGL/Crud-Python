import mysql.connector

conexao = mysql.connector.connect(
  
   host='localhost',
   user='root',
   password='1234',
   database='bdyoutube',
  
)
cursor = conexao.cursor()  #cursor

# CRUD PYTHON COM MSQL




 #CREATE

nome_produto = 'leite'   # Cria dados no banco
valor = 6
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute (comando)
conexao.commit() 



# READ

comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() #  Ler dados do banco
print(resultado)


#UPDATE

nome_produto = "chocolate"           #  Atualiza itens do banco
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()  


#DELETE


nome_produto = 'desktop'
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()          # Exclui itens do banco




cursor.close()   # para fechamento do cursor
conexao.close()   # para fechamento do banco 













# conexao.commit() # edita o banco de dados
# resultado = cursor.fetchall() # ler o banco de dados