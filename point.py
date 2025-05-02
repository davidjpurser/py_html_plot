import html

class Point:

    def __init__(self, x, y, data_name=None):
        self.x = x
        self.y = y
        self.data_name = data_name
        self.x_normaliser = None
        self.y_normaliser = None

    def get_x(self):
        if self.x_normaliser:
            return self.x_normaliser.normalise(self.x)
        return self.x
    
    def get_y(self):    
        if self.y_normaliser:
            return self.y_normaliser.normalise(self.y)
        return self.y   

    def get_html(self):
        x = self.get_x()
        y = 100 - self.get_y()
        obj = html.HTML('div')
        obj.set_attr('class', 'point')
        obj.set_style('left', f'{x}%')
        obj.set_style('top', f'{(y)}%')
        if self.data_name:
            obj.set_attr('data-name', self.data_name)
        return obj