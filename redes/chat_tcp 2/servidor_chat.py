import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 12345))
servidor.listen(1)
print("Servidor esperando conexão...")

conexao, endereco = servidor.accept()
print(f"Conectado com {endereco}")

while True:
    mensagem = conexao.recv(1024).decode()
    if mensagem.lower() == "quit":
        print("Cliente encerrou a conversa.")
        break
    print(f"Cliente: {mensagem}")
    
    resposta = input("Servidor: ")
    conexao.send(resposta.encode())
    if resposta.lower() == "quit":
        break

conexao.close()
servidor.close()
