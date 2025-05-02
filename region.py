import html

class Region:
    def __init__(self, x, y, x_end, y_end, colour=None):
        self.x = x
        self.y = y
        self.x_end = x_end
        self.y_end = y_end
        self.colour = colour
        self.x_normaliser = None
        self.y_normaliser = None


    def set_colour(self, colour):
        self.colour = colour

    def get_left(self):
        if self.x_normaliser:
            return self.x_normaliser.normalise(self.x)
        return self.x
    
    def get_right(self):
        if self.x_normaliser:
            return 100 - self.x_normaliser.normalise(self.x_end)
        return 100 - self.x_end

    def get_bottom(self): 
        if self.y_normaliser:
            return self.y_normaliser.normalise(self.y)
        return self.y

    def get_top(self): 
        if self.y_normaliser:
            return 100 - self.y_normaliser.normalise(self.y_end)
        return 100 - self.y


    def get_html(self):
        left = self.get_left()
        right = self.get_right()
        top = self.get_top()
        bottom = self.get_bottom()

        obj = html.HTML('div')
        obj.set_attr('class', 'region')
        obj.set_style('left', f'{left}%')
        obj.set_style('top', f'{top}%')
        obj.set_style('right', f'{right}%')
        obj.set_style('bottom', f'{bottom}%')
        if self.colour:
            obj.set_style('background-color', self.colour)
        return obj
    

