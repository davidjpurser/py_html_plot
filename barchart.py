from region import Region
from plot import Plot
from normaliser import Normaliser
from normalised import NormalisedPlot

class Barchart(NormalisedPlot):
    """A class for creating and managing normalized bar chart plots."""


    colours = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#000000', '#FFFFFF']

    def __init__(self,title, x_label, y_label, dir = 'x'):
        self.data = []
        super().__init__(title, x_label, y_label)
        self.group_gap = 0 
        self.series_gap = 0
        self.start_gap = 0
        self.end_gap = 0
        self.bar_width = 10
        self.colours = None
        self.dir = dir

    def add_series(self, series):
        self.data.append(series)

    def set_colours(self, colours):
        if len(colours) < len(self.data):
            raise ValueError("Number of colours needs to be equal to or greater than number of series")
        self.colours = colours

    def get_series_colour(self, series_index):
        if self.colours is None:
            return Barchart.colours[series_index % len(Barchart.colours)]
        else:
            return self.colours[series_index % len(self.colours)]

    def add_normalised_object(self, object):
        object.x_normaliser = self.x_normaliser
        object.y_normaliser = self.y_normaliser
        self.objects.append(object)

    def set_bar_width(self, bar_width):
        self.bar_width = bar_width

    def get_data_max(self):
        return max([max(x) for x in self.data])

    def normalise_on_max(self):
        max_val = self.get_data_max()
        if self.dir == 'x':
            self.y_normaliser.max_val = max_val
        elif self.dir == 'y':
            self.x_normaliser.max_val = max_val

    def set_separator_gaps(self, series_gap,group_gap=None):

        if self.group_gap is None:
            group_gap = series_gap
        self.group_gap = group_gap
        self.series_gap = series_gap

    def set_side_gaps(self, start_gap, end_gap=None):  
        if end_gap is None:
            end_gap = start_gap
        self.start_gap = start_gap
        self.end_gap = end_gap


    def count_groups(self):
        return max([len(x) for x in self.data])

    def get_position(self, series_index, datum_index, groups, series_count):
        total_parts = groups * series_count
        bar_width = self.bar_width
        x = datum_index * series_count + series_index
        space_per_group = series_count * bar_width + (series_count - 1) * self.series_gap + self.group_gap

        x_start = self.start_gap + (datum_index * space_per_group) + (series_index * (bar_width + self.series_gap)) 

        return x_start, x_start + bar_width


    def get_total_width(self):

        groups = self.count_groups()
        series_count = len(self.data)
        return self.start_gap + self.end_gap + (groups * series_count * self.bar_width) + ((groups - 1) * self.group_gap) + (groups * (series_count - 1) * self.series_gap)

    def set_dir_normaliser(self):
        total_width = self.get_total_width()

        if self.dir == 'x':
            self.x_normaliser.max_val = total_width
        elif self.dir == 'y':
            self.y_normaliser.max_val = total_width


    def get_y_position(self, series_index, datum_index, groups, series_count):
        return 0, self.data[series_index][datum_index]

    def generate_regions(self):

        self.set_dir_normaliser()

        groups = self.count_groups()
        series_count = len(self.data)

        for series_index, series in enumerate(self.data):

            for datum_index, datum in enumerate(series):
                x_start, x_end = self.get_position(series_index, datum_index, groups, series_count)
                y_start, y_end = self.get_y_position(series_index, datum_index, groups, series_count)
                if self.dir == 'x':
                    reg = Region(x_start, y_start, x_end, y_end)
                elif self.dir == 'y':
                    reg = Region(y_start, x_start, y_end, x_end)
                reg.set_colour(self.get_series_colour(series_index))
                reg.y_normaliser = self.y_normaliser
                reg.x_normaliser = self.x_normaliser
                self.add_object(reg)



    
        