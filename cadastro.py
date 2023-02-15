import pyodbc

dados = (
    "Driver={****};"
    "User=****;"
    "Password=****;"
    "Server=****;"
    "DataBase=****;"
)

conexao = pyodbc.connect(dados)
print("A conexão foi feita")

user_ = str(input('Qual será seu nome de usuario? '))

cursor = conexao.cursor()

comando = """select user_ from usuarios"""
verificacao = str(cursor.execute(comando).fetchall())
if user_ in verificacao:
    print('esse usuario já existe')
else:
    pass_ = str(input('Qual será sua senha? '))
    novo_usuario = f"""insert into usuarios values(default, '{user_}', '{pass_}');"""
    cursor.execute(novo_usuario)
    cursor.commit()