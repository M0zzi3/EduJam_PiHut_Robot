class server:

    def __init__(self):
        import socket
        self.ip = "192.168.15.217"

        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.serv.bind((self.ip, 8080))
        except OSError:
            pass

        self.serv.listen(5)
        self.client = False

        print("Server started")

        self.accept_client()



    def accept_client(self):

        self.conn, addr = self.serv.accept()
        print("Client Connected")



    def listen(self):
        return self.conn.recv(4096).decode()

    def send(self, message):
        self.conn.send(message.encode())

    def end_connection(self):
        self.conn.close()
        print("Server closed")
        quit()




