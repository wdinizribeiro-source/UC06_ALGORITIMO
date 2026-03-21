import pymysql as pysql


conexao = pysql.connect(
    host="localhost",                     # endereço de servidor (local = 'localhost")
    user="root",                       # usuario do mysql
    password="" ,                       # senha do mysql
    database="bd_livrariaonline" ,       # banco que voce ja criou
    port=3306                         # porta padrão do mysql    
)

cursor = conexao.cursor(pysql.cursors.DictCursor)

# arquivo destinado a trabalhar com banco de dados e fazer a operaçoes UPDATE, INSERT e DELETE

try: 
#     # INSERT: Adicionar um novo registro -----------
#     sql_insert = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
#     cursor.execute(sql_insert,("wellington Diniz", "wdiniz@email.com"))
#     conexao.commit () # confirma o Insert
#     print ("inserido com sucesso ! ID:", cursor.lastrowid) # -> RETORNA O ID QUE FOI CRIADO

    # UPDATE atualizar um registro existente 
#     sql_update = "UPDATE clientes SET email = %s where id_cliente = %s"
#     cursor.execute(sql_update, ("novo@gmail.com", 1))
#     conexao.commit() # -> confirma o update
#     print ("linhas afetadas", cursor.rowcount)

#  --------- delete : remover um registro
    cursor.execute("DELETE FROM  clientes where id_cliente = %s", 5)
    conexao.commit() # confirma o DELETE
except Exception as erro:
    conexao.rollback() # desfaz tudo de algo que deu errado
    print("erro ! operação revertida:", erro)
# finally:
#     cursor.close()
#     conexao.close() # -> fechar a conexão com o banco de dados



