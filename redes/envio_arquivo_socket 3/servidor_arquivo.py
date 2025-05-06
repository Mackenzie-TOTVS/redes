import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 12345))
servidor.listen(1)
print("Servidor aguardando conexão...")

conexao, endereco = servidor.accept()
print(f"Conectado a {endereco}")

nome_arquivo = conexao.recv(1024).decode()
with open(f"recebido_{nome_arquivo}", 'wb') as f:
    while True:
        dados = conexao.recv(1024)
        if not dados:
            break
        f.write(dados)

print("Arquivo recebido com sucesso.")
conexao.close()
servidor.close()
