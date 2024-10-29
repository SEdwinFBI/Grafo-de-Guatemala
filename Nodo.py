class Nodo():
    def __init__(self,id):
        self.id = id
        self.vecino = []
        self.visitado = False
        self.padre = None
        self.distancia = float("inf")
    
    def agregar_veciono(self,nodo,peso):
        if nodo not in self.vecino: #si no existe en el arreglo de vecino
            self.vecino.append([nodo,peso]) #agrega un arreglo en el arreglo vecino