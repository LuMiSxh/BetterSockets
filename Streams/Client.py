import asyncio


class WebSocket:
    def __init__(self, **kwargs):
        self.__port: int = kwargs.get("port", 8888)
        self.__ip: str = kwargs.get("ip", "127.0.0.1")

        self.__Reader, self.__Writer = None, None
        self.__func = kwargs.get("func", None)

    __author__ = "Luca Michael Schmidt"
    __version__ = "0.0.1a"


    def send(self, data):
        asyncio.run(self.__send(data))

    async def __send(self, data):
        self.__Reader, self.__Writer = await asyncio.open_connection(self.__ip, self.__port)

        self.__Writer.write(f"{data}".encode())
        await self.__Writer.drain()

        if self.__func:
            _data = await self.__Reader.read(100)
            if _data:
                retr = self.__func(_data)
                if retr:
                    self.__Writer.write(bytes(retr, "utf-8"))

        self.__Writer.close()


# Cl = WebSocket()
# Cl.send("Test")
