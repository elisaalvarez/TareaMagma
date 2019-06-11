#AGENDA TELEFÓNICA
#Elisa Alvarez
from tkinter import * #Importar el paquete para hacer la interfaz
from tkinter import simpledialog, messagebox
#Definición de los métodos
def Add (): #Método ue añade contactos a la agenda
    global idc, agenda
    if not((nomt.get() and telt.get())==""):
        agenda.append([str(idc),nomt.get(),telt.get()])
        messagebox.showinfo("Agregado","El contacto ha sido agregado en la agenda")
        nomt.delete(0,END)
        telt.delete(0,END)
        idc+=1
        Mostrar()
    else:
        messagebox.showerror("Error","Uno o ambos campos están vacíos\nPor favor llene los datos correspondientes al nombre y teléfono")
def Busqueda(bus): #Método que regresa la posición de los datos de la búsqueda por ID
    global agenda
    index=-1
    encuentra=False
    for i in range (len(agenda)):
        elem=agenda[i]
        if elem[0]==bus:
            index=i
            encuentra=True
    if (not encuentra):
        messagebox.showerror("Error","El ID no se encuentra en la lista")
    return index
def Buscar (): #Método que muestra los datos del contacto
    global v, agenda
    if NoEmpty():
        idget=simpledialog.askstring("Buscar", "Ingrese el ID:",parent=v)
        if idget is not None:
            pos=Busqueda(idget)
            if not(pos==-1):
                messagebox.showinfo("Contacto","Nombre: %s\nTeléfono: %s"%(agenda[pos][1],agenda[pos][2]))
def Modificar():#Método que modifica datos del contacto
    global v,agenda
    if NoEmpty():
        idget=simpledialog.askstring("Modificar", "Ingrese el ID:",parent=v)
        if idget is not None:
            pos=Busqueda(idget)
            if not(pos==-1):
                nnom=simpledialog.askstring("Nombre","Ingrese el nuevo nombre:\n(Deje en blanco para no modificar)",parent=v)
                ntel=simpledialog.askstring("Teléfono","Ingrese el nuevo teléfono:\n(Deje en blanco para no modificar)",parent=v)
                if not(nnom=="") and not(ntel=="") and (nnom and ntel is not None):
                    agenda[pos][1]=nnom
                    agenda[pos][2]=ntel
                    messagebox.showinfo("Contacto modificado","El nombre y teléfono del contacto han sido modificados")
                    Mostrar()
                elif not(nnom=="") and (nnom is not None):
                    agenda[pos][1]=nnom
                    messagebox.showinfo("Contacto modificado","El nombre del contacto ha sido modificado")
                    Mostrar()
                elif not(ntel=="") and (ntel is not None):
                    agenda[pos][2]=ntel
                    messagebox.showinfo("Contacto modificado","El teléfono del contacto ha sido modificado")
                    Mostrar()
                elif (nnom and ntel is not None):
                    messagebox.showwarning("Aviso","El contacto no fue modificado\nNo se han ingresado datos para modificar")
def Eliminar(): #Método que elimina un contacto de la agenda y recorre la numeración de los ID
    global v,agenda,idc
    if NoEmpty():
        idget=simpledialog.askstring("Eliminar","Ingrese el ID:",parent=v)
        if idget is not None:
            pos=Busqueda(idget)
            if not(pos==-1):
                yesno=messagebox.askyesno("Aviso","Confirme la eliminación del contacto "+agenda[pos][1])
                if yesno:
                    agenda.pop(pos)
                    messagebox.showinfo("Contacto eliminado","El contacto fue eliminado correctamente")
                    Mostrar()
                else:
                    messagebox.showwarning("Aviso","Operación cancelada")
def Mostrar(): #Método que muestra los contactos en un campo de texto
    global agenda
    if NoEmpty():
        showt.configure(state="normal")
        showt.delete(1.0,END)
        for x in range (len(agenda)):
            elem=agenda[x]
            for y in range (len(elem)):
                showt.insert(END,elem[y])
                showt.insert(END," | ")
            showt.insert(END,"\n")
        showt.configure(state="disabled")
    else:
        showt.configure(state="normal")
        showt.delete(1.0,END)
def NoEmpty(): #Método que comprueba si hay elementos o no en la agenda
    if len(agenda)>0:
        return True
    else:
        messagebox.showerror("Error","La agenda está vacía")
    return False
v=Tk() #Crea un objeto de Tk()
v.geometry("250x400") #Define el tamaño de la ventana
v.configure(bg="alice blue") #Define el color de fondo de la ventana
v.title("☎ AGENDA ☎") #Define el título de la ventana
v.resizable(width=False,height=False)#Impide que se pueda ajustar manualmente
agenda=[] #Lista donde guardar los datos nombre y teléfono
idc=1 #Contador para los id
#Definición de las etiquetas
noml=Label(v,text="Nombre:")
noml.configure(bg="alice blue")
noml.grid(row=1,column=0,sticky=W)
tell=Label(v,text="Teléfono:")
tell.configure(bg="alice blue")
tell.grid(row=2,column=0,sticky=W)
showtl=Label(v,text="ID  Nombre  Teléfono")
showtl.configure(bg="alice blue")
showtl.grid(row=4,column=0,columnspan=3,sticky=W,padx=5)
#Definición de los campos de texto
nomt=Entry(v)
nomt.grid(row=1,column=1,sticky=W)
telt=Entry(v)
telt.grid(row=2,column=1,sticky=W)
showt=Text(v,width="7",height="10")
showt.grid(row=5,column=0, padx=5, pady=5,columnspan=3,rowspan=10,sticky=W+E+S+N)
#Definición de la barra de desplazamiento para el campo de texto donde se muestran los datos
sb=Scrollbar(v)
sb.grid(row=5,column=2,sticky=N+E+S,padx=5,pady=5,rowspan=10)
showt.configure(state="disabled",yscrollcommand=sb.set)
sb.configure(command=showt.yview)
#Definición de los botones necesarios
add=Button(v,text="Añadir", command=Add)
add.configure(bg="honeydew3",width="7",height="1")
add.grid(row=0,column=2, padx=5)
read=Button(v,text="Buscar", command=Buscar)
read.configure(bg="azure3",width="7",height="1")
read.grid(row=1,column=2, padx=5)
update=Button(v,text="Modificar", command=Modificar)
update.configure(bg="LavenderBlush3",width="7",height="1")
update.grid(row=2,column=2, padx=5)
delete=Button(v,text="Eliminar",command=Eliminar)
delete.configure(bg="MistyRose3",width="7",height="1")
delete.grid(row=3,column=2, padx=5)
v.mainloop() #Evita que se cierre la ventana al iniciar la ejecución desde consola


