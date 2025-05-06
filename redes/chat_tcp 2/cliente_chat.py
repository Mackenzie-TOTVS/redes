import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 12345))

while True:
    mensagem = input("Cliente: ")
    cliente.send(mensagem.encode())
    if mensagem.lower() == "quit":
        break

    resposta = cliente.recv(1024).decode()
    if resposta.lower() == "quit":
        print("Servidor encerrou a conversa.")
        break
    print(f"Servidor: {resposta}")

cliente.close()
