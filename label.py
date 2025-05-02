import html
from point import Point
class Label(Point):

    def get_html(self):
        x = self.get_x()
        y = 100 - self.get_y()
        obj = html.HTML('div')
        obj.add_class('label')
        obj.set_style('left', f'{x}%')
        obj.set_style('top', f'{(y)}%')
        obj.set_style('text-align', 'center')
        if self.data_name != None:
            obj.set_text(self.data_name)
        return obj