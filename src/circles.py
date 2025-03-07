import menu_utils
import canvas_utils
import tkinter as tk

class CircleDrawer:
    def __init__(self, menu, canvas):
        self.menu = menu
        self.canvas = canvas
        self.xc = self.yc = None
        self.radius = None
        self.selected_color = "black"
        self.color_button = None  

    def start_circle(self):
        """Initialize the circle drawing tool."""
        self.create_circle_menu()
        self.canvas.bind("<Button-1>", self.get_coordinates)

    def create_circle_menu(self):
        menu_utils.clear_menu(self.menu)
        menu_utils.add_text_to_menu(self.menu, "Para criar uma circunferência clique em dois pontos no canvas.\n\nO primeiro ponto será o centro e o segundo será a demarcação para o raio.")
        self.color_button = menu_utils.add_button_to_menu(self.menu, "cor", lambda: self.update_color(), "black", True)
        self.radius_slider = menu_utils.add_slider_to_menu(self.menu, "Raio", from_=5, to=200, command=self.update_radius,initial=50)
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
        print(f"Updated radius: {self.radius}")


    def set_selected_color(self, color):
        """Updates the selected color."""
        self.selected_color = color
        print(f"Updated selected color: {self.selected_color}")
        if self.color_button:
            self.color_button.config(bg=self.selected_color)

    def get_coordinates(self, event):
        self.xc, self.yc = event.x, event.y
        print(f"select center: ({self.xc}, {self.yc})")
        canvas_utils.draw_pixel(self.canvas, self.xc, self.yc, self.selected_color)
        self.bresenham_circle(self.xc, self.yc, self.radius)
        self.xc = self.yc = None 
                  

    def bresenham_circle(self, xc, yc, r):
        print("starting Bresenham circle")
        x = 0
        y = r
        p = 3 - 2 * r 
        
        while x < y:
            if (p<0): p += 4 * x + 6
            else:
                p += 4 * (x - y) + 10
                y -= 1
            x += 1
            self.plotSimetrics(x, y, xc, yc)
        
                
    def plotSimetrics(self, a, b, xc, yc):
        canvas_utils.draw_pixel(self.canvas, (xc + a), (yc + b), self.selected_color)
        canvas_utils.draw_pixel(self.canvas, (xc + a), (yc - b), self.selected_color)
        canvas_utils.draw_pixel(self.canvas, (xc - a), (yc + b), self.selected_color)
        canvas_utils.draw_pixel(self.canvas, (xc - a), (yc - b), self.selected_color)
        canvas_utils.draw_pixel(self.canvas, (xc + b), (yc + a), self.selected_color)
        canvas_utils.draw_pixel(self.canvas, (xc + b), (yc - a), self.selected_color)
        canvas_utils.draw_pixel(self.canvas, (xc - b), (yc + a), self.selected_color)
        canvas_utils.draw_pixel(self.canvas, (xc - b), (yc - a), self.selected_color)