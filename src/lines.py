import menu_utils
import canvas_utils
import tkinter as tk

selected_method = None  # algorithm to be used to plot the line
x1, y1, x2, y2 = None, None, None, None  # Variables to store coordinates of clicks
selected_color = "black"  # Default color
color_button = None # colour button - changes color when a new one is selected

def start_line(menu, canvas):
    global x_coord, y_coord
    create_line_menu(menu, canvas)
    canvas.bind("<Button-1>", get_coordinates)

def create_line_menu(menu, canvas):
    global selected_method, color_button

    menu_utils.clear_menu(menu)
    menu_utils.add_text_to_menu(menu, "Para Criar uma reta clique em dois pontos no canvas. Será automaticamente plotada uma reta entre eles usando o algorítmo selecionado.")
    selected_method = menu_utils.add_dropdown_to_menu(menu, ["Bresenham", "DDA"], update_method)
    color_button = menu_utils.add_button_to_menu(menu, "cor", lambda: update_color(), "black", True)
    menu_utils.add_button_to_menu(menu, "Voltar", lambda: menu_utils.draw_default_menu(menu, canvas), "red")

def update_method(value):
    global selected_method
    if selected_method:
        selected_method.set(value)
        print("Selected method:", selected_method.get())

def update_color():
    color = menu_utils.choose_color()
    if color:
        set_selected_color(color)

def set_selected_color(color):
    """Updates the global selected color and button color."""
    global selected_color, color_button
    if color:
        selected_color = color
        print(f"Updated selected color: {selected_color}")
        if color_button:
            color_button.config(bg=selected_color)

def get_coordinates(event):
    global x1, y1, x2, y2, selected_method, selected_color
    if x1 is None and y1 is None:  
        x1, y1 = event.x, event.y
        print(f"select coord 1: ({x1}, {y1})")
        canvas_utils.draw_pixel(event.widget, x1, y1, selected_color)
    else:
        x2, y2 = event.x, event.y
        print(f"select coord 2: ({x2}, {y2})")
        canvas_utils.draw_pixel(event.widget, x2, y2, selected_color)
        if selected_method.get() == "DDA":
            dda(event.widget, x1, y1, x2, y2)
        else:
            bresenham(event.widget, x1, y1, x2, y2)
        x1 = y1 = x2 = y2 = None

def dda(canvas, x1, y1, x2, y2):
    print("starting DDA")
    global selected_color
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1

    if abs(dx) > abs(dy):
        passos = abs(dx)
    else:
        passos = abs(dy)
    
    xincr = dx / passos
    yincr = dy / passos
    
    for i in range(passos):
        x += xincr
        y += yincr
        canvas_utils.draw_pixel(canvas, abs(x), abs(y), selected_color)

def bresenham(canvas, x1, y1, x2, y2):
    print("starting Bresenham")
    global selected_color
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1

    xincr = 1 if x2 > x1 else -1
    yincr = 1 if y2 > y1 else -1

    canvas_utils.draw_pixel(canvas, x, y, selected_color)

    if dx > dy: # Case 1
        p = 2 * dy - dx
        c1 = 2 * dy
        c2 = 2 * (dy - dx)
        for _ in range(dx):
            x += xincr
            if p >= 0:
                y += yincr
                p += c2
            else:
                p += c1
            canvas_utils.draw_pixel(canvas, x, y, selected_color)
    else:  # Case 2
        p = 2 * dx - dy
        c1 = 2 * dx
        c2 = 2 * (dx - dy)
        for _ in range(dy):
            y += yincr
            if p >= 0:
                x += xincr
                p += c2
            else:
                p += c1
            canvas_utils.draw_pixel(canvas, x, y, selected_color)
