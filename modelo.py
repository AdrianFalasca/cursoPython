from tkinter import messagebox as ms
from tkinter import END
import re
from modelo_regex import Regex
from modelo_base import *
from datetime import datetime
from observador import Observado


class Crud(Observado):
    """ 
    Clase que contiene los métodos: alta, modificar, consultar y baja.
    Y otros para salir, borrar campos y mostrar.
    Hereda de la clase Observado el método notificar utilizado en el 
    método consultar de la clase Crud. 
    """ 
     
    def __init__(self):
        """ 
        Constructor que contiene la instancia de la clase Regex y un contador.
        """  
        self.obj_regex = Regex()
        self.inicio = 0
        

    def salir(self, root):
        """
        Método para salir de la aplicación.
        """  
        si = ms.askquestion("Salir",
                            "Deseas salir de la aplicación?")

        if si=="yes":
            root.destroy()


    def borrar_campos(self, *arg):
        """
        Método para borrar campos
        """
        arg[0].delete(1.0, END)
        
        for a in arg[1:]:
            a.set("")
        

    def decorador(func):
        def envoltura(*arg, **kwarg):          
            """
            Función que decora a los métodos: alta, baja y modificar.
            Los registra en un archivo txt. 
            """

            fecha_2 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            log = open("registro_log.txt", "a", encoding="utf-8")
            
            if arg[1].get():
                if arg[0].inicio == 0:
                    log.write("***" * 24) 
                    log.write("\nRegistro del alta, baja y modificación " +
                            "en la fecha: %s\n" % (fecha_2))
                    log.write("***" * 24)
                    arg[0].inicio += 1

                log.write("\n\nLlamada %s al metodo '%s'. Fecha: %s \n"  \
                            % (envoltura.contador,
                               func.__name__,
                               fecha_2))

                log.write("Id: %s\nConector: %s\nSimbolo: %s\nInformacion: %s \n"\
                            % (arg[4].get(),
                               arg[1].get(), 
                               arg[2].get(), 
                               arg[3].get(1.0, END)))
                    
                envoltura.contador += 1

            log.close()
            
            return func(*arg, **kwarg)
                  
        envoltura.contador = 0
        
        return envoltura

   
    @decorador    
    def alta(self, conector, simbolo, informacion_text, id):        
        """
        Método para dar de alta en campos. 
        Filtra con regex y los carga con ORM
        """

        if not re.match(self.obj_regex.conector, conector.get()):
    
            ms.showwarning("Error",
                            "Introduzca un conector lógico") 

        elif not simbolo.get():
    
            ms.showwarning("Error",
                            "Elija el símbolo del conector lógico") 

       
        elif not re.match(self.obj_regex.informacion_texto,
                          informacion_text.get(1.0, END)):
    
            ms.showwarning("Error",
                            "Introduzca un texto mínimo de 10 caracteres")       

        else:  
 
            logica = Logica()
            logica.conector = conector.get()
            logica.simbolo = simbolo.get()
            logica.info = informacion_text.get(1.0, END)
            logica.save()
            
            ms.showinfo("Mensaje", "Registro creado correctamente")
            
            
            self.borrar_campos(informacion_text,
                                conector,
                                simbolo,
                                id)    

    
    def consultar(self, conector, simbolo, informacion_text, id, top):
        """
        Método para consultar la tabla utilizando el id.
        Filtra y obtiene los datos con ORM.
        Utiliza el método notificar de la clase padre de Crud(Observado)
         y le pasa parámetros.
        """ 
        informacion = Logica.select().where(Logica.id == id.get())

        if not informacion:
    
            ms.showwarning("Error", "Ingrese el id correctamente")
   
        else:       
            
            top.destroy()
                
            for x in informacion:
            
                conector.set(x.conector)
                simbolo.set(x.simbolo)
                informacion_text.insert(1.0, x.info)

            self.notificar(x.id, x.conector, x.simbolo, x.info)
            ms.showinfo("Mensaje", 
                        "Registro consultado correctamente")
    

    @decorador    
    def modificar(self, conector, simbolo, informacion_text, id):
        """ 
        Método para actualizar utilizando el id.
        Filtra con regex y obtiene el id y actualiza con ORM.
        """         


        if not Logica.select().where(Logica.id == id.get()):
    
            ms.showwarning("Error", "Primero consulte el id")
   
        else:
    
            if not re.match(self.obj_regex.conector, conector.get()):
    
                ms.showwarning("Error",
                                "Introduzca un conector lógico") 

            elif not simbolo.get():
    
                ms.showwarning("Error",
                                "Elija el símbolo del conector lógico") 

       
            elif not re.match(self.obj_regex.informacion_texto,
                              informacion_text.get(1.0, END)):
    
                ms.showwarning("Error",
                                "Introduzca un texto mínimo de 10 caracteres")       

            else:


                actualizar = Logica.update(conector=conector.get(),
                                            simbolo=simbolo.get(),
                                            info=informacion_text.get(1.0, END)
                                            ).where(Logica.id == id.get())
                actualizar.execute()

                ms.showinfo("Mensaje",
                            "Registro actualizado correctamente")

                
                self.borrar_campos(informacion_text, 
                                   simbolo, 
                                   conector,
                                   id)
                
                
    @decorador        
    def baja(self, conector, simbolo, informacion_text, id):
        """
        Método para borrar utilizando el id.
        Filtra el id y borrar los datos con ORM
        """        
  

        if not Logica.select().where(Logica.id == id.get()):
    
            ms.showwarning("Error", "Primero consulte el id")
   
        else:
        
            borrar = Logica.get(Logica.id == id.get())
            
            borrar.delete_instance()          
            
            ms.showinfo("Mensaje",
                        "Registro borrado correctamente") 

            self.borrar_campos(informacion_text, 
                                simbolo, 
                                conector,
                                id)
    
    
    def mostrar(self, tree):
        """
        Método para mostrar todos los registros de la tabla
        """        
        records = tree.get_children()
        for elemento in records:
            tree.delete(elemento)

        for x in Logica.select():
            tree.insert('', 0, text = x.id,
                values = (x.fecha, x.conector, x.simbolo, x.info))