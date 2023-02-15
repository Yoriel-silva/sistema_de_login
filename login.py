'''
1 - usuario/senha
2 - cadastro - adicionalos ao banco dados; login - ver se os dados existem no banco de dados e permitir o acesso
3 - cadastro - não posso aceitar usuarios iguais; login - o usuario e asnha devem estar certos
4 - cadastro - adição dos daddos no databse; login - permitir o accesso
5 - cadastro - perguntar qual vai ser o usuario e ver se não existe outro igual, qual vai ser a senha e então adicionar esses dados do database;
login - olhar no banco de dados e ver se o usuario digitado existe e se sua senha esta correta, caso sim permitit o acesso, caso não negue o acceso
'''

import pyodbc

dados = (
    "Driver={****};"
    "User=****;"
    "Password=****;"
    "Server=****;"
    "DataBase=****;"
)

conexao = pyodbc.connect(dados)
cursor = conexao.cursor()

user_ = str(input('Qual é seu nome de usuario? '))

comando_user = f"""select user_ from usuarios where user_ = '{user_}'"""
verificacao_user = str(cursor.execute(comando_user).fetchall())
if user_ in verificacao_user:

    pass_ = str(input('Qual é sua senha? '))

    comando_pass = f"""select pass_ from usuarios where user_ = '{user_}'"""
    verificacao_pass = str(cursor.execute(comando_pass).fetchall())
    if pass_ in verificacao_pass:
        print('Acesso permitido')
    else:
        print('essa senha está errada')
else:
    print('esse usuario nao existe')

