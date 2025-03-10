import tkinter as tk
from circles import CircleDrawer
import transformations
import clipping
import menu_utils
from lines import LineDrawer

# window config
root = tk.Tk()
root.title("Computação Gráfica - MyPaint")
root.geometry("800x600")

# create menu
menu_frame = tk.Frame(root, width=200, bg="gray")
menu_frame.pack(side="left", fill="y")

# create canvas
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

# Create dawers
line_drawer = LineDrawer(menu_frame, canvas)
circle_drawer = CircleDrawer(menu_frame, canvas)

# Dictionary of the main menu functions
menu_functions = {
    "Reta": line_drawer.start_line,
    "Circunferência": circle_drawer.start_circle,
    "Transformações": transformations.start_transformations,
    "Recorte": clipping.start_clipping
}
menu_utils.set_global_menu_functions(menu_functions)

# Initialize default menu
menu_utils.draw_default_menu(menu_frame, canvas)

root.mainloop()
