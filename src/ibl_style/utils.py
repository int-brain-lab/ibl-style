import matplotlib.pyplot as plt

mm_to_inch = 1 / 25.4


def single_column_fig():
    return plt.figure(figsize=(90 * mm_to_inch, 170 * mm_to_inch))


def double_column_fig():
    return plt.figure(figsize=(180 * mm_to_inch, 170 * mm_to_inch))


def get_coords(dimension, ratios=None, space=15, pad=7.5, span=(0, 1)):
    """

    :param dimension:
    :param ratios:
    :param space: the space between panels in the figure in mm. If a single value is given then the same spacing is applied
    between each row or column. If a list is given, the specified . The dimension of the list must be n-1 the number of rows
    or columns as it indicates the interval between.
    spacing is applied between each row or column.
    :param pad:
    :param span:
    :return:
    """

    extent = span[1] - span[0]

    if isinstance(space, list):
        space = [s / dimension for s in space]
    else:
        space = [space / dimension] * (len(ratios) - 1)

    pad = pad / dimension

    white_space = sum(space)
    available_space = (1 - white_space - pad) * extent
    panel_extent = available_space / sum(ratios)

    # Get the coordinates of the first panel
    coords = [[pad + span[0], pad + span[0] + panel_extent * ratios[0]]]
    # Loop through the others to get the rest of the coordinates
    for i, r in enumerate(ratios[1:]):
        coords.append([coords[i][-1] + space[i], coords[i][-1] + space[i] + panel_extent * r])

    return coords


def add_label(text, fig, xspan, yspan, padx=2.5, pady=2.5, fontsize=8):

    width, height = fig.get_size_inches() / mm_to_inch

    def _get_label_pos(dimension, coord, pad):
        return coord - pad / dimension

    label = {
        'label_text': text,
        'xpos': _get_label_pos(width, xspan[0], padx),
        'ypos': _get_label_pos(height, yspan[0], pady),
        'fontsize': fontsize,
        'weight': 'bold',
        'ha': 'right',
        'va': 'bottom'}

    return label

