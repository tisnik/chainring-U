import tkinter


class Canvas(tkinter.Canvas):

    GRID_SIZE = 50

    def __init__(self, parent, width, height):
        super().__init__(parent, width=width, height=height,
                         background="white")
        self.draw_grid(width, height, Canvas.GRID_SIZE)

    def draw_grid(self, width, height, grid_size):
        for x in range(0, width, grid_size):
            self.create_line(x, 0, x, height, dash=7, fill="gray")
        for y in range(0, height, grid_size):
            self.create_line(0, y, width, y, dash=7, fill="gray")
