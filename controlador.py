from tkinter import Tk
from vista import ventana


class Controlador:
    """
    Clase desde la cual se instancia a la vista
    """
    def __init__(self, root):
        self.root_controlador = root
        ventana(self.root_controlador)
        

if __name__ == "__main__":

    root = Tk()
    application = Controlador(root)
    root.mainloop()