import tkinter as tk
from tkinter import colorchooser

# Global dictionary to store menu functions
global_menu_functions = {}

def set_global_menu_functions(menu_functions):
    """
    Sets the global dictionary of menu functions.
    """
    global global_menu_functions
    global_menu_functions = menu_functions

def draw_default_menu(menu, canvas):
    """
    Creates the default menu dynamically using global_menu_functions.
    
    :Parameters:
    - menu (tk.Frame): The Tkinter frame where menu buttons will be placed.
    - canvas (tk.Canvas): The canvas where drawing operations occur (not used in this function but can be extended).
    """
    buttons = [
        {
            "text": option, 
            "command": lambda opt=option: global_menu_functions[opt](),
            "color": "#6495ED"
        }
        for option in global_menu_functions if option != "Clear"
    ]
    clear_menu(menu)
    add_buttons_to_menu(menu, buttons)
    add_button_to_menu(menu, "Limpar canvas", global_menu_functions["Clear"], "red")

def clear_menu(menu):
    """
    Removes all widgets from the given menu.
    
    :Parameters:
    - menu (tk.Frame): The menu frame to be cleared.
    """
    for widget in menu.winfo_children():
        widget.destroy()

def add_buttons_to_menu(menu, buttons_config):
    """
    Creates buttons dynamically in the menu based on a given configuration.
    
    :Parameters:
    - menu (tk.Frame): The menu frame where buttons will be added.
    - buttons_config (list of dict): List of button configurations with keys "text", "command", and optional "color".
    """
    default_color="#6495ED"
    for btn in buttons_config:
        button = tk.Button(
            menu, 
            text=btn["text"], 
            font=("Arial", 10),
            bg=btn.get("color", default_color),
            fg=btn.get("fg", "white"),
            width=25,
            height=1,
            padx=5, 
            pady=5,
            command=btn["command"]
        )
        button.pack(padx=20, pady=10)

def add_button_to_menu(menu, text, command, color="#6495ED", return_button=False):
    """
    Creates a button in the menu and optionally returns it.
    
    :Parameters:
    - menu (tk.Frame): The menu frame where the button will be added.
    - text (str): The button label.
    - command (callable): The function to execute when the button is clicked.
    - color (str, optional): The background color of the button. Default is "#6495ED".
    - return_button (bool, optional): Whether to return the button instance. Default is False.
    
    :Returns:
    - tk.Button (optional): The created button instance if return_button is True.
    """
    button = tk.Button(
        menu, 
        text=text, 
        font=("Arial", 10),
        bg=color,
        fg="white",
        width=25,
        height=1,
        padx=5, 
        pady=5,
        command=command
    )
    button.pack(padx=20, pady=10)
    
    if return_button:
        return button

def add_dropdown_to_menu(menu, options, command, defaut_value=""):
    """
    Adds a dropdown (OptionMenu) to the menu without a label.
    
    :Parameters:
    - menu (tk.Frame): The menu frame where the dropdown will be added.
    - options (list): List of options for the dropdown.
    - command (callable): The function to call when an option is selected.
    - default_value (str, optional): The initially selected value. Defaults to the first option.
    
    :Returns:
    - tk.StringVar: The variable holding the selected option.
    """
    frame = tk.Frame(menu, bg="gray")
    frame.pack(pady=0)

    selected_option = tk.StringVar()
    if (defaut_value == ""):
        selected_option.set(options[0])
    else:
        selected_option.set(defaut_value)

    dropdown = tk.OptionMenu(frame, selected_option, *options, command=command)

    dropdown.config(
        font=("Arial", 10), 
        bg="#6495ED",
        fg="white",
        width=25,
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
    
    :Parameters:
    - menu (tk.Frame): The menu frame where the text will be added.
    - text (str): The text to display.
    - color (str, optional): The text color. Default is "white".
    
    :Returns:
    - tk.Label: The created label instance.
    """
    label = tk.Label(menu, text=text, fg=color, bg=menu.cget("bg"), font=("Arial", 10, "bold"), wraplength=200)
    label.pack(pady=5)
    return label

def add_slider_to_menu(menu, label, from_, to, command, initial=10):
    """
    Adds a slider (Scale) to the menu.
    
    :Parameters:
    - menu (tk.Frame): The menu frame where the slider will be added.
    - label (str): The text label for the slider.
    - from_ (int): The minimum value of the slider.
    - to (int): The maximum value of the slider.
    - command (callable): The function to call when the slider value changes.
    - initial (int, optional): The initial value of the slider. Default is 10.
    
    :Returns:
    - tk.Scale: The created slider instance.
    """
    frame = tk.Frame(menu, bg=menu.cget("bg"))
    frame.pack(pady=5)

    # Label
    label_widget = tk.Label(frame, text=label, fg="white", bg=menu.cget("bg"), font=("Arial", 10, "bold"))
    label_widget.pack()

    # Slider (Scale widget)
    slider = tk.Scale(
        frame, 
        from_=from_, 
        to=to, 
        orient="horizontal", 
        length=200,
        resolution=1,
        command=command,
        bg="gray",
        fg="white",
        highlightthickness=0
    )
    slider.set(initial)
    slider.pack()

    return slider

def choose_color():
    """
    Opens a color chooser dialog and updates the selected color.
    
    :Returns:
    - str: The selected color in hex format (e.g., "#FF0000").
    """
    global selected_color
    color = colorchooser.askcolor(title="Escolha uma cor")[1]  # Open color picker
    if color:
        selected_color = color
        print(f"Selected color: {selected_color}")
    return selected_color
