import random
import logging
import socketserver
import ujson
import pydantic

logging.basicConfig(level=logging.INFO)


class Message(pydantic.BaseModel):
    command: str
    metadata: float


messages = [
    Message(command="COLOR", metadata=i / 10) for i in range(4, 10)
]


class TCPHandler(socketserver.BaseRequestHandler):
    def setup(self) -> None:
        logging.info(f"Connected: {self.client_address}")

    def handle(self) -> None:
        self.request.sendall(
            ujson.dumps(
                random.choice(messages).dict()
            ).encode('utf-8')
        )

    def finish(self) -> None:
        logging.info(f"Disconnected: {self.client_address}")


if __name__ == '__main__':
    with socketserver.TCPServer(("127.0.0.1", 9999), TCPHandler) as server:
        server.serve_forever()
