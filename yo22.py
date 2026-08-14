# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

    

# abrir imfo de donde naci
def abrir_toplevel_nacimi():
    global toplevel_naci
    toplevel_naci = Toplevel()
    toplevel_naci.title("info de donde naci")
    toplevel_naci.resizable(False, False)
    toplevel_naci.geometry("700x500")
    toplevel_naci.config(bg="#7C9A99")

# logo de la app
    lb_logo2 = Label(toplevel_naci, image=logo, bg="white")
    lb_logo2.place(x=0,y=200)


   # etiqueta de nacimiento
    lb_d = Label(toplevel_naci, text = "San Gil es un municipio colombiano ")   
    lb_d.config(bg="#7C9A99", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=60)
   
    lb_d = Label(toplevel_naci, text = "en el departamento de Santander")
    lb_d.config(bg="#7C9A99", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=90)
   
    lb_d = Label(toplevel_naci, text = "conocido oficialmente como la Capital Turística")
    lb_d.config(bg="#7C9A99", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=120)
   
    lb_d = Label(toplevel_naci, text = "de la región y la capital nacional de los deportes de aventura")
    lb_d.config(bg="#7C9A99", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=150)
   
    lb_d = Label(toplevel_naci, text = "naci el 16 de julio de 2011")
    lb_d.config(bg="#7C9A99", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=200)



   # abrir datos medi
def abrir_toplevel_medicos():
    global toplevel_medi
    toplevel_medi = Toplevel()
    toplevel_medi.title("datos medicos")
    toplevel_medi.resizable(False, False)
    toplevel_medi.geometry("700x500")
    toplevel_medi.config(bg="#99B7CB")

    # logo de la app
    lb_logo2 = Label(toplevel_medi, image=medi, bg="white")
    lb_logo2.place(x=0,y=200)

    # etiqueta para datos medicos
    lb_c = Label(toplevel_medi, text = "tube apendisites el año pasado")   
    lb_c.config(bg="#99B7CB", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=60)
    
    lb_d = Label(toplevel_medi, text = "me operaron y me toco quedarme en casa durante 2 meses")
    lb_d.config(bg="#99B7CB", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=90)
    
    lb_e = Label(toplevel_medi, text = "cuandom naci tube un desplasamienjto de cadera")
    lb_e.config(bg="#99B7CB", fg="black", font=("Helvetica", 18))
    lb_e.place(x=0, y=120)

    lb_d = Label(toplevel_medi, text = "pero ya estoy bien :)")
    lb_d.config(bg="#99B7CB", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=150)

    lb_d = Label(toplevel_medi, text = "soy tipo de sangre o+")
    lb_d.config(bg="#99B7CB", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=180)
   
  # abrir famili
def abrir_toplevel_familia():
    global toplevel_famili
    toplevel_famili = Toplevel()
    toplevel_famili.title("familia")
    toplevel_famili.resizable(False, False)
    toplevel_famili.geometry("700x750")
    toplevel_famili.config(bg="#73C9F1")

    # logo de la app
    lb_logo2 = Label(toplevel_famili, image=famili, bg="white")
    lb_logo2.place(x=0,y=400)

# etiqueta para valor en centigrados
    lb_c = Label(toplevel_famili, text = "tengo 1 hermano que se graduo del guanenta")   
    lb_c.config(bg="#73C9F1", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=40)
    
    lb_d = Label(toplevel_famili, text = "escojio la especialidad de electronica")
    lb_d.config(bg="#73C9F1", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=80)
    
    lb_e = Label(toplevel_famili, text = "esta estudiando en la uni de bucaramanga ingieneria electronica")
    lb_e.config(bg="#73C9F1", fg="black", font=("Helvetica", 18))
    lb_e.place(x=0, y=120)
    
    lb_d = Label(toplevel_famili, text = "esta en el trabajo de grado para graduarsde de la uni")
    lb_d.config(bg="#73C9F1", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=160) 

    lb_d = Label(toplevel_famili, text = "mi hermano ya tiene 24 años")
    lb_d.config(bg="#73C9F1", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=200)

    lb_d = Label(toplevel_famili, text = "mi mamá nos quiere mucho y trabaja en una tienda")
    lb_d.config(bg="#73C9F1", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=240)

    lb_d = Label(toplevel_famili, text = "mi papá nos quiere mucho a mi hermano y a mi")
    lb_d.config(bg="#73C9F1", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=280)

    lb_d = Label(toplevel_famili, text = "siempre dise que aprendamos ingles para conseguir ")
    lb_d.config(bg="#73C9F1", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=320)

    lb_d = Label(toplevel_famili, text = "un trabajo bonito por aprender ingles")
    lb_d.config(bg="#73C9F1", fg="black", font=("Helvetica", 18))
    lb_d.place(x=0, y=370)

# abrir edu
def abrir_toplevel_educativo():
    global toplevel_edu
    toplevel_edu = Toplevel()
    toplevel_edu.title("proseso educativo")
    toplevel_edu.resizable(False, False)
    toplevel_edu.geometry("720x500")
    toplevel_edu.config(bg="#ADCCB8")

# logo de la app
    lb_logo2 = Label(toplevel_edu, image=edu, bg="white")
    lb_logo2.place(x=0,y=200)


    # etiqueta para valor en centigrados
    lb_c = Label(toplevel_edu, text = "en la educasion me va muy bien porque llevo un buen promedio")   
    lb_c.config(bg="#ABCCB8", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=40)

    lb_c = Label(toplevel_edu, text = "y en la primaria nunca repeti ningun año")   
    lb_c.config(bg="#ABCCB8", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=80)

    lb_c = Label(toplevel_edu, text = "en el guanenta he perdido materias pero he logrado pasador el año")   
    lb_c.config(bg="#ABCCB8", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=120)

    lb_c = Label(toplevel_edu, text = "sin importar que alla perdido algunas materias pero las he recuperar")   
    lb_c.config(bg="#ABCCB8", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=160)

    # abrir ami
def abrir_toplevel_amigos():
    global toplevel_ami
    toplevel_ami = Toplevel()
    toplevel_ami.title("amigos")
    toplevel_ami.resizable(False, False)
    toplevel_ami.geometry("700x500")
    toplevel_ami.config(bg="#D3A896")

    # logo de la app
    lb_logo2 = Label(toplevel_ami, image=amigos, bg="white")
    lb_logo2.place(x=0,y=200)


    lb_c = Label(toplevel_ami, text = "tengo muchos amigos y tengo 2 que son mejores amigos")   
    lb_c.config(bg="#D3A896", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=40)

    lb_c = Label(toplevel_ami, text = "mis 2 mejores amigos se llaman yeiber y julian")   
    lb_c.config(bg="#D3A896", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=80)

    lb_c = Label(toplevel_ami, text = "yeiber es de 10-4 y julian es de 10-5")   
    lb_c.config(bg="#D3A896", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=120)

    lb_c = Label(toplevel_ami, text = "a yeiber lo conosco desde la guarderia")   
    lb_c.config(bg="#D3A896", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=160)

    lb_c = Label(toplevel_ami, text = "a julian lo conosco desde 4 de primaria")   
    lb_c.config(bg="#D3A896", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=200)

# abrir hobbies
def abrir_toplevel_hobbies():
    global toplevel_hobbi
    toplevel_hobbi = Toplevel()
    toplevel_hobbi.title("hobbies")
    toplevel_hobbi.resizable(False, False)
    toplevel_hobbi.geometry("700x500")
    toplevel_hobbi.config(bg="#CF9FB5")

    # logo de la app
    lb_logo2 = Label(toplevel_hobbi, image=hobbi, bg="white")
    lb_logo2.place(x=0,y=150)

    lb_c = Label(toplevel_hobbi, text = "mis hobbies son jugar videojuegos jugar futbol con mis amigos ")   
    lb_c.config(bg="#CF9FB5", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=20)

    lb_c = Label(toplevel_hobbi, text = "y juagr balonsesto con mis amigos y con mi hermmano")   
    lb_c.config(bg="#CF9FB5", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=60)

    lb_c = Label(toplevel_hobbi, text = "hacer ejercicio")   
    lb_c.config(bg="#CF9FB5", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=100)
    

    # abrir libres
def abrir_toplevel_horario():
    global toplevel_libres
    toplevel_libres = Toplevel()
    toplevel_libres.title("horario")
    toplevel_libres.resizable(False, False)
    toplevel_libres.geometry("700x500")
    toplevel_libres.config(bg="#8DA49B")

    # logo de la app
    lb_logo2 = Label(toplevel_libres, image=libre, bg="white")
    lb_logo2.place(x=0,y=150)

    lb_c = Label(toplevel_libres, text = "en mi orario de clase de lunes a viernes tengo clases 12:30 a 6:30")   
    lb_c.config(bg="#8DA49B", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=20)

    lb_c = Label(toplevel_libres, text = "el sabado tengo clase de ingles de 9:00 a 12:00")   
    lb_c.config(bg="#8DA49B", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=60)
 
    lb_c = Label(toplevel_libres, text = "el domingo no hago nada solo descansar y jugar videojuegos")   
    lb_c.config(bg="#8DA49B", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=100)

    # abrir 2026
def abrir_toplevel_pruevas():
    global toplevel_2026
    toplevel_2026 = Toplevel()
    toplevel_2026.title("pruebas")
    toplevel_2026.resizable(False, False)
    toplevel_2026.geometry("700x500")
    toplevel_2026.config(bg="#CBB843")

    # logo de la app
    lb_logo2 = Label(toplevel_2026, image=prueva, bg="white")
    lb_logo2.place(x=0,y=150)

    lb_c = Label(toplevel_2026, text = "estudiar para aprender para sacar muy buenas notas")   
    lb_c.config(bg="#CBB843", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=20)

    lb_c = Label(toplevel_2026, text = "y pasar el año para entrar a 11")   
    lb_c.config(bg="#CBB843", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=60)

    # abrir proyect
def abrir_toplevel_proyecto():
    global toplevel_proyect
    toplevel_proyect = Toplevel()
    toplevel_proyect.title("proyecto")
    toplevel_proyect.resizable(False, False)
    toplevel_proyect.geometry("700x500")
    toplevel_proyect.config(bg="#B5B898")

# logo de la app
    lb_logo2 = Label(toplevel_proyect, image=proyecto, bg="white")
    lb_logo2.place(x=0,y=150)

    lb_c = Label(toplevel_proyect, text = "para el 2031 yo pienso estar en la universidad")   
    lb_c.config(bg="#B5B898", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=20)

    lb_c = Label(toplevel_proyect, text = "estudiando ingieneria en sistemas")   
    lb_c.config(bg="#B5B898", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=60)

    lb_c = Label(toplevel_proyect, text = "")   
    lb_c.config(bg="#B5B898", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=60)


    # abrir hola
def abrir_toplevel_libre():
    global toplevel_hola
    toplevel_hola = Toplevel()
    toplevel_hola.title("libre")
    toplevel_hola.resizable(False, False)
    toplevel_hola.geometry("750x500")
    toplevel_hola.config(bg="#B27A76")

    # logo de la app
    lb_logo2 = Label(toplevel_hola, image=hola, bg="white")
    lb_logo2.place(x=0,y=150)


    lb_c = Label(toplevel_hola, text = "Al menos 224 personas han muerto y cientos han resultado")   
    lb_c.config(bg="#B27A76", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=20)

    lb_c = Label(toplevel_hola, text = "heridas en Colombia or el terremoto de magnitud 7,4 ")   
    lb_c.config(bg="#B27A76", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=60)

    lb_c = Label(toplevel_hola, text = "que sacudió el oeste del país el lunes egún las autoridades locales")   
    lb_c.config(bg="#B27A76", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=100)

    lb_c = Label(toplevel_hola, text = "Los bomberos avanzan en las labores de búsqueda y rescate de los")   
    lb_c.config(bg="#B27A76", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=100)

    lb_c = Label(toplevel_hola, text = "supervivientes")   
    lb_c.config(bg="#B27A76", fg="black", font=("Helvetica", 18))
    lb_c.place(x=0, y=100) 


#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("yo33")

# tamaño de la ventana
ventana_principal.geometry("900x900")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="#7C9A99")

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="#7C9A99")
frame_entrada.place(x=0, y=0, width=900, height=900)

# logo de la app
logo = PhotoImage(file="img/a.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=20,y=170)

# logo de la app
amigos = PhotoImage(file="img/amigos.png")
lb_amigos = Label(frame_entrada, image=amigos, bg="white")
lb_amigos.place(x=700,y=170)

# logo de la app
famili = PhotoImage(file="img/famili.png")
lb_famili = Label(frame_entrada, image=famili, bg="white")
lb_famili.place(x=380,y=170)

# logo de la app
edu = PhotoImage(file="img/edu.png")
lb_edu = Label(frame_entrada, image=edu, bg="white")
lb_edu.place(x=550,y=170)

# logo de la app
medi = PhotoImage(file="img/medi.png")
lb_medi = Label(frame_entrada, image=medi, bg="white")
lb_medi.place(x=190,y=170)

# logo de la app
libre = PhotoImage(file="img/libre.png")
lb_libre = Label(frame_entrada, image=libre, bg="white")
lb_libre.place(x=190,y=450)

# logo de la app
prueva = PhotoImage(file="img/prueva.png")
lb_prueva = Label(frame_entrada, image=prueva, bg="white")
lb_prueva.place(x=380,y=450)

# logo de la app
proyecto = PhotoImage(file="img/proyecto.png")
lb_proyecto = Label(frame_entrada, image=proyecto, bg="white")
lb_proyecto.place(x=550,y=450)

# logo de la app
hobbi = PhotoImage(file="img/hobbi.png")
lb_hobbi = Label(frame_entrada, image=hobbi, bg="white")
lb_hobbi.place(x=20,y=450)

# logo de la app
hola = PhotoImage(file="img/hola.png")
lb_hola = Label(frame_entrada, image=hola, bg="white")
lb_hola.place(x=700,y=450)

# boton para abrir Toplevel para nacimiento
bt_rty = Button(frame_entrada, text="nacimiento", command=abrir_toplevel_nacimi,)
bt_rty.place(x=20, y=154, width=115)

# boton para abrir Toplevel para datos medicos
bt_centigrados = Button(frame_entrada, text="datos medicos", command=abrir_toplevel_medicos)
bt_centigrados.place(x=190, y=154, width=115)

# boton para abrir Toplevel para familia
bt_centigrados = Button(frame_entrada, text="familia", command=abrir_toplevel_familia)
bt_centigrados.place(x=380, y=150, width=115)

# boton para abrir Toplevel para edu
bt_centigrados = Button(frame_entrada, text="edu", command=abrir_toplevel_educativo)
bt_centigrados.place(x=550, y=150, width=115)

# boton para abrir Toplevel para amigos
bt_centigrados = Button(frame_entrada, text="amigos", command=abrir_toplevel_amigos)
bt_centigrados.place(x=700, y=150, width=115)

# boton para abrir Toplevel para habbies
bt_centigrados = Button(frame_entrada, text="habbies", command=abrir_toplevel_hobbies)
bt_centigrados.place(x=20, y=450, width=115)

# boton para abrir Toplevel para horario
bt_centigrados = Button(frame_entrada, text="horario", command=abrir_toplevel_horario)
bt_centigrados.place(x=190, y=450, width=115)

# boton para abrir Toplevel para pruevas
bt_centigrados = Button(frame_entrada, text="pruevas", command=abrir_toplevel_pruevas)
bt_centigrados.place(x=380, y=450, width=115)

# boton para abrir Toplevel para proyecto
bt_centigrados = Button(frame_entrada, text="proyecto", command=abrir_toplevel_proyecto)
bt_centigrados.place(x=550, y=450, width=115)

# boton para abrir Toplevel para libre
bt_centigrados = Button(frame_entrada, text="libre", command=abrir_toplevel_libre)
bt_centigrados.place(x=700, y=450, width=115)

# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()