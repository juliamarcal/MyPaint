import tkinter as tk

def clear_menu(menu):
    """Remove todos os widgets do menu."""
    for widget in menu.winfo_children():
        widget.destroy()

def add_buttons_to_menu(menu, buttons_config):
    """
    Cria botões dinamicamente no menu.

    Args:
    - menu (tk.Frame): O menu onde os botões serão adicionados.
    - buttons_config (list): Lista de dicionários com as propriedades dos botões.
    """
    clear_menu(menu)

    for btn in buttons_config:
        button = tk.Button(
            menu, 
            text=btn["text"], 
            font=("Arial", 10),
            bg=btn.get("bg", "#6495ED"),
            fg=btn.get("fg", "white"),
            width=btn.get("width", 15),
            height=btn.get("height", 1),
            padx=5, 
            pady=5,
            command=btn["command"]
        )
        button.pack(padx=20, pady=10)

def draw_pixel(canvas, x, y, color="black"):
    """Desenha um pixel no canvas."""
    canvas.create_rectangle(x, y, x+1, y+1, outline=color, fill=color)