# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# abrir toplevel centigrados
def abrir_toplevel_centigrados():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("info de donde naci")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("500x500")
    toplevel_centigrados.config(bg="#7C9A99")

   # etiqueta para valor en centigrados
    lb_c = Label(toplevel_centigrados, text = "San Gil es un municipio colombiano ")   
    lb_c.config(bg="#7C9A99", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=60)

    lb_d = Label(toplevel_centigrados, text = "en el departamento de Santander")
    lb_d.config(bg="#7C9A99", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=90)

    lb_e = Label(toplevel_centigrados, text = "conocido oficialmente como la Capital Turística")
    lb_e.config(bg="#7C9A99", fg="black", font=("Helvetica", 18))
    lb_e.place(x=0, y=120)

    lb_d = Label(toplevel_centigrados, text = "de la región y la capital nacional de los deportes de aventura")
    lb_d.config(bg="#7C9A99", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=150)



#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("yo33")

# tamaño de la ventana
ventana_principal.geometry("500x1000")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="#7C9A99")

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="#7C9A99")
frame_entrada.place(x=0, y=0, width=500, height=200)

# boton para abrir Toplevel para nacimiento
bt_centigrados = Button(frame_entrada, text="nacimiento", command=abrir_toplevel_centigrados)
bt_centigrados.place(x=100, y=100)



# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()