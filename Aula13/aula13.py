import pymysql as pysql
# cria a conexão com o banco de dados

conexao = pysql.connect(
    host="localhost",                     # endereço de servidor (local = 'localhost")
    user="root",                       # usuario do mysql
    password="" ,                       # senha do mysql
    database="bd_livrariaonline" ,       # banco que voce ja criou
    port=3306                         # porta padrão do mysql    
)

# cria cursor - versão dicionario (retorna {"coluna":"valor"})
cursor = conexao.cursor(pysql.cursors.DictCursor)

# --- buscar todos os registros ------------
cursor.execute("select * FROM clientes")
todos = cursor.fetchall()

# for cliente in todos:
#     print(cliente["nome"],"-", cliente["email"],"-", cliente["telefone"])

# buscar um unico registro por ID

# cursor.execute("select * from clientes where id_cliente =1")
# cliente = cursor.fetchone()
# print (cliente) # 

# buscar um filtro dinamico (seguro)
nome_busca = "ursula%"
cursor.execute("select * from clientes  where nome like %s",(nome_busca),)
resultado = cursor.fetchall()
print(resultado)
