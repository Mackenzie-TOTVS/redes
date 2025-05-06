import socket

# Cria o socket UDP
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP e porta para escutar
servidor.bind(('localhost', 12345))

print("Servidor UDP esperando mensagem...")

# Espera receber dados do cliente
mensagem, endereco = servidor.recvfrom(1024)
print(f"Mensagem recebida de {endereco}: {mensagem.decode()}")

# Fecha o socket
servidor.close()
