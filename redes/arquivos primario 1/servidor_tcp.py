import socket

# Cria o socket do servidor (IPv4, TCP)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP e Porta que o servidor vai escutar
servidor.bind(('localhost', 12345))

# Servidor começa a escutar conexões
servidor.listen()

print("Servidor TCP esperando conexão...")

# Aceita a conexão de um cliente
conexao, endereco = servidor.accept()
print(f"Conectado com {endereco}")

# Recebe mensagem do cliente
mensagem = conexao.recv(1024).decode()
print(f"Mensagem recebida do cliente: {mensagem}")

# Fecha a conexão
conexao.close()
