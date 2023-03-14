import threading
import uvicorn
import logging

from fastapi import (
    FastAPI,
    Depends
)

from flashlight.command import LightCommandModel
from flashlight import AbstractFlashlight
from typing import Callable

server = FastAPI(
    docs_url="/"
)


def thread(function: Callable):
    def decorator(*args, **kwargs):
        t = threading.Thread(
            target=function,
            args=args, kwargs=kwargs,
            daemon=True
        )
        t.start()
        return t
    return decorator


@thread
def setup_command_listener(address: str, fl: AbstractFlashlight):
    logging.warning("Starting")

    @server.post('/command')
    async def command(body: LightCommandModel, fl: AbstractFlashlight = Depends(fl)):
        body.execute(fl)
        return {}

    host, port = address.strip().split(":")

    uvicorn.run(server, host=host, port=int(port))
