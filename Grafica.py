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
            "Guatemala": "#FFD700", 
            "Chimaltenango": "#8A2BE2", 
            "Sacatepéquez": "#FF6347",
            "Escuintla": "#87CEEB", 
            "Santa Rosa": "#FF4500", 
            "Jutiapa": "#32CD32",
            "Chiquimula": "#FF1493", 
            "Jalapa": "#4682B4", 
            "El Progreso": "#A52A2A",
            "Zacapa": "#00FA9A",
            "Izabal": "#9400D3", 
            "Petén": "#3CB371",
            "Alta Verapaz": "#20B2AA", 
            "Baja Verapaz": "#B8860B",
            "Quiché": "#4B0082",
            "Huehuetenango": "#DA70D6",
            "San Marcos": "#7FFF00",
            "Quetzaltenango": "#D2691E",
            "Totonicapán": "#FF00FF", 
            "Sololá": "#1E90FF",
            "Retalhuleu": "#FF69B4",
            "Suchitepéquez":"#FF69B4",
        
        }
        self.posiciones = {
        "Guatemala": (3.8, 8.2),
        "Chimaltenango": (3.3, 7.8),
        "Sacatepéquez": (3.5, 7.3),
        "Escuintla": (3.5, 6.5),
        "Santa Rosa": (4.5, 6.3),
        "Jutiapa": (5.7, 5.8),
        "Chiquimula": (6.8, 6.7),
        "Jalapa": (5.5, 6.8),
        "El Progreso": (4.5, 7.5),
        "Zacapa": (6.3, 7.7),
        "Izabal": (7.5, 8.7),
        "Petén": (6.8, 10),
        "Alta Verapaz": (5.3, 9.2),
        "Baja Verapaz": (4.5, 8.5),
        "Quiché": (3.3, 9.1),
        "Huehuetenango": (2.2, 9),
        "San Marcos": (1.2, 7.7),
        "Quetzaltenango": (2.3, 7),
        "Totonicapán": (2.7, 7.7),
        "Sololá": (3.1, 7.2),
        "Retalhuleu": (2.5, 6),
        "Suchitepéquez": (3.1, 6.3)
        }


        
    
    def graficar (self):
        pyplot.figure(figsize=(10, 8))#tamaño
        networkx.draw_networkx_nodes( #nodos, opciones
            G=self.grafica, pos=self.posiciones, node_size=500,
            node_color=[self.colores[depto] for depto in self.grafica.nodes]
        )
        labels = networkx.get_edge_attributes(
            self.grafica, "weight"
            )
        networkx.draw_networkx_edge_labels(#etiqueta
            self.grafica, pos=self.posiciones, edge_labels=labels,font_size=7
            )
        networkx.draw_networkx_edges(
            self.grafica, pos=self.posiciones, width=1.5
            )
        networkx.draw_networkx_labels(
            self.grafica, pos=self.posiciones, font_size=9, font_color="black"
                                      )
        pyplot.title("Grafo de Guatemala")
        pyplot.show()#se muestra la grafo
    
    def agregar_nodo(self,id):#nuevo nodo
        if id not in self.nodos:
            self.nodos[id]= Nodo.Nodo(id)#arreglo de objetos nodo
    
    def agregar_rama(self,nodo_A,nodo_B,peso):
        if nodo_A in self.nodos and nodo_B in self.nodos:#conexion de objetos
            self.nodos[nodo_A].agregar_veciono(nodo_B,peso)
            self.nodos[nodo_B].agregar_veciono(nodo_A,peso)
            
            
            self.grafica.add_edge(nodo_A,nodo_B,weight=peso)#conexion de nodos en la grafica
            
    def obtener_camino(self,nodo_B):
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
        self.dijkstra(nodo_A)
        camino = self.obtener_camino(nodo_B)
        print("Camino mas corto para llegar del punto A, al punto B",camino[0])
        print("Kilometros a recorrer",camino[1],"km")
        self.graficar()
        
    
    