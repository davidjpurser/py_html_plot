from tick import Tick
class Gridline(Tick):

    def get_html(self):
        obj = super().get_html()
        obj.add_class('gridline')
        x = self.get_x()
        y = 100- (self.get_y())
        obj.set_style('left', f'{x}%')
        obj.set_style('top', f'{(y)}%')
        if self.dir == 'x':
            obj.set_style('top', f'0%')
            obj.set_style('width', f'1px')
            obj.set_style('height', f'100%')
        elif self.dir == 'y':
            obj.set_style('width', f'100%')
            obj.set_style('height', f'1px')

        return obj