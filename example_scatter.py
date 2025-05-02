import page
import point
import region
import scatterplot
import label


myplot = scatterplot.ScatterPlot('Title', 'X-axis', 'Y-axis')

pastel_red = '#FFB3B3'
pastel_yellow = '#FFF5BA'
pastel_green = '#B3E5B3'

region3 = region.Region(0, 0, 100, 10, pastel_red)
myplot.add_normalised_object(region3)
region2 = region.Region(10, 5, 100, 10, pastel_yellow)
myplot.add_normalised_object(region2)
region1 = region.Region(50, 2, 100, 10, pastel_green)
myplot.add_normalised_object(region1)


myplot.set_x_max(100)
myplot.set_y_max(10)
myplot.set_x_min(0)
myplot.set_y_min(0)

myplot.add_gridlines(x_step=10, y_step=1)
myplot.add_ticks(x_step=10, y_step=1)


myplot.add_normalised_object(label.Label(95,4.5, f"green",))
myplot.add_normalised_object(label.Label(15,8.5, f"yellow",))
myplot.add_normalised_object(label.Label(95,1.5, f"red",))



data = [(0,0,'A'),(3,40,'C'),(4,20,'B'),(5,10,'D'),(6,30,'E'),(7,50,'F'),(8,60,'G'),(9,70,'H'),(10,80,'I')]


for x, y, name in data:
    pt = point.Point(y,x)
    pt.data_name = name
    myplot.add_point(pt)






plot_html = myplot.get_html()
plot_html.set_style('height', '500px')
plot_html.set_style("margin-top", "30px")
pg = page.Page()
pg.add_object(plot_html)

pg.get_html().set_text("""Here is some preamble.""")

pg.get_html().set_style("padding-bottom", "30px")

# print the html to a file
with open('example_scatter.html', 'w') as file:
    file.write(pg.render())
