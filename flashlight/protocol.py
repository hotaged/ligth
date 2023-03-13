import ujson
import socket
import logging
import pydantic

from abc import ABC
from typing import Callable

logging.basicConfig(level=logging.INFO)


class AbstractFlashlight(ABC):
    def change_color(self, color: float):
        raise NotImplementedError()

    def switch(self, mode: bool):
        raise NotImplementedError()


class FlashlightControlProtocol:
    _commands: dict[str, Callable[[AbstractFlashlight, float], None]] = {}

    class Message(pydantic.BaseModel):
        command: str
        metadata: float

    @classmethod
    def command(cls, name: str):
        def wrapper(function: callable):
            cls._commands.update({name: function})
            return function
        return wrapper

    def __init__(self, address: str):
        logging.info(f"Connecting to: {address}")

        self.host, port = address.strip().split(":")
        self.port = int(port)

        self.connected = False
        self._connect(self.host, self.port)

    def _connect(self, host: str, port: int):
        # TODO! Add error catching

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

    def _execute(self, fl: AbstractFlashlight, msg: Message):
        if msg.command in self._commands:
            self._commands[msg.command](fl, msg.metadata)

    def poll(self, flashlight: AbstractFlashlight):
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
                message = self.Message(
                    **ujson.loads(content.decode("utf-8"))
                )

                print(message.metadata)

                self._execute(flashlight, message)
            else:
                self.connected = False
                self._close()


@FlashlightControlProtocol.command("ON")
def flashlight_on(fl: AbstractFlashlight, *_):
    fl.switch(True)


@FlashlightControlProtocol.command("OFF")
def flashlight_off(fl: AbstractFlashlight, *_):
    fl.switch(False)


@FlashlightControlProtocol.command("COLOR")
def flashlight_color(fl: AbstractFlashlight, color: float):
    fl.change_color(color)
