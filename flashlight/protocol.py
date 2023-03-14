import ujson
import socket
import logging

from flashlight.command import LightCommandModel
from flashlight import AbstractFlashlight


class FlashlightControlProtocol:
    def __init__(self, address: str, fl: AbstractFlashlight):
        logging.info(f"Connecting to: {address}")

        self.host, port = address.strip().split(":")
        self.port = int(port)

        self.connected = False
        self._connect(self.host, self.port)

        self.fl = fl

    def _connect(self, host: str, port: int):
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_TCP
        )

        try:
            self.socket.connect((host, port))
            self.connected = True

            logging.info("Connected.")

        except ConnectionRefusedError:
            self.connected = False

            logging.warning("Connection refused.")

    def _close(self):
        if not self.connected:
            self.socket.close()
            self.connected = False

    def poll(self):
        if not self.connected:

            logging.info("Reconnecting.")

            self._connect(self.host, self.port)

        else:
            try:
                content = self.socket.recv(1024)
            except ConnectionResetError:
                self.connected = False
                self._close()
                return

            if len(content):
                message = LightCommandModel(
                    **ujson.loads(content.decode("utf-8"))
                )

                message.execute(self.fl)
            else:
                self.connected = False
                self._close()
