import tkinter as tk

# Global dictionary for menu functions
global_menu_functions = {}
def set_global_menu_functions(menu_functions):
    """Sets the global menu functions dictionary."""
    global global_menu_functions
    global_menu_functions = menu_functions

def draw_default_menu(menu, canvas):
    """
    Creates the default menu dynamically using global_menu_functions.
    """
    buttons = [
        {
            "text": option, 
            "command": lambda opt=option: global_menu_functions[opt](menu, canvas),
            "color": "#6495ED"
        }
        for option in global_menu_functions
    ]
    clear_menu(menu)
    add_buttons_to_menu(menu, buttons)

def clear_menu(menu):
    """Removes all widgets from menu."""
    for widget in menu.winfo_children():
        widget.destroy()

def add_buttons_to_menu(menu, buttons_config):
    """Creates buttons dynamically in the menu."""
    for btn in buttons_config:
        button = tk.Button(
            menu, 
            text=btn["text"], 
            font=("Arial", 10),
            bg=btn["color"],
            fg=btn.get("fg", "white"),
            width=btn.get("width", 20),
            height=btn.get("height", 1),
            padx=5, 
            pady=5,
            command=btn["command"]
        )
        button.pack(padx=20, pady=10)

def draw_pixel(canvas, x, y, color="black"):
    """Draws a pixel on the canvas."""
    canvas.create_rectangle(x, y, x+1, y+1, outline=color, fill=color)
