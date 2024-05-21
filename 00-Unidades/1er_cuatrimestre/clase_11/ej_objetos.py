class Boligrafo:
    def __init__(self, grosor_punta:str, color:str)->None:
        self.capacidad_tinta_maxima = 100
        self.grosor_punta = grosor_punta
        self.cantidad_tinta = 80
        self.color = color
    
    def escribir(self, texto:str)->str:
        largo_texto = len(texto)
        cantidad_tinta = self.cantidad_tinta

        if cantidad_tinta >= largo_texto:
            cantidad_tinta - largo_texto
            return texto
        else:
            respuesta = "No alcanza la tinta"
            return respuesta
        
    def recargar(self, cantidad_recargar:int)->str:
        suma_tinta = self.cantidad_tinta + cantidad_recargar

        if suma_tinta < self.capacidad_tinta_maxima:
            respuesta = "Lapicera recargada"
            return respuesta
        else:
            pass


Boligrafo_azul = ("fino","azul")
Boligrafo_rojo = ("grueso","rojo")