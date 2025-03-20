import menu_utils
import canvas_utils
import tkinter as tk

class Line:
    """
    Represents a line with specified coordinates, color, and drawing method.
    """
    def __init__(self, x1, y1, x2, y2, color, method):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.method = method
    
    def __repr__(self):
        """
        Returns a string representation of the line.
        """
        return f"Line(x1={self.x1}, y1={self.y1}, x2={self.x2}, y2={self.y2})"

class LineDrawer:
    """
    Handles line drawing operations on a canvas.
    """
    def __init__(self, menu, canvas):
        """
        Initializes the LineDrawer with a menu and canvas.
        
        :param menu: The menu where options will be displayed.
        :param canvas: The drawing canvas.
        """
        self.menu = menu
        self.canvas = canvas
        self.selected_method = None
        self.x1 = self.y1 = self.x2 = self.y2 = None
        self.selected_color = "black"
        self.color_button = None
        self.lines = []

    def start_line(self):
        """
        Initializes the line drawing tool by setting up the menu and event bindings.
        """
        self.create_line_menu()
        self.canvas.bind("<Button-1>", self.get_coordinates)

    def create_line_menu(self):
        """
        Creates a menu for line drawing options, including method selection and color choice.
        """
        menu_utils.clear_menu(self.menu)
        menu_utils.add_text_to_menu(self.menu, "Para criar uma reta clique em dois pontos no canvas.")
        self.selected_method = menu_utils.add_dropdown_to_menu(self.menu, ["Bresenham", "DDA"], self.update_method)
        self.color_button = menu_utils.add_button_to_menu(self.menu, "cor", lambda: self.update_color(), "black", True)
        menu_utils.add_button_to_menu(self.menu, "Voltar", lambda: self.leave_lines(), "red")

    def leave_lines(self):
        """
        Resets the line settings and returns to the default menu.
        """
        self.selected_method.set("Bresenham")
        self.set_selected_color("black")
        menu_utils.draw_default_menu(self.menu, self.canvas)
        self.x1 = self.y1 = self.x2 = self.y2 = None

    # stored lines functions
    def get_stored_lines(self):
        """
        Returns the list of stored lines.
        """
        return self.lines
    
    def set_stored_lines(self, line_list):
        """
        Sets the stored lines from an external list.
        
        :param line_list: List of Line objects
        """
        if isinstance(line_list, list) and all(isinstance(line, Line) for line in line_list):
            self.lines = line_list
            for line in line_list:
                self.draw_line(line)
        else:
            raise ValueError("Invalid format for line_list. Expected a list of Line objects.")

    def reset(self):
        """
        Clears all stored lines.
        """
        self.lines = []

    # dinamic updates
    def update_method(self, value):
        """
        Updates the selected line drawing method.
        
        :param value: Selected method (Bresenham or DDA).
        """
        if self.selected_method:
            self.selected_method.set(value)
            print("Selected method for line:", self.selected_method.get())

    def update_color(self):
        """
        Opens a color selection dialog and updates the selected color.
        """
        color = menu_utils.choose_color()
        if color:
            self.set_selected_color(color)

    def set_selected_color(self, color):
        """
        Updates the selected drawing color.
        
        :param color: New color value.
        """
        self.selected_color = color
        print(f"Updated selected color for line: {self.selected_color}")
        if self.color_button:
            self.color_button.config(bg=self.selected_color)

    # line drawing
    def get_coordinates(self, event):
        """
        Handles user clicks to capture coordinates for drawing a line.
        
        :param event: Tkinter event containing click coordinates.
        """
        if self.x1 is None and self.y1 is None:  
            self.x1, self.y1 = event.x, event.y
            canvas_utils.draw_pixel(self.canvas, self.x1, self.y1, self.selected_color)
        else:
            self.x2, self.y2 = event.x, event.y
            canvas_utils.draw_pixel(self.canvas, self.x2, self.y2, self.selected_color)
        
            transformed_x1 = canvas_utils.transform_coords_to_center(self.x1, "x", self.canvas)
            transformed_y1 = canvas_utils.transform_coords_to_center(self.y1, "y", self.canvas)
            transformed_x2 = canvas_utils.transform_coords_to_center(self.x2, "x", self.canvas)
            transformed_y2 = canvas_utils.transform_coords_to_center(self.y2, "y", self.canvas)
    
            new_line = Line(transformed_x1, transformed_y1, transformed_x2, transformed_y2, self.selected_color, self.selected_method.get())
            self.draw_line(new_line)
            self.lines.append(new_line)
            self.x1 = self.y1 = self.x2 = self.y2 = None

    def draw_line(self, line):
        """
        Draws a stored line on the canvas.
        
        :param line: Line object containing coordinates and drawing method.
        """
        print(f"Drawing line: {line}")
        recovered_x1 = canvas_utils.transform_coords_from_center(line.x1, "x", self.canvas)
        recovered_y1 = canvas_utils.transform_coords_from_center(line.y1, "y", self.canvas)
        recovered_x2 = canvas_utils.transform_coords_from_center(line.x2, "x", self.canvas)
        recovered_y2 = canvas_utils.transform_coords_from_center(line.y2, "y", self.canvas)
        
        canvas_utils.draw_pixel(self.canvas, recovered_x1, recovered_y1, line.color)
        canvas_utils.draw_pixel(self.canvas, recovered_x2, recovered_y2, line.color)
        
        print(f"Starting line creation with methood: {line.method}")
        if line.method == "DDA":
            self.dda(recovered_x1, recovered_y1, recovered_x2, recovered_y2, line.color)
        else:
            self.bresenham(recovered_x1, recovered_y1, recovered_x2, recovered_y2, line.color)
    
    def dda(self, x1, y1, x2, y2, color):
        """
        Implements the DDA algorithm for drawing a line.
        """
        dx = x2 - x1
        dy = y2 - y1
        x, y = x1, y1

        passos = max(abs(dx), abs(dy))
        xincr = dx / passos
        yincr = dy / passos
        
        for _ in range(passos):
            x += xincr
            y += yincr
            canvas_utils.draw_pixel(self.canvas, round(x), round(y), color)

    def bresenham(self, x1, y1, x2, y2, color):
        """
        Implements the Bresenham algorithm for drawing a line.
        """        
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        xincr = 1 if x2 > x1 else -1
        yincr = 1 if y2 > y1 else -1

        canvas_utils.draw_pixel(self.canvas, x, y, color)

        if dx > dy:
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
                canvas_utils.draw_pixel(self.canvas, x, y, color)
        else:
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
                canvas_utils.draw_pixel(self.canvas, x, y, color)
