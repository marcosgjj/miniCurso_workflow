import sys

username = sys.argv[1]
password = sys.argv[2]

print("Tentando autenticar com as seguintes credenciais:")
print("Username:", username)
print("Password", password)

if username == 'davi' and password == '123123':
    print("Autenticação OK")
else:
    raise Exception("Login e senhas incorretos")
