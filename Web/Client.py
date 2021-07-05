from __future__ import annotations
import socket


class WebSocket:
    def __init__(self, **kwargs) -> WebSocket:
        self.__port = int(kwargs.get("port", 5555))
        self.__Host = socket.gethostbyname(socket.gethostname())
        self.__buffer = int(kwargs.get("buffer", 1024))

        self.__Socket = socket.socket()
        self.__Socket.connect((self.__Host, self.__port))

    def __del__(self):
        self.__Socket.send("!DISCONNECT".encode())
        self.__Socket.close()

    def send(self, data) -> send:
        self.__Socket.send(f"{data}".encode())

    def reconnect(self) -> WebSocket:
        self.__Socket.send("!DISCONNECT".encode())
        self.__Socket.close()
        self.__Socket = socket.socket()
        self.__Socket.connect((self.__Host, self.__port))


Client = WebSocket()

while True:
    inp = input("What do you want to send:\n")
    if inp == "re":
        Client.reconnect()

    else:
        Client.send(inp)
