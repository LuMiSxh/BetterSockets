import asyncio
import socket


class Server:
    def __init__(self, **kwargs):
        self.__port: int = kwargs.get("port", 8888)
        self.__ip: str = kwargs.get("ip", "127.0.0.1")

        self.__rSocket = socket.socket()
        self.__Reader, self.__Writer = None, None

        self.__func = kwargs.get("func", None)
        self.__Server = None

    __author__ = "Luca Michael Schmidt"
    __version__ = "0.0.1a"

    def listen(self):
        asyncio.run(self.__listeningPrep())

    async def __listeningPrep(self):
        self.__Server = await asyncio.start_server(self.__listen, self.__ip, self.__port)

        async with self.__Server:
            await self.__Server.serve_forever()

    async def __listen(self, reader, writer):
        data = await reader.read(100)
        data = data.decode()
        print(data)

        if self.__func:
            retr = self.__func(data)

            if retr:
                writer.write(f"{retr}".encode())
                await writer.drain()


# S = Server()
# S.listen()
