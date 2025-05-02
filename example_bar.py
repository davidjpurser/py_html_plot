import page
import label
from barchart import Barchart
from stackedbar import StackedBar


pg = page.Page()

data1 = [1,2,3,4,10]
data2 = [2,3,1,5,1]
data3 = [0,0,2,6,1]

pastel_colours = ['#FFB3B3', '#FFF5BA', '#B3E5B3']

bar = Barchart("Bar Chart Example", "X Axis", "Y Axis",'x')
bar.add_series(data1)
bar.add_series(data2)
bar.add_series(data3)
bar.set_colours(pastel_colours)
bar.normalise_on_max()
bar.add_gridlines(y_step=2)
bar.add_ticks(y_step=1)
bar.set_separator_gaps(1, 15)
bar.set_side_gaps(5, 5)
bar.set_bar_width(20)
bar.generate_regions()

plot_html = bar.get_html()
# plot_html.set_style('aspect-ratio', '1 / 1')
plot_html.set_style("margin-top", "30px")
pg.add_object(plot_html)

bar = StackedBar("Bar Chart Example", "X Axis", "Y Axis",'x')
bar.add_series(data1)
bar.add_series(data2)
bar.add_series(data3)
bar.set_colours(pastel_colours)
bar.normalise_on_max()
bar.add_gridlines(y_step=2)
bar.add_ticks(y_step=1)
bar.set_separator_gaps(1, 15)
bar.set_side_gaps(5, 5)
bar.set_bar_width(20)
bar.generate_regions()

plot_html = bar.get_html()
# plot_html.set_style('aspect-ratio', '1 / 1')
plot_html.set_style("margin-top", "30px")

pg.add_object(plot_html)



pg.get_html().set_text("""Testing a bar chart.
<br>
""")

pg.get_html().set_style("padding-bottom", "30px")

# print the html to a file
with open('example_bar.html', 'w') as file:
    file.write(pg.render())
