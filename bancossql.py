import pyodbc

dados_conexao = (
    "Driver={SQL server};"
    "Server=Bruno-Pc;"
    "Database=PythonSQL;"       
)
conexao = pyodbc.connect(dados_conexao)
print("Conectado")

cursor = conexao.cursor()

comando = """INSERT INTO Vendas (id_vendas, cliente, produto, quantidade, data_venda, preço)VALUES
    (1, 'rodrigo', 'carro', 1, 25/11/2021, 20000)"""
cursor.execute(comando)
cursor.commit()