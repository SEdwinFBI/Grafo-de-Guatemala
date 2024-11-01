class Nodo():
    def __init__(self,id:str):

        self.id = id.lower()
        self.vecino = []
        self.visitado = False
        self.padre = None
        self.distancia = float("inf")
    
    def agregar_veciono(self,nodo:str,peso):
        
        if nodo not in self.vecino: #si no existe en el arreglo de vecino
            self.vecino.append([nodo.lower(),peso]) #agrega un arreglo en el arreglo vecino