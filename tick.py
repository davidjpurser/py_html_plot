import html
from point import Point

class Tick(Point):
    def __init__(self,val, dir, data_name=None):
        self.dir = dir
        if self.dir == 'x':
            x = val
            y = 0
        elif self.dir == 'y':
            x = 0
            y = val
        else:
            raise ValueError("Invalid direction. Use 'x' or 'y'.")
        super().__init__(x, y, data_name)

    def get_html(self):
        x = self.get_x()
        y = 100 - self.get_y()
        obj = html.HTML('div')
        obj.add_class('tick')
        obj.add_class(f'tick-{self.dir}')
        obj.set_style('left', f'{x}%')
        obj.set_style('top', f'{(y)}%')
        if self.data_name != None:
            obj.set_attr('data-label',self.data_name)
        return obj