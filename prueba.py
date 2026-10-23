import tkinter as tk

def crear_ventan():
    ventana = tk.Tk()
    ventana.title("Mi primera ventana")
    ventana.geometry("500x300")

    boton = tk.Button(ventana, text="Hola mundo")
    boton.pack(pady=20)

    ventana.mainloop()
crear_ventan()