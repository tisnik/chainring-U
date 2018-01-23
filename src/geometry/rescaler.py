class Rescaler:

    @staticmethod
    def computeScale(bounds, width, height):
        xdist = bounds.xmax - bounds.xmin
        ydist = bounds.ymax - bounds.ymin
        xscale = 0.99 * width / xdist
        yscale = 0.99 * height / ydist
        scale = min(xscale, yscale)
        return -bounds.xmin, -bounds.ymin, scale

    @staticmethod
    def computeScaleForCanvas(bounds, canvas):
        canvas_width = canvas.winfo_reqwidth()
        canvas_height = canvas.winfo_reqheight()
        return Rescaler.computeScale(bounds, canvas_width, canvas_height)

