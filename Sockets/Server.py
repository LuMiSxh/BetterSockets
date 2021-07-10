from __future__ import annotations
import socket
from threading import Thread


class WebSocket:
    def __init__(self, **kwargs) -> WebSocket:
        self.__port = int(kwargs.get("port", 5555))
        self.__Host = "0.0.0.0"
        self.__buffer = int(kwargs.get("buffer", 1024))

        self.__Socket = socket.socket()

        self.__Function = kwargs.get("func", None)

        self.__bind()

    __author__ = "Luca Michael Schmidt"
    __version__ = "0.0.1a"
    __doc__ = \
    """
    This is a WebSocket class, specified for Hub (Server) use. Buffer size and Port can be specified as keyword arguments.
    To process the received data, just put a function with one argument ONLY (data) in the constructor WebSocket(func=function) >> Needs 
    to return a value to send back; if "None" is returned, nothing will be send back. 
    -> Server works completely fine in receiving messages without modification
    """

    def __del__(self):
        self.__Socket.close()

    def __bind(self) -> socket:
        self.__Socket.bind((self.__Host, self.__port))

    def listen(self) -> Thread:
        self.__Socket.listen(1)
        print(f"[STATUS] Listening")

        while True:
            conn, addr = self.__Socket.accept()
            thread = Thread(target=self.__flag, args=[conn, addr])
            thread.start()

    def __flag(self, conn, addr):
        print(f"[INCOMING] {addr}")
        while True:
            try:
                msg = conn.recv(self.__buffer)
            except socket.error():
                print(f"[STATUS] Error occurred during handling address: {addr}")
                break
            msg = msg.decode()
            print(msg)
            if msg == "!DISCONNECT":
                print("[STATUS] Disconnect")
                conn.close()
                break

            # Checking if a function is insterted for data valuation
            if self.__Function:
                retr = self.__Function(msg)
                if retr:
                    if retr != "!DISCONNECT":
                        conn.send(f"{retr}".encode())


# Server = WebSocket()
# Server.listen()
