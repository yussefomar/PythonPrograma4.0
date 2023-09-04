from tkinter import *
from tkinter import messagebox
def obtener_usuarios_claves():
    return { "Andres":"AndresJ",
            "Pablo":"PabloG",
            "Gustavo":"GustavoB" }
def validar(user, password):
    credenciales = obtener_usuarios_claves()
    
    if user in credenciales and credenciales.get(user) == password:
        messagebox.showinfo(message="Usuario y Clave Correctos")
    else:
        messagebox.showerror(message="Algunos de los datos ingresados es Incorrecto")
def ventana_login():
    raiz = Tk()
    raiz.title("Login Grupo Cátedra")
    raiz.resizable(False, False)
    
    raiz.geometry("300x130")
    raiz.config(bg = "blue")
    mi_frame = Frame()
    mi_frame.pack()
    mi_frame.config(bg = "blue", width = "300", height = "130" )
    Label(mi_frame, text = "Usuario Alumno: ").place(x = 10, y = 20)
    box_alumno = Entry(mi_frame)
    box_alumno.place(x = 130, y = 20)
    Label(mi_frame, text = "Clave: ").place(x = 10, y = 50)
    box_clave = Entry(mi_frame)
    box_clave.place(x = 130, y = 50)
    box_clave.config(show = "*")
    mi_frame.config(width = "300", height = "100" )
    boton_ingresar = Button(raiz, text = "Ingresar", \
    command = lambda:validar(box_alumno.get(), box_clave.get()))
    boton_ingresar.pack()
    raiz.mainloop
    
ventana_login()
