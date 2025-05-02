import html


class Plot:
    """
    A class to represent a plot with a title, x-axis label, y-axis label, 
    and a collection of objects to be rendered as HTML.
    """


    def __init__(self, title, x_label, y_label):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)


    def get_html(self):

        obj = html.HTML('div')
        obj.set_attr('class', 'plot')
        for child in self.objects:
            obj.add_child(child.get_html())
        return obj