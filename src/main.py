import tkinter as tk
import lines
import circles
import transformations
import clipping
import menu_utils

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
    "Reta": lines.start_line,
    "Circunferência": circles.start_circle,
    "Transformações": transformations.start_transformations,
    "Recorte": clipping.start_clipping
}
menu_utils.set_global_menu_functions(menu_functions)

# Initialize default menu
menu_utils.draw_default_menu(menu_frame, canvas)

root.mainloop()
