from __future__ import annotations
import socket


class WebSocket:
    def __init__(self, **kwargs) -> WebSocket:
        self.__port = int(kwargs.get("port", 5555))
        self.__Host = socket.gethostbyname(socket.gethostname())
        self.__buffer = int(kwargs.get("buffer", 1024))

        self.__Function = kwargs.get("func", None)

        self.__Socket = socket.socket()
        self.__Socket.connect((self.__Host, self.__port))

    __author__ = "Luca Michael Schmidt"
    __version__ = "0.0.1a"
    __doc__ = \
        """
        This is a WebSocket class, specified for Client use. Buffer size and Port can be specified as keyword arguments.
        To process the received data, just put a function with one argument ONLY (data) in the constructor WebSocket(func=function)
        -> Client works perfectly fine in sending and receiving without modification
        """

    def __del__(self):
        self.__Socket.send("!DISCONNECT".encode())
        self.__Socket.close()

    def send(self, data) -> send:
        self.__Socket.send(f"{data}".encode())

        rec = self.__Socket.recv(self.__buffer)
        rec = rec.decode()
        print(rec)

        if self.__Function:
            self.__Function(rec)

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
