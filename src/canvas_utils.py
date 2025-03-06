import tkinter as tk

def draw_pixel(canvas, x, y, color="black"):
    """Draws a pixel on the canvas."""
    canvas.create_rectangle(x, y, x+1, y+1, outline=color, fill=color)

def transform_coords_to_center(x, y, canvas):
    """
    Transforms coordinates from the sistem where the center is in the top 
    left to the sistem where the center is center of the canvas.
    The center of the canvas becomes (0,0).
    """
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    new_x = x + width // 2
    new_y = -y + height // 2
    return new_x, new_y

def transform_coords_from_center(x, y, canvas):
    """
    Transforms coordinates from the system where the center of the canvas is (0,0)
    back to the system where the top-left corner is (0,0).
    """
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    new_x = x - width // 2
    new_y = -(y - height // 2)
    return new_x, new_y
