import matplotlib.pyplot as plt

MM_TO_INCH = 1 / 25.4


def single_column_fig():
    return plt.figure(figsize=(90 * MM_TO_INCH, 170 * MM_TO_INCH))


def double_column_fig():
    return plt.figure(figsize=(180 * MM_TO_INCH, 170 * MM_TO_INCH))


def get_coords(extent, ratios=[1], space=15, pad=7.5, span=(0, 1)):
    """
    Computes the coordinates (spans) of panels along a given extent (width or height) of a figure.

    This function calculates panel positions based on specified size ratios, spacing, and padding. It helps divide
    a figure into multiple panels with customizable dimensions and gaps.

    Parameters:
    -----------
    extent : float
        The total extent of the figure in millimeters (mm), either width or height.

    ratios : list of float, optional (default=[1])
        A list of relative ratios for the panels. The number of elements determines the number of panels.
        For example, [1, 1, 1] creates 3 panels of equal size.

    space : float or list of float, optional (default=15)
        The spacing between panels in millimeters (mm).
        - If a single value is provided, it is applied uniformly between all panels.
        - If a list is provided, each value specifies the spacing between consecutive panels.
          The length of this list must be one less than the length of the `ratios` list.
        Example: If `ratios=[1, 1, 2]`, then `space=[5, 10]` sets 5 mm between the first two panels and 10 mm between the next.

    pad : float, optional (default=7.5)
        The padding (margin) in millimeters (mm) from the starting edge (left or top) of the figure to the first panel.

    span : tuple of float, optional (default=(0, 1))
        The normalized span (0 to 1) over which the panels extend. For example:
        - (0, 1): Full figure extent.
        - (0.2, 0.8): Panels occupy the central 60% of the figure.

    Returns:
    --------
    list of list of float
        A list of coordinates representing the spans for each panel. Each span is a list of two values indicating
        the start and end positions of the panel along the extent.

    Example:
    --------
    >>> get_coords(extent=100, ratios=[1, 1, 2], space=[5, 10], pad=7.5)
    [[0.075, 0.26875], [0.31875, 0.5125], [0.6124, 1.0]]
    """
    full_span = span[1] - span[0]

    if isinstance(space, list):
        space = [s / extent for s in space]
    else:
        space = [space / extent] * (len(ratios) - 1)

    pad = pad / extent

    white_space = sum(space)
    available_space = (1 - white_space - pad) * full_span
    panel_span = available_space / sum(ratios)

    # Get the coordinates of the first panel
    coords = [[pad + span[0], pad + span[0] + panel_span * ratios[0]]]
    # Loop through the others to get the rest of the coordinates
    for i, r in enumerate(ratios[1:]):
        coords.append([coords[i][-1] + space[i], coords[i][-1] + space[i] + panel_span * r])

    return coords


def add_label(text, fig, xspan, yspan, padx=2.5, pady=2.5, fontsize=8):
    """
    Generates label information for annotating a panel within a Matplotlib figure.

    This function computes the coordinates and properties for placing a label (e.g., 'a', 'b', 'c')
    within a specified panel in a figure. It ensures proper padding and alignment based on
    figure dimensions.

    Parameters:
    -----------
    text : str
        The label text to display, such as 'a', 'b', or 'c'.

    fig : matplotlib.figure.Figure
        The Matplotlib figure object in which the label will be placed.

    xspan : tuple of float
        The span (start and end) of the panel along the x-axis in figure coordinates.
        Example: `(0.1, 0.4)` places the label in a panel starting at 10% of the figure width.

    yspan : tuple of float
        The span (start and end) of the panel along the y-axis in figure coordinates.
        Example: `(0.6, 0.9)` places the label in a panel starting at 60% of the figure height.

    padx : float, optional (default=2.5)
        Padding to the left of the panel (in millimeters) for positioning the label.

    pady : float, optional (default=2.5)
        Padding from the top of the panel (in millimeters) for positioning the label.

    fontsize : int, optional (default=8)
        The font size for the label text.

    Returns:
    --------
    dict
        A dictionary containing the label properties:
        - `'label_text'`: The label text.
        - `'xpos'`: The x-coordinate for label placement.
        - `'ypos'`: The y-coordinate for label placement.
        - `'fontsize'`: The font size of the label.
        - `'weight'`: Font weight (set to `'bold'`).
        - `'ha'`: Horizontal alignment (`'right'`).
        - `'va'`: Vertical alignment (`'bottom'`).

    Example:
    --------
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots(figsize=(8, 6))
    >>> label_info = add_label('a', fig, xspan=(0.1, 0.4), yspan=(0.6, 0.9))
    """

    width, height = fig.get_size_inches() / MM_TO_INCH

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

