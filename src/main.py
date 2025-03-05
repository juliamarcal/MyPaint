import tkinter as tk
import lines
import circles
import transformations
import clipping
import utils

# window config
root = tk.Tk()
root.title("Computação Gráfica - MyPaint")
root.geometry("800x600")

# menu
menu_frame = tk.Frame(root, width=200, bg="gray")
menu_frame.pack(side="left", fill="y")

# canvas
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

# Dictionary of the main menu functions
menu_functions = {
    "Reta": lines.draw_line,
    "Circunferência": circles.draw_circle,
    "Transformações": transformations.apply_transformations,
    "Recorte": clipping.apply_clipping
}
utils.set_global_menu_functions(menu_functions)

# Initialize default menu
utils.draw_default_menu(menu_frame, canvas)

root.mainloop()
