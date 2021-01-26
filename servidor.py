import socket
host = 'localhost'
port = 8001
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)
print('Aguarde a conexao...')
con, cliente = serv_socket.accept()
print('Conectado')
print('Aguardando mensagem...')

enviar = ''
while(enviar!= 'sair'):
    recebe = con.recv(1024)
    print('Mensagem recebida' + recebe.decode())
    enviar = input('Digite uma mensagem para enviar ao Cliente: ')
    con.send(enviar.encode())


serv_socket.close()