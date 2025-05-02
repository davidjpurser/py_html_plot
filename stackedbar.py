from barchart import Barchart

class StackedBar(Barchart):
    """A class for creating stacked bar charts."""


    def get_data_max(self):
        summed_series = [sum(x) for x in zip(*self.data)]
        return max(summed_series)

    def get_position(self, series_index, datum_index, groups, series_count):
        total_parts = groups 
        bar_width = self.bar_width
        x = series_index
        space_per_group = bar_width + self.group_gap

        x_start = self.start_gap + (datum_index * space_per_group) 
        return x_start, x_start + bar_width

    def get_y_position(self, series_index, datum_index, groups, series_count):
        
        y_start = 0
        for i in range(series_index):
            y_start += self.data[i][datum_index]
        return y_start, y_start + self.data[series_index][datum_index]


    def get_total_width(self):

        groups = self.count_groups()
        series_count = len(self.data)
        return self.start_gap + self.end_gap + (groups * self.bar_width) + ((groups - 1) * self.group_gap) 

        