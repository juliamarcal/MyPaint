import menu_utils
import canvas_utils
import tkinter as tk
from lines import Line

class Window:
    """
    Represents a clipping window defined by two corner points.
    """
    def __init__(self, x1, y1, x2, y2):
        """
        Initializes Window object.
        """
        self.x_min = min(x1, x2)
        self.y_min = min(y1, y2)
        self.x_max = max(x1, x2)
        self.y_max = max(y1, y2)

    def __repr__(self):
        """
        String representation of window.
        """
        return f"Window(x_min={self.x_min}, y_min={self.y_min}, x_max={self.x_max}, y_max={self.y_max})"

class Clipping:
    """
    Handles line clipping using Cohen-Sutherland and Liang-Barsky algorithms.
    """
    def __init__(self, line_drawer, circle_drawer, canvas, menu):
        """
        Initializes the Clipping class.
        """
        self.line_drawer = line_drawer
        self.circle_drawer = circle_drawer
        self.canvas = canvas
        self.menu = menu
        self.selected_method = None
        self.start_x = self.start_y = None
        self.rect_id = None

    def start_clipping(self):
        """
        Starts the clipping process by enabling user selection of the clipping window.
        """
        self.create_clipping_menu()
        self.selected_method = "Cohen-Sutherland"
        self.canvas.bind("<ButtonPress-1>", self.start_selection)
        self.canvas.bind("<B1-Motion>", self.update_selection)
        self.canvas.bind("<ButtonRelease-1>", self.end_selection)

    def create_clipping_menu(self):
        """
        Creates the menu options for the clipping tool.
        """
        menu_utils.clear_menu(self.menu)
        menu_utils.add_text_to_menu(self.menu, "Clique e arraste para selecionar a janela de recorte.")
        menu_utils.add_dropdown_to_menu(self.menu, ["Cohen-Sutherland", "Liang-Barsky"], lambda value: self.update_method(value))
        menu_utils.add_button_to_menu(self.menu, "Aplicar recorte", self.do_clipping)
        menu_utils.add_button_to_menu(self.menu, "Voltar", self.leave_clipping, "red")
    
    def leave_clipping(self):
        """
        Exits the clipping mode and restores the default menu.
        """
        if self.rect_id:
            self.canvas.delete(self.rect_id)
            self.rect_id = None

        if hasattr(self, 'window'):
            del self.window
        
        menu_utils.draw_default_menu(self.menu, self.canvas)

    # dinamic updated
    def update_method(self, value):
        """
        Updates the selected clipping algorithm.
        """
        self.selected_method = value
        print("Selected method:", self.selected_method)

    # selection functions
    def start_selection(self, event):
        """
        Starts the selection of the clipping window when the user clicks.
        """
        self.start_x, self.start_y = event.x, event.y
        if self.rect_id:  
            self.canvas.delete(self.rect_id)
        self.rect_id = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="red", dash=(2, 2))
    
    def update_selection(self, event):
        """
        Updates the dimensions of the selection rectangle while dragging.
        """
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, event.x, event.y)

    def end_selection(self, event):
        """
        Finalizes the selection of the clipping window and stores the values.
        """
        x1 = canvas_utils.transform_coords_to_center(self.start_x, "x", self.canvas)
        y1 = canvas_utils.transform_coords_to_center(self.start_y, "y", self.canvas)
        x2 = canvas_utils.transform_coords_to_center(event.x, "x", self.canvas)
        y2 = canvas_utils.transform_coords_to_center(event.y, "y", self.canvas)
        self.window = Window(x1, y1, x2, y2)
        print(f"Janela definida: {self.window}")
    
    # start clipping
    def do_clipping(self):
        """
        Applies the selected clipping algorithm to the stored lines.
        """
        if hasattr(self, 'window'):
            print(f"Apply clipping with window: {self.window}")
            lines = self.line_drawer.get_stored_lines()
            if (self.selected_method == "Cohen-Sutherland"):
                lines = self.cohen_sutherland(lines)
            else:
                lines = self.liang_barsky(lines)
            
            canvas_utils.clear_canvas(self.canvas)
            self.line_drawer.set_stored_lines(lines)
            self.circle_drawer.redraw_all_circles()
        else:
            print("No Window selected!")
            # add ERROR
    
    # Cohen-Sutherland
    def cohen_sutherland(self, lines):
        """
        Performs line clipping using the Cohen-Sutherland algorithm.
        """
        new_lines = []
        for line in lines:
            done = accept = False
            
            while not done:
                cod_a = self.get_code(line.x1, line.y1)
                cod_b = self.get_code(line.x2, line.y2)

                if cod_a == 0 and cod_b == 0:  # Linha completamente dentro
                    done = True
                    accept = True
                elif (cod_a & cod_b) != 0:  # Linha completamente fora
                    done = True
                else:  # Linha parcialmente dentro
                    if cod_a != 0:
                        cod = cod_a
                    else:
                        cod = cod_b

                    x_int = y_int = 0

                    if self.get_bit(0, cod) == 1:  # Esquerda
                        x_int = self.window.x_min
                        y_int = line.y1 + (line.y2 - line.y1) * (self.window.x_min - line.x1) / (line.x2 - line.x1)
                    elif self.get_bit(1, cod) == 1:  # Direita
                        x_int = self.window.x_max
                        y_int = line.y1 + (line.y2 - line.y1) * (self.window.x_max - line.x1) / (line.x2 - line.x1)
                    elif self.get_bit(2, cod) == 1:  # Baixo
                        y_int = self.window.y_min
                        x_int = line.x1 + (line.x2 - line.x1) * (self.window.y_min - line.y1) / (line.y2 - line.y1)
                    elif self.get_bit(3, cod) == 1:  # Cima
                        y_int = self.window.y_max
                        x_int = line.x1 + (line.x2 - line.x1) * (self.window.y_max - line.y1) / (line.y2 - line.y1)
                    
                    if cod == cod_a:
                        line.x1, line.y1 = round(x_int), round(y_int)
                    else:
                        line.x2, line.y2 = round(x_int), round(y_int)
            if accept:
                new_lines.append(line)
        return new_lines

    def get_code(self, xp, yp):
        """
        Computes the region code for a point using the Cohen-Sutherland algorithm.
        """
        cod = 0
        if (xp < self.window.x_min): cod = cod + 1 # left
        if (xp > self.window.x_max): cod = cod + 2 # right
        if (yp < self.window.y_min): cod = cod + 4 # down
        if (yp > self.window.y_max): cod = cod + 8 # up
        return cod
    
    def get_bit(self, pos, number):
        """
        Retrieves a specific bit from a number.
        """
        return (number >> pos) & 1
    
    # Liang-Barsky
    def liang_barsky(self, lines):
        """
        Performs line clipping using the Liang-Barsky algorithm.
        """
        new_lines = []

        def clip_test(p, q, u1, u2):
            """
            Helper function for Liang-Barsky to determine valid intersections.
            """
            result = True
            if p == 0 and q < 0:
                result = False
            elif p != 0:
                r = q / p
                if p < 0:
                    if r > u2:
                        result = False
                    elif r > u1:
                        u1 = r
                else:
                    if r < u1:
                        result = False
                    elif r < u2:
                        u2 = r
            return result, u1, u2

        for line in lines:
            u1, u2 = 0, 1  # Inicializando os valores

            dx = line.x2 - line.x1
            dy = line.y2 - line.y1

            # Testes de corte
            accept, u1, u2 = clip_test(-dx, line.x1 - self.window.x_min, u1, u2)
            if accept:
                accept, u1, u2 = clip_test(dx, self.window.x_max - line.x1, u1, u2)
                if accept:
                    accept, u1, u2 = clip_test(-dy, line.y1 - self.window.y_min, u1, u2)
                    if accept:
                        accept, u1, u2 = clip_test(dy, self.window.y_max - line.y1, u1, u2)
                        if (u2 < 1):
                            line.x2 = round(line.x1 + dx * u2)
                            line.y2 = round(line.y1 + dy * u2)
                        if (u1 > 0):
                            line.x1 = round(line.x1 + dx * u1)
                            line.y1 = round(line.y1 + dy * u1)
                        new_lines.append(line)
        return new_lines
            