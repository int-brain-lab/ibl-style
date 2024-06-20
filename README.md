# IBL Style

[![PyPI - Version](https://img.shields.io/pypi/v/ibl-style.svg)](https://pypi.org/project/ibl-style)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ibl-style.svg)](https://pypi.org/project/ibl-style)

-----

## Installation

```console
pip install ibl-style
```

## Figure guidelines

Original figures generated from Python or MATLAB code should be saved in PDF (or SVG) format. These formats are *vector graphic* formats, meaning that the quality is the same regardless of the final resolution. It's okay to temporarily convert figures to PNG for an initial submission of a paper, but be aware that PNG is a raster format which means the image has been converted to pixels and the resolution is now fixed. Unless absolutely necessary you should never use JPG/JPEG/GIF formats -- these raster formats are lossy formats and your figures may end up looking bad.

### Size

Figures should be **90 mm** for single column or **180 mm** wide for double column. In most journals the maximum height of a figure is **170 mm**.

### Font

Figures should use Helvetica for all fonts. You can find the necessary font files in this repository, double click the font file and choose **install** on Windows or Mac.

 - **Figure panel letters** should be in *lowercase* *8-point* *bold* font with no period
 - **Additional text** on a figure should be in *italics* in *7-point* font, only the first letter should be capitalized
 - **Axis labels** should be in *7-point* font with no period, only the first letter should be capitalized
 - **Tick marks** should be in *6-point* font

#### Axes

 - Axis lines should usually be 0.5 pt width, and ticks should be 0.25. Keep lines in the range 0.25-1 pt
 - Axis labels should identify the value reported and (units) in parenthesis

#### Units

 - Separate thousands with commas (1,000)
 - Percentages should range from 0 to 100

### Colors

```
# To-do code example
```