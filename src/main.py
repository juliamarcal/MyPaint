import tkinter as tk
import lines
import circles
import transformations
import clipping

# Configuração da janela
root = tk.Tk()
root.title("Computação Gráfica - MyPaint")
root.geometry("800x600")

# Cores
WHITE = "#FFFFFF"
GRAY = "#D3D3D3"
BLUE = "#6495ED"
DARK_BLUE = "#4682B4"

# menu
menu_frame = tk.Frame(root, width=200, bg=GRAY)
menu_frame.pack(side="left", fill="y")

# canvas
canvas = tk.Canvas(root, bg=WHITE)
canvas.pack(fill="both", expand=True)

# Lista de botões
menu_options = ["Reta", "Circunferência", "Transformações", "Recorte"]
selected_option = tk.StringVar(value="")

menu_functions = {
    "Reta": lines.draw_line,
    "Circunferência": circles.draw_circle,
    "Transformações": transformations.apply_transformations,
    "Recorte": clipping.apply_clipping
}

def on_button_click(option):
    selected_option.set(option)
    canvas.delete("all")
    menu_functions[option](canvas, menu_frame)
    print(f"Opção selecionada: {option}")


# Criando os botões no menu
for option in menu_options:
    button = tk.Button(menu_frame, text=option, font=("Arial", 10),
                       bg=BLUE, fg="white", width=15, height=1,
                       padx=5, pady=5,
                       command=lambda opt=option: on_button_click(opt))
    button.pack(padx=20, pady=10)

root.mainloop()