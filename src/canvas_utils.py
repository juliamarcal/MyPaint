import tkinter as tk

def draw_pixel(canvas, x, y, color="black"):
    """Draws a pixel on the canvas."""
    canvas.create_rectangle(x, y, x+1, y+1, outline=color, fill=color)

def transform_coords_to_center(coord, type, canvas):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    return coord - (width // 2) if type == "x" else (height // 2) - coord

def transform_coords_from_center(coord, type, canvas):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    return coord + (width // 2) if type == "x" else (height // 2) - coord

def clear_canvas(canvas):
    canvas.delete("all")