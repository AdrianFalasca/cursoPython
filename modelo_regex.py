class Regex:
    """
    Clase que luego será instanciada por el modelo para hacer
    las validaciones de los campos
    """    
    def __init__(self,):
        """
        Constructor que contiene los regex
        """
        self.conector = r"[a-zA-Záéíóú ñ1]{4,30}"
        self.informacion_texto = r"[a-zA-Záéíóúñ¬∧∨∆→↔⊻⊤⊥, 0-9]{10,}"