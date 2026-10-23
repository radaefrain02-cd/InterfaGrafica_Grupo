import tkinter as tk

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

tk.Button(ventana, text="Enviar", command=lambda: print(e1.get(), e2.get(), e3.get())).pack(pady=10)

ventana.mainloop()

"""agregar nombre edad y email

validacion que se valide lo de arriba

git pull origin main
y depues push origin"""