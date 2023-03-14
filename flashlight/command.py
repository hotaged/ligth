from pydantic import (
    BaseModel,
    Field
)
from flashlight import AbstractFlashlight
from typing import Callable


class LightCommandModel(BaseModel):
    command: str
    metadata: float

    class Meta:
        commands: dict[str, Callable[[AbstractFlashlight, float], None]] = {}

    @classmethod
    def new_command(cls, name: str):
        def wrapper(function: callable):
            cls.Meta.commands.update({name: function})
            return function

        return wrapper

    def execute(self, fl: AbstractFlashlight):
        if self.command in self.Meta.commands:
            self.Meta.commands[self.command](fl, self.metadata)


@LightCommandModel.new_command("ON")
def flashlight_on(fl: AbstractFlashlight, *_):
    fl.switch(True)


@LightCommandModel.new_command("OFF")
def flashlight_off(fl: AbstractFlashlight, *_):
    fl.switch(False)


@LightCommandModel.new_command("COLOR")
def flashlight_color(fl: AbstractFlashlight, color: float):
    fl.change_color(color)
