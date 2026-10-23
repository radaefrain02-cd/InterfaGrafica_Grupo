import tkinter as tk
from tkinter import messagebox
import re

ventana = tk.Tk()
ventana.title("Formulario básico")
ventana.geometry("400x300")

titulo = tk.Label(ventana, text="Escribe tus datos", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

tk.Label(ventana, text="Nombre").pack()
e1 = tk.Entry(ventana)
e1.pack()

tk.Label(ventana, text="Edad").pack()
e2 = tk.Entry(ventana)
e2.pack()

tk.Label(ventana, text="Email").pack()
e3 = tk.Entry(ventana)
e3.pack()

def validar_datos():
    nombre = e1.get().strip()
    edad = e2.get().strip()
    email = e3.get().strip()

    # Validación de nombre
    if nombre == "":
        messagebox.showerror("Error", "El nombre no puede estar vacío.")
        return

    # Validación de edad numérica
    if not edad.isdigit():
        messagebox.showerror("Error", "La edad debe ser un número.")
        return

    # Validación de email con regex
    patron_email = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if not re.match(patron_email, email):
        messagebox.showerror("Error", "El email no es válido.")
        return

    # Si todo está correcto
    messagebox.showinfo(f"Datos válidos", f"Nombre: {nombre} Edad: {edad} Email: {email}")

tk.Button(ventana, text="Enviar", command=validar_datos).pack(pady=10)

ventana.mainloop()