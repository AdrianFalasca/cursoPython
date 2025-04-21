from tkinter import StringVar, Frame, Entry, Text, Toplevel
from tkinter import ttk, Label, Menu, Button, Scrollbar
from tkinter.ttk import Combobox
from tkinter.constants import CENTER
from modelo import Crud
from observador import Observador_1


class ventana:
    """
    Clase que instancia las clases Crud y Observador.
    Le pasa la instancia de Crud al observador. 
    Contiene los métodos que llaman a los métodos de la instancia Crud, 
    y las propiedades para la ventana, los frame,
    los campos, el menu, los label, el combobox,  los botones y el treeview.

    """
    def __init__(self, vent):
        """
        Contructor que instancia las clases Crud y Observador_1
        """        
        self.obj_crud = Crud()
        self.el_observador = Observador_1(self.obj_crud)
        
        
        #-------Ventana-------------
        self.root = vent
        self.root.title("Lógica proposicional")
        self.root.geometry("800x600")
        self.root.config(bg="black", pady=1, padx=1)
      

        #------------Frame-------------------
        self.frame_1 = Frame(self.root)
        self.frame_1.pack(pady=1)

        self.frame = Frame(self.root)
        self.frame.pack()

        self.framee = Frame(self.root, background="black")
        self.framee.pack(pady=1)

        self.frame_2 = Frame(self.root)
        self.frame_2.pack(pady=5)       


        #-----------Campos----------------
        
        self.id = StringVar()
        self.conector = StringVar()
         

        self.conector_entry = Entry(self.frame, 
                                    textvariable=self.conector)
        self.conector_entry.grid(row=3, column=1, padx=10, pady=10)
        self.conector_entry.focus()

        self.opciones = ["↔", "→", "∧", "¬", "∨", "⊻", "⊤", "⊥" ]
        self.simbolo = Combobox(self.frame, 
                                values=self.opciones, 
                                state="readonly", 
                                width="5")
        self.simbolo.grid(row=4, column=1, padx=10, pady=10)
    

        self.informacion_text = Text(self.frame, width=16, height=5)
        self.informacion_text.grid(row=5, column=1, padx=10, pady=10)

        self.scroll = Scrollbar(self.frame,
                                command=self.informacion_text.yview)
        self.scroll.grid(row=5, column=2, sticky="nsew")

        self.informacion_text.config(yscrollcommand=self.scroll.set)

 
        #---------------Menú------------------
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu, width=300, height=300)

        self.menu_conectar = Menu(self.menu, tearoff=0)
        self.menu_conectar.add_command(label="Visualizar",
                                       command=self.conectar_v)

        self.menu_borrar = Menu(self.menu, tearoff=0)
        self.menu_borrar.add_command(label="Borrar",
                                     command=self.borrar_v)

        self.menu_salir = Menu(self.menu, tearoff=0)
        self.menu_salir.add_command(label="Salir",
                                    command=self.salir_v)

        self.menu.add_cascade(label="Visualizar campos",
                              menu=self.menu_conectar)
        self.menu.add_cascade(label="Borrar campos",
                              menu=self.menu_borrar)
        self.menu.add_cascade(label="Salir de la aplicación",
                              menu=self.menu_salir)


        #--------------------Label-------------------
        self.label = Label(self.frame_1, text="Ingrese la información",
                           fg="white", font="24", width=30, bg="black")
        self.label.grid()  
                          

        self.conector_label = Label(self.frame, text="Conector lógico:")
        self.conector_label.grid(row=3, column=0,
                                 sticky="e", padx=10, pady=10)

        self.simbolo_label = Label(self.frame, text="Símbolo:")
        self.simbolo_label.grid(row=4, column=0,
                                sticky="e", padx=10, pady=10)

        self.informacion_label = Label(self.frame, text="Información:")
        self.informacion_label.grid(row=5, column=0,
                                    sticky="e", padx=10, pady=10)


        #---------------Botones----------------------
        self.boton_crear = Button(self.framee,
                                  text="Alta",
                                  background="gold", 
                                  command=self.crear_v)
        self.boton_crear.grid(row=6, column=0, 
                              sticky="e", padx=10, pady=10)

        self.boton_consultar = Button(self.framee,
                                      text="Consultar id",
                                      background="gold", 
                                      command=self.consultar_v
                                      )
        self.boton_consultar.grid(row=6, column=1,
                                  sticky="e", padx=10, pady=10)

        self.boton_modificar = Button(self.framee, 
                                      text="Modificar",
                                      background="gold", 
                                      command=self.modificar_v)
        self.boton_modificar.grid(row=6, column=2,
                                  sticky="e", padx=10, pady=10)

        self.boton_eliminar = Button(self.framee,
                                     text="Baja",
                                     background="gold", 
                                     command=self.eliminar_v)
        self.boton_eliminar.grid(row=6, column=3,
                                 sticky="e", padx=10, pady=10)
                                 
       
        #-----------Muestra toda los registros de la tabla----------
        self.tree = ttk.Treeview(self.frame_2)
        self.tree["columns"] = ("tree_1", "tree_2", "tree_3", "tree_4")
        self.tree.column("tree_1", width=120, minwidth=120, anchor=CENTER)
        self.tree.column("#0", width=40, minwidth=40)
        self.tree.column("tree_2", width=120, minwidth=120)
        self.tree.column("tree_3", width=70, minwidth=70, anchor=CENTER)
        self.tree.column("tree_4", width=300, minwidth=300)

        self.tree.heading("#0", text="Id")
        self.tree.heading("#1", text=" Fecha de alta")
        self.tree.heading("#2", text="Conector lógico")
        self.tree.heading("#3", text="Símbolo")
        self.tree.heading("#4", text="Información")
        
        self.tree.grid(column=0, row=10, columnspan=8)
        
    
    #Métodos que llaman a los métodos de la clase Crud      
    def conectar_v(self):
        """
        Método llamado con el menu y que llama a un método de
        la instancia de la clase Crud
        """
        
        self.obj_crud.mostrar(self.tree)
        

    def borrar_v(self):
        """
        Método llamado con el menu y que llama a un método de
        la instancia de la clase Crud
        """

        self.obj_crud.borrar_campos(self.informacion_text,
                                    self.simbolo,
                                    self.conector,
                                    self.id)

    def salir_v(self):
        """
        Método llamado con el menu y que llama a un método de
        la instancia de las clase Crud
        """
        self.obj_crud.salir(self.root)    

    def crear_v(self):
        """
        Método llamado con un botón y que llama a dos métodos de
        la instancia de la clase Crud
        """
        self.obj_crud.alta(self.conector,
                            self.simbolo, 
                            self.informacion_text,
                            self.id)
        self.obj_crud.mostrar(self.tree)

    def consultar_v(self):
        """
        Método llamado con un botón y que abre un toplevel y 
        con un botón llama a un método de la instancia de la clase Crud.
        """
        top = Toplevel(height="1500", width="500")
        top.grab_set()
        top.focus_set()
       
        id_label = Label(top, text="Introduzca el id:")
        id_label.grid(padx=10, pady=10)

        id_entry = Entry(top, textvariable=self.id, width="5")
        id_entry.grid(padx=10, pady=10) 
              
        id_button = Button(top, text='Consultar', 
                command=(lambda: self.obj_crud.consultar(self.conector, 
                                                        self.simbolo, 
                                                        self.informacion_text,
                                                        self.id,
                                                        top)))
        id_button.grid()

        
    
    def modificar_v(self):
        """
        Método llamado con un botón y que llama a dos métodos de
        la instancia de la clase Crud
        """
        self.obj_crud.modificar(self.conector,
                                 self.simbolo, 
                                 self.informacion_text,
                                 self.id)
        self.obj_crud.mostrar(self.tree)

    def eliminar_v(self):
        """
        Método llamado con un botón y que llama a dos métodos de
        la instancia de la clase Crud
        """
        
        self.obj_crud.baja(self.conector,
                            self.simbolo, 
                            self.informacion_text,
                            self.id) 
    
        self.obj_crud.mostrar(self.tree)
    
    