import Grafica as Grap

grafo = Grap.Grafica()


grafo.agregar_nodo("Guatemala")
grafo.agregar_nodo("Chimaltenango")
grafo.agregar_nodo("Sacatepéquez")
grafo.agregar_nodo("Escuintla")
grafo.agregar_nodo("Santa Rosa")
grafo.agregar_nodo("Jutiapa")
grafo.agregar_nodo("Chiquimula")
grafo.agregar_nodo("Jalapa")
grafo.agregar_nodo("El Progreso")
grafo.agregar_nodo("Zacapa")
grafo.agregar_nodo("Izabal")
grafo.agregar_nodo("Petén")
grafo.agregar_nodo("Alta Verapaz")
grafo.agregar_nodo("Baja Verapaz")
grafo.agregar_nodo("Quiché")
grafo.agregar_nodo("Huehuetenango")
grafo.agregar_nodo("San Marcos")
grafo.agregar_nodo("Quetzaltenango")
grafo.agregar_nodo("Totonicapán")
grafo.agregar_nodo("Sololá")
grafo.agregar_nodo("Retalhuleu")
grafo.agregar_nodo("Suchitepéquez")

#nodo a y nodo b, y kilometros en enteros
#grafo.agregar_rama("Guatemala","Chimaltenango",000000)

#Ramas 0-4 Andre 
#ciudad Capital
grafo.agregar_rama("Guatemala", "El Progreso", 80)
grafo.agregar_rama("Guatemala", "Baja Verapaz", 120)
grafo.agregar_rama("Guatemala", "Jalapa", 100)
grafo.agregar_rama("Guatemala", "Escuintla", 60)
grafo.agregar_rama("Guatemala", "Santa Rosa", 75)
grafo.agregar_rama("Guatemala", "Sacatepéquez", 54)
grafo.agregar_rama("Guatemala", "Chimaltenango", 52)

#Chimaltenango 
grafo.agregar_rama("Chimaltenango", "Quiché", 110)
grafo.agregar_rama("Chimaltenango", "Baja Verapaz", 130)
grafo.agregar_rama("Chimaltenango", "Sacatepéquez", 54)
grafo.agregar_rama("Chimaltenango", "Escuintla", 53)
grafo.agregar_rama("Chimaltenango", "Suchitepéquez", 128)
grafo.agregar_rama("Chimaltenango", "Sololá", 86)

#Sacatepéquez
grafo.agregar_rama("Sacatepéquez", "Escuintla", 37)

#Escuintla
grafo.agregar_rama("Escuintla", "Santa Rosa", 89)
grafo.agregar_rama("Escuintla", "Suchitepéquez", 70)

#Santa Rosa
grafo.agregar_rama("Santa Rosa", "Jutiapa", 70)
grafo.agregar_rama("Santa Rosa", "Jalapa", 110)



deparamentoSalida = str(input("Ingrese el departamento de salida: "))
departamentoLlegada = str(input("Ingrese el departamento de llegada: "))


grafo.recorrer_grafo(deparamentoSalida, departamentoLlegada)
