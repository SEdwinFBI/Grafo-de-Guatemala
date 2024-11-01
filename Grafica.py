#librerias
import networkx
import matplotlib.pyplot as pyplot 
#clases
import Nodo

class Grafica():
    def __init__(self):
        self.grafica = networkx.Graph()#grafo no dirigido
        self.nodos:Nodo.Nodo= {}#diccionario 
        self.colores = {
        "guatemala": "#FFD700", 
        "chimaltenango": "#8A2BE2", 
        "sacatepequez": "#FF6347",
        "escuintla": "#87CEEB", 
        "santa rosa": "#FF4500", 
        "jutiapa": "#32CD32",
        "chiquimula": "#FF1493", 
        "jalapa": "#4682B4", 
        "el progreso": "#A52A2A",
        "zacapa": "#00FA9A",
        "izabal": "#9400D3", 
        "peten": "#3CB371",
        "alta verapaz": "#20B2AA", 
        "baja verapaz": "#B8860B",
        "quiche": "#4B0082",
        "huehuetenango": "#DA70D6",
        "san marcos": "#7FFF00",
        "quetzaltenango": "#D2691E",
        "totonicapan": "#FF00FF", 
        "solola": "#1E90FF",
        "retalhuleu": "#FF69B4",
        "suchitepequez": "#FF69B4",
    }

        self.posiciones = {
            "guatemala": (4.4, 7.0),
            "chimaltenango": (3.7, 6.8),
            "sacatepequez": (3.8, 6.3),
            "escuintla": (3.5, 5.5),
            "santa rosa": (4.5, 5.7),
            "jutiapa": (5.7, 5.8),
            "chiquimula": (6.8, 6.7),
            "jalapa": (5.5, 6.8),
            "el progreso": (5.4, 7.7),
            "zacapa": (6.3, 7.7),
            "izabal": (7.4, 8.4),
            "peten": (5.0, 10.7),
            "alta verapaz": (4.7, 9.2),
            "baja verapaz": (4.5, 8.0),
            "quiche": (3.3, 8.1),
            "huehuetenango": (2.2, 9),
            "san marcos": (1.2, 7.7),
            "quetzaltenango": (2.3, 7),
            "totonicapan": (2.7, 7.7),
            "solola": (3.1, 7.2),
            "retalhuleu": (2.5, 6),
            "suchitepequez": (3.1, 6.3)
        }



        
    
    def graficar (self,nodo_a,nodo_b,ruta_nodos):
        nodo_a=nodo_a.lower()
        nodo_b=nodo_b.lower()
        pyplot.figure(figsize=(10, 8))#tamaño
        #color de nodos
        node_colors = [
        "red" if depto.lower() == nodo_a or depto.lower() == nodo_b else self.colores[depto.lower()]
        for depto in self.grafica.nodes
        ]
        networkx.draw_networkx_nodes( #nodos, opciones
            G=self.grafica, pos=self.posiciones, node_size=500,
            node_color=node_colors
        )

        labels = networkx.get_edge_attributes(
            self.grafica, "weight"
            )
        networkx.draw_networkx_edge_labels(#etiqueta
            self.grafica, pos=self.posiciones, edge_labels=labels,font_size=7
            )
        #color de ramas
        edge_colors = [
        "red" if (u in ruta_nodos and v in ruta_nodos) else "black"
        for u, v in self.grafica.edges
         ]
        networkx.draw_networkx_edges(
            self.grafica, pos=self.posiciones, width=1.5,edge_color=edge_colors
            )
        networkx.draw_networkx_labels(
            self.grafica, pos=self.posiciones, font_size=9, font_color="black"
                                      )
        pyplot.title("Grafo de Guatemala")
        pyplot.show()#se muestra la grafo
    
    def agregar_nodo(self,id:str):#nuevo nodo
        id = id.lower()
        if id not in self.nodos:
            self.nodos[id]= Nodo.Nodo(id)#arreglo de objetos nodo
    
    def agregar_rama(self,nodo_A:str,nodo_B:str,peso):
        nodo_A=nodo_A.lower()
        nodo_B=nodo_B.lower()
        if nodo_A in self.nodos and nodo_B in self.nodos:#conexion de objetos
            self.nodos[nodo_A].agregar_veciono(nodo_B,peso)
            self.nodos[nodo_B].agregar_veciono(nodo_A,peso)
            
            
            self.grafica.add_edge(nodo_A,nodo_B,weight=peso)#conexion de nodos en la grafica
            
    def obtener_camino(self,nodo_B):
        nodo_B=nodo_B.lower()
        camino=[]
        actual=nodo_B
        while(actual != None):
            camino.insert(0,actual)
            actual = self.nodos[actual].padre
        return [camino,+self.nodos[nodo_B].distancia]
    
    def menor_distancia(self,lista):#buscar el menor camino en un arreglo
        if len(lista)> 0:
            minimo = self.nodos[lista[0]].distancia
            n = lista[0]
            
            for i in lista:
                if minimo > self.nodos[i].distancia:
                    minimo =self.nodos[i].distancia
                    n = i
            return n
            
    def dijkstra(self,nodo_A):
        nodo_A=nodo_A.lower()
        if nodo_A in self.nodos:
            self.nodos[nodo_A].distancia = 0
            actual = nodo_A
            no_visitados=[]
            
            for nodo in self.nodos:
                if nodo!= nodo_A:
                    self.nodos[nodo].distancia = float('inf')
                self.nodos[nodo].padre = None
                no_visitados.append(nodo)
            
            while(len(no_visitados)>0):
                for vecino in self.nodos[actual].vecino:
                    if self.nodos[vecino[0]].visitado == False:
                        if self.nodos[actual].distancia + vecino[1]<self.nodos[vecino[0]].distancia:
                            self.nodos[vecino[0]].distancia = self.nodos[actual].distancia + vecino[1]
                            self.nodos[vecino[0]].padre = actual
                
                self.nodos[actual].visitado=True
                no_visitados.remove(actual)
            
                actual = self.menor_distancia(no_visitados)
        else:
            return False
    
    def recorrer_grafo(self,nodo_A,nodo_B):
        nodo_A=nodo_A.lower()
        nodo_B=nodo_B.lower()
        self.dijkstra(nodo_A)
        camino = self.obtener_camino(nodo_B)
        print(f"Camino mas corto para llegar {nodo_A} a {nodo_B} es: ",camino[0])
        print("Kilometros a recorrer",camino[1],"km")
        self.graficar(nodo_A,nodo_B,camino[0])
        
    
    