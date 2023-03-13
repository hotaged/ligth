import tkinter as tk

from colorsys import hsv_to_rgb
from flashlight.protocol import AbstractFlashlight


def rgb2hex(r, g, b) -> str:
    return f'#{r:02x}{g:02x}{b:02x}'


def hsv2hex(h: float) -> str:
    return rgb2hex(*tuple(map(lambda x: 255 if x >= 1.0 else int(x * 256), hsv_to_rgb(h, 0.5, 0.5))))


class FlashlightUI(tk.Tk, AbstractFlashlight):
    arm = None
    nose = None
    canvas = None
    light = None

    color = '#ffff00'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setup_window()
        self.setup_canvas()
        self.draw_flashlight()

        self.light = self.canvas.create_polygon(
            100, 200, 0, 0, 300, 0, 200, 200,
            fill=self.color
        )

        self.state = True

    def add_periodic_task(self, task: callable, delay: int):
        task()

        self.after(
            delay,
            lambda: self.add_periodic_task(task, delay)
        )

    def setup_window(self):
        self.geometry("300x500")
        self.resizable(False, False)

    def setup_canvas(self):
        self.canvas = tk.Canvas(self, width=300, height=500, background="white")
        self.canvas.pack(side="top", fill="both")

    def draw_flashlight(self):
        self.arm = self.canvas.create_rectangle(125, 250, 175, 450)
        self.canvas.itemconfigure(self.arm, fill='grey', outline='grey')

        self.nose = self.canvas.create_rectangle(100, 250, 200, 200)
        self.canvas.itemconfigure(self.nose, fill='grey', outline='grey')

    def change_color(self, color: float):
        if color > 1.0:
            color = 1.0
        elif color < 0.0:
            color = 0.0

        self.color = hsv2hex(color)

        if self.state:
            self.switch(self.state)

    def switch(self, mode: bool):
        self.state = mode

        if mode:
            self.canvas.itemconfigure(self.light, fill=self.color)
        else:
            self.canvas.itemconfigure(self.light, fill='#ffffff')


if __name__ == '__main__':
    ui = FlashlightUI()
    ui.title("Flashlight")
    ui.mainloop()
