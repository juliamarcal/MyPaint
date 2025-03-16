import menu_utils
import canvas_utils
import tkinter as tk

class Circle:
    def __init__(self, xc, yc, radius, color):
        self.xc = xc
        self.yc = yc
        self.radius = radius
        self.color = color

class CircleDrawer:
    def __init__(self, menu, canvas):
        self.menu = menu
        self.canvas = canvas
        self.xc = self.yc = None
        self.radius = None
        self.selected_color = "black"
        self.color_button = None
        self.circles = [] 

    def start_circle(self):
        """Initialize the circle drawing tool."""
        self.create_circle_menu()
        self.canvas.bind("<Button-1>", self.get_coordinates)

    def get_stored_circles(self):
        """Return stored circles"""
        return self.circles

    def set_stored_circles(self, circles_list):
        """
        Sets the stored circles from an external list.
        
        :param circles_list: List of Circle objects
        """
        if isinstance(circles_list, list) and all(isinstance(line, Circle) for line in circles_list):
            self.circles = circles_list
            for circle in circles_list:
                self.draw_circle(circle)
        else:
            raise ValueError("Invalid format for circle_list. Expected a list of Circle objects.")

    def redraw_all_circles(self):
        for circle in self.circles:
                self.draw_circle(circle)

    def create_circle_menu(self):
        menu_utils.clear_menu(self.menu)
        menu_utils.add_text_to_menu(self.menu, "Para criar uma circunferência clique em dois pontos no canvas.\n\nO primeiro ponto será o centro e o segundo será a demarcação para o raio.")
        self.color_button = menu_utils.add_button_to_menu(self.menu, "cor", lambda: self.update_color(), "black", True)
        menu_utils.add_slider_to_menu(self.menu, "Raio", from_=1, to=200, command=self.update_radius,initial=100)
        menu_utils.add_button_to_menu(self.menu, "Voltar", lambda: self.leave_circles(), "red")

    def leave_circles(self):
        self.update_radius(50)
        self.set_selected_color("black")
        menu_utils.draw_default_menu(self.menu, self.canvas)

    def update_color(self):
        color = menu_utils.choose_color()
        if color:
            self.set_selected_color(color)

    def update_radius(self, value):
        """Updates the radius from the slider."""
        self.radius = int(value)

    def set_selected_color(self, color):
        """Updates the selected color."""
        self.selected_color = color
        print(f"Updated selected color: {self.selected_color}")
        if self.color_button:
            self.color_button.config(bg=self.selected_color)

    def get_coordinates(self, event):
        self.xc, self.yc = event.x, event.y
        print(f"Clicked at:  ({self.xc}, {self.yc})")
        
        transformed_x = canvas_utils.transform_coords_to_center(self.xc, "x", self.canvas)
        transformed_y = canvas_utils.transform_coords_to_center(self.yc, "y", self.canvas)
        print(f"Transformed to: ({transformed_x}, {transformed_y})")

        canvas_utils.draw_pixel(self.canvas, self.xc, self.yc, self.selected_color)
        new_circle = Circle(transformed_x, transformed_y, self.radius, self.selected_color)
        self.draw_circle(new_circle)
        self.circles.append(new_circle)
        self.xc = self.yc = None 
                  
    def draw_circle(self, circle):
        recovered_x = canvas_utils.transform_coords_from_center(circle.xc, "x", self.canvas)
        recovered_y = canvas_utils.transform_coords_from_center(circle.yc, "y", self.canvas)
        print(f"circle -> x = {circle.xc}, y = {circle.yc}")
        print(f"circle recovered -> x = {recovered_x}, y = {recovered_y}")
        canvas_utils.draw_pixel(self.canvas, recovered_x, recovered_y)
        self.bresenham_circle(recovered_x, recovered_y, circle.radius, circle.color)

    def bresenham_circle(self, xc, yc, r, color):
        print("starting Bresenham circle")
        x = 0
        y = r
        p = 3 - 2 * r 
        
        while x <= y:
            if (p<0): p += 4 * x + 6
            else:
                p += 4 * (x - y) + 10
                y -= 1
            x += 1
            self.plotSimetrics(x, y, xc, yc, color)
                 
    def plotSimetrics(self, a, b, xc, yc, color):
        canvas_utils.draw_pixel(self.canvas, (xc + a), (yc + b), color)
        canvas_utils.draw_pixel(self.canvas, (xc + a), (yc - b), color)
        canvas_utils.draw_pixel(self.canvas, (xc - a), (yc + b), color)
        canvas_utils.draw_pixel(self.canvas, (xc - a), (yc - b), color)
        canvas_utils.draw_pixel(self.canvas, (xc + b), (yc + a), color)
        canvas_utils.draw_pixel(self.canvas, (xc + b), (yc - a), color)
        canvas_utils.draw_pixel(self.canvas, (xc - b), (yc + a), color)
        canvas_utils.draw_pixel(self.canvas, (xc - b), (yc - a), color)