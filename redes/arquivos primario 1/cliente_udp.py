import socket

# Cria o socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envia mensagem para o servidor
mensagem = "Olá, servidor UDP!"
cliente.sendto(mensagem.encode(), ('localhost', 54321))


# Fecha o socket
cliente.close()
