class Rescaler:

    @staticmethod
    def computeScale(bounds, canvas):
        canvas_width = canvas.winfo_reqwidth()
        canvas_height = canvas.winfo_reqheight()
        xdist = bounds.xmax - bounds.xmin
        ydist = bounds.ymax - bounds.ymin
        xscale = 0.99 * canvas_width / xdist
        yscale = 0.99 * canvas_height / ydist
        scale = min(xscale, yscale)
        return -bounds.xmin, -bounds.ymin, scale

