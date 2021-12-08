class client:

    def __init__(self):
        import socket

        self.ip = "192.168.15.217"  # IP of Raspberry Pi
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.client.connect((self.ip, 8080))
            print("CLIENT: connected")

        except ConnectionRefusedError:
            print("CLIENT: disconnected")
            self.client.close()
            quit()


    def send(self, message):
        self.client.send(message.encode())

    def listen(self):
        from_server = self.client.recv(4096).decode()
        return from_server