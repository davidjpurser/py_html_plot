from tick import Tick
from plot import Plot
from normaliser import Normaliser
from gridline import Gridline

class NormalisedPlot(Plot):
    

    def __init__(self, title=None, x_label=None, y_label=None):
        super().__init__(title, x_label, y_label)
        self.x_normaliser = Normaliser(0, 100)
        self.y_normaliser = Normaliser(0, 100)

    def add_gridlines(self, x_step=None, y_step=None): 
        if x_step is not None:
            for inc in range(self.x_normaliser.min_val, self.x_normaliser.max_val + 1, x_step):
                gl = Gridline(inc, 'x')
                self.add_normalised_object(gl)

        if y_step is not None:
            for inc in range(self.y_normaliser.min_val, self.y_normaliser.max_val + 1, y_step):
                gl = Gridline(inc, 'y')
                self.add_normalised_object(gl)

    def add_ticks(self, x_step=None, y_step=None,x_tick_label=None, y_tick_label=None):
        if x_step is not None:
            for i,inc in enumerate(range(self.x_normaliser.min_val, self.x_normaliser.max_val + 1, x_step)):
                if x_tick_label is not None and i < len(x_tick_label):
                    tk = Tick(inc, 'x', x_tick_label[i])
                else:
                    tk = Tick(inc, 'x', inc)
                self.add_normalised_object(tk)

        if y_step is not None:
            for i,inc in enumerate(range(self.y_normaliser.min_val, self.y_normaliser.max_val + 1, y_step)):
                if y_tick_label is not None and i < len(y_tick_label):
                    tk = Tick(inc, 'y', y_tick_label[i])
                else:
                    tk = Tick(inc, 'y', inc)
                self.add_normalised_object(tk)


    def add_normalised_object(self, object):
        object.x_normaliser = self.x_normaliser
        object.y_normaliser = self.y_normaliser
        self.add_object(object)

    def get_x_normaliser(self):
        return self.x_normaliser
    
    def get_y_normaliser(self):
        return self.y_normaliser

    def set_x_max(self, x_max):
        self.x_normaliser.max_val = x_max
    def set_y_max(self, y_max):
        self.y_normaliser.max_val = y_max
    def set_x_min(self, x_min):
        self.x_normaliser.min_val = x_min
    def set_y_min(self, y_min):
        self.y_normaliser.min_val = y_min
