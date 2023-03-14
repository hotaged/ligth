import click
import logging

from flashlight.ui import FlashlightUI
from flashlight.protocol import FlashlightControlProtocol
from flashlight.server import setup_command_listener

logging.basicConfig(level=logging.DEBUG)


@click.command()
@click.option(
    '--address',
    default='127.0.0.1:9999',
    help='host:port of server to connect.'
)
@click.option(
    '--method',
    type=click.Choice(['tcp', 'fastapi'], case_sensitive=False),
    default='fastapi',
    help='Method for interaction.'
)
def cli(address: str, method: str):
    ui = FlashlightUI()

    if method == 'fastapi':
        setup_command_listener(address, ui)
    elif method == 'tcp':
        proto = FlashlightControlProtocol(address, ui)
        ui.add_periodic_task(lambda: proto.poll(), 100)
    else:
        exit(-1)

    ui.title("Flashlight")
    ui.mainloop()


if __name__ == '__main__':
    cli()
