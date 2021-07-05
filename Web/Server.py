from __future__ import annotations
import socket
from threading import Thread


class WebSocket:
    def __init__(self, **kwargs) -> WebSocket:
        self.__port = int(kwargs.get("port", 5555))
        self.__Host = "0.0.0.0"
        self.__buffer = int(kwargs.get("buffer", 1024))

        self.__Socket = socket.socket()

        self.__bind()

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
            msg = conn.recv(self.__buffer)
            msg = msg.decode()
            print(msg)
            if msg == "!DISCONNECT":
                print("[STATUS] Disconnect")
                conn.close()
                break



Client = WebSocket()
Client.listen()
