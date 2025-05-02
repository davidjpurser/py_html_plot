from plot import Plot
from normaliser import Normaliser
from normalised import NormalisedPlot


class ScatterPlot(NormalisedPlot):
    """A class for creating and managing scatter plots with normalised points."""

    def __init__(self, title=None, x_label=None, y_label=None):
        super().__init__(title, x_label, y_label)
        self.points = []

    def add_point(self, point):
        self.points.append(point)
        self.add_normalised_object(point)

    def get_x_max(self):
        return max([point.x for point in self.points])
    
    def get_y_max(self):
        return max([point.y for point in self.points])
    
    def get_x_min(self):
        return min([point.x for point in self.points])
    
    def get_y_min(self):
        return min([point.y for point in self.points])

    def compute_x_max(self):
        self.set_x_max(self.get_x_max())
    def compute_y_max(self):
        self.set_y_max(self.get_y_max())
    def compute_x_min(self):
        self.set_x_min(self.get_x_min())
    def compute_y_min(self):
        self.set_y_min(self.get_y_min())