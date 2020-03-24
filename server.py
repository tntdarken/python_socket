#!/usr/bin/python
import socket 
import threading
import time
import tkinter as tk

##
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.geometry("370x100")
        self.pack()
        self.create_widgets()
        self.host = '192.168.1.7'
        self.port = 7000
        self.addr = (self.host, self.port)
        self.timeOut = 10

    def create_widgets(self):
        self.btAbrirSocket = tk.Button(self)
        self.btAbrirSocket["text"] = "Abrir socket"
        self.btAbrirSocket["command"] = self.abrirSocket
        self.btAbrirSocket.pack(side="top")

        self.cxMensagem = tk.Entry(self)
        self.cxMensagem.pack(side="top")
        
        self.btEnviarMensagem = tk.Button(self)
        self.btEnviarMensagem["text"] = "Enviar mensagem"
        self.btEnviarMensagem["command"] = self.enviarMensagem
        self.btEnviarMensagem.pack(side="top")

        self.btSair = tk.Button(self, text="Sair", fg="red",
                              command=self.master.destroy)
        self.btSair.pack(side="bottom")

    def enviarMensagem(self):
        mensagem = self.cxMensagem.get()
        self.cxMensagem.delete(0, 'end')
        self.con.send(mensagem.encode())

    def abrirSocket(self):
        self.con = self.criarConexao()
        t = threading.Thread(target=self.init)
        t.daemon = True
        t.start()

    def init(self):
        print(self.con)
        self.receberMensagens(self.con)
        print("Abriu o socket")

    def criarConexao(self):
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        serv_socket.bind(self.addr) 
        serv_socket.listen(self.timeOut)
        return serv_socket

    def receberMensagens(self, con):
        conn, cliente = con.accept() # O accept retorna um array com dois elementos, por isso duas variaveis
        self.con = conn
        while True:
            print("aguardando mensagem")
            recebe = conn.recv(1024)
            if not recebe:
                self.fecharConexao(conn)
                break
            else:        
                print("mensagem recebida: "+ recebe.decode())

    def fecharConexao(self, con):
        print('Obrigado!')
        con.close()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
