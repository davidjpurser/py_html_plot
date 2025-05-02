
# Python generated CSS Plots

Supports bar, stacked and scatter plots using Pure HTML and CSS, no JavaScript used.

The plots are defined using python code, which generates the HTML and CSS code for the plots. The generated code can be used in any HTML environment, including static sites, blogs, and documentation pages.


## Features
- **Bar Plots**: Create simple bar plots
- **Stacked Bar Plots**: Create stacked bar plots
- **Scatter Plots**: Create scatter plots
- **Floating Pop-ups**: Add floating pop-ups to your plots for additional information.
- **Customizable**: Customize the appearance of your plots using CSS.
- **Responsive**: Plots are responsive and adapt to different screen sizes.
- **Lightweight**: No JavaScript required, making it lightweight and fast.


## Why use HTML and CSS Plots

Using pure HTML and CSS for plots eliminates the need for JavaScript, making your application lighter and reducing potential security vulnerabilities. It also ensures compatibility with environments where JavaScript is disabled or restricted, while still providing visually appealing and functional charts.

This tool was initially built with BookStack in mind, aiming to provide an interactive / non-static plots in a knowledge base environment where JavaScript is not allowed. However, it can be used in any HTML environment, including static sites, blogs, and documentation pages.

## Interface

The interface is still in development and very likely to change in the future!


## Limitations and Future Possibilities

The tool only supports points and rectangles (including axis aligned lines, which are just thin rectangles). This means that it is not possible to create arbitrary shapes or curves. The tool is also limited to 2D plots.

This is unlikely to change as the tool uses basic html and css to create the plots. More plot types that rely on these basic shapes may be added in the future.

Future possibilities include:
- Histograms
- Box and whisker plots
- Lines (non-axis aligned)
- Error bars

Unlikely:
- 3D plots
- Heatmaps / Colour maps
- Contours
- Polar plots
- non-linear trends or curves

In theory, the HTML and CSS could be constructed manually, however, the tool in intended to be used via the Python interface. As such, the tool focuses on creating a simple python interface, potentially generating somewhat-ugly (albeit still readable) HTML and CSS.


# Example
![example](example.svg)



