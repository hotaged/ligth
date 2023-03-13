import click

from flashlight.ui import FlashlightUI
from flashlight.protocol import FlashlightControlProtocol


@click.command()
@click.option(
    '--address',
    default='127.0.0.1:9999'
)
def cli(address: str):
    ui = FlashlightUI()
    proto = FlashlightControlProtocol(address)

    ui.add_periodic_task(lambda: proto.poll(ui), 100)
    ui.title("Flashlight")
    ui.mainloop()


if __name__ == '__main__':
    cli()
