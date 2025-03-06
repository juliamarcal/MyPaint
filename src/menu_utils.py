import tkinter as tk
from tkinter import colorchooser

global_menu_functions = {} # Global dictionary for menu functions

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
    add_button_to_menu(menu, "Limpar canvas", lambda: canvas.delete("all"), "red")

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
            width=20,
            height=1,
            padx=5, 
            pady=5,
            command=btn["command"]
        )
        button.pack(padx=20, pady=10)

def add_button_to_menu(menu, text, command, color, return_button=False):
    """Creates a button and optionally returns the reference to the button."""
    button = tk.Button(
        menu, 
        text=text, 
        font=("Arial", 10),
        bg=color,
        fg="white",
        width=20,
        height=1,
        padx=5, 
        pady=5,
        command=command
    )
    button.pack(padx=20, pady=10)
    
    if return_button:
        return button

def add_dropdown_to_menu(menu, options, command):
    """
    Adds a dropdown (OptionMenu) to the menu without a label.

    Parameters:
    - menu: The Tkinter Frame where the dropdown will be added.
    - options: A list of options for the dropdown.
    - command: A function to call when an option is selected.
    """
    frame = tk.Frame(menu, bg="gray")
    frame.pack(pady=0)

    selected_option = tk.StringVar()
    selected_option.set(options[0])  # Default value

    # Pass the command directly without using lambda
    dropdown = tk.OptionMenu(frame, selected_option, *options, command=command)

    dropdown.config(
        font=("Arial", 10), 
        bg="#6495ED",
        fg="white",
        width=20,
        height=1,
        padx=5, 
        pady=5,    
        relief="raised",
        highlightthickness=0,
    )
    dropdown.pack(padx=20, pady=10)

    return selected_option

def add_text_to_menu(menu, text, color="white"):
    """
    Adds a text label to the menu.

    Parameters:
    - menu: The Tkinter Frame where the text will be added.
    - text: The text to display.
    - color: The text color (default: white).
    """
    label = tk.Label(menu, text=text, fg=color, bg=menu.cget("bg"), font=("Arial", 10, "bold"), wraplength=menu.winfo_width())
    label.pack(pady=5)
    return label

def choose_color():
    """Opens a color chooser and updates the selected color."""
    global selected_color
    color = colorchooser.askcolor(title="Escolha uma cor")[1]  # Open color picker
    if color:  # If a color was selected
        selected_color = color
        print(f"Selected color: {selected_color}")
    return selected_color  # Return the chosen color
