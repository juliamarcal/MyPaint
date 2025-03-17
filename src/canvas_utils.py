import tkinter as tk

def draw_pixel(canvas, x, y, color="black"):
    """
    Draws a pixel on the given canvas.
    
    :param canvas: The Tkinter canvas where the pixel will be drawn.
    :param x: X-coordinate of the pixel.
    :param y: Y-coordinate of the pixel.
    :param color: Color of the pixel. Default is black.
    """
    canvas.create_rectangle(x, y, x+1, y+1, outline=color, fill=color)

def transform_coords_to_center(coord, type, canvas):
    """
    Transforms coordinates to be centered relative to the canvas.
    
    :param coord: The coordinate to transform.
    :param type: The type of coordinate ('x' or 'y').
    :param canvas: The Tkinter canvas to get width and height.
    :return: Transformed coordinate.
    """
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    return coord - (width // 2) if type == "x" else (height // 2) - coord

def transform_coords_from_center(coord, type, canvas):
    """
    Transforms coordinates from centered values back to normal coordinates.
    
    :param coord: The centered coordinate to transform back.
    :param type: The type of coordinate ('x' or 'y').
    :param canvas: The Tkinter canvas to get width and height.
    :return: Transformed coordinate.
    """
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    return coord + (width // 2) if type == "x" else (height // 2) - coord

def clear_canvas(canvas, line_drawer=None, circle_drawer=None):
    """
    Clears the canvas and resets optional drawer objects.
    
    :param canvas: The Tkinter canvas to be cleared.
    :param line_drawer: Optional line drawer object to reset.
    :param circle_drawer: Optional circle drawer object to reset.
    """
    canvas.delete("all")
    if (line_drawer):
        line_drawer.reset()
    if (circle_drawer):
        circle_drawer.reset()
