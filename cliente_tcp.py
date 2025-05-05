import socket

# Cria o socket do cliente (IPv4, TCP)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tenta conectar ao servidor (IP, Porta)
cliente.connect(('localhost', 54321))

# Envia mensagem para o servidor
cliente.sendall("Olá, servidor!".encode())

# Fecha a conexão
cliente.close()
