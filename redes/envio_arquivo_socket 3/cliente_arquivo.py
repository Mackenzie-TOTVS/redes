import socket
import os

arquivo = input("Digite o nome do arquivo para enviar: ")

if not os.path.exists(arquivo):
    print("Arquivo não encontrado.")
    exit()

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 12345))

cliente.send(arquivo.encode())

with open(arquivo, 'rb') as f:
    dados = f.read(1024)
    while dados:
        cliente.send(dados)
        dados = f.read(1024)

cliente.close()
print("Arquivo enviado com sucesso.")
