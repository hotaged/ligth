from abc import ABC


class AbstractFlashlight(ABC):
    def change_color(self, color: float):
        raise NotImplementedError()

    def switch(self, mode: bool):
        raise NotImplementedError()

    def __call__(self):
        return self
