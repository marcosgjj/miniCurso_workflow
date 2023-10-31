import sys

USER_NAME = sys.argv[1]
PASSWORD = sys.argv[2]

print("Tentando autenticar com as seguintes credenciais:")
print("Username:", USER_NAME)
print("Password", PASSWORD)

if USER_NAME == 'marcos' and PASSWORD == '123456':
    print("Autenticação OK")
else:
    raise Exception("Login e senhas incorretos")
