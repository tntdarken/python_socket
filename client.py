import socket 

def main():
    socket = abrirSocket()
    enviarMensagem(socket)

def abrirSocket():
    ip = input('digite o ip de conexao: ')
    port = 7000
    addr = ((ip,port))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(addr)
    return client_socket

def enviarMensagem(socket):
    while True:
        mensagem = input("digite uma mensagem para enviar ao servidor: ")
        if mensagem != 'sair':
            socket.send(mensagem.encode()) 
            print('mensagem enviada')
            recebe = socket.recv(1024)
            print('/n mensagem recebida:'+ recebe.decode())
        else:
            fecharSocket(socket)
            break

def fecharSocket(socket):
    socket.close()
    
main()
