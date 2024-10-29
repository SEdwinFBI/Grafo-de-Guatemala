import Grafica

grafo = Grafica.Grafica()


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


grafo.agregar_rama("Guatemala", "Chimaltenango", 176)
grafo.agregar_rama("Guatemala", "Sacatepéquez", 187)
grafo.agregar_rama("Guatemala", "Jutiapa", 155)
grafo.agregar_rama("Guatemala", "Chiquimula", 134)
grafo.agregar_rama("Chimaltenango", "Escuintla", 134)
grafo.agregar_rama("Chimaltenango", "Santa Rosa", 166)
grafo.agregar_rama("Chimaltenango", "Jutiapa", 109)
grafo.agregar_rama("Chimaltenango", "Huehuetenango", 187)
grafo.agregar_rama("Sacatepéquez", "Escuintla", 145)
grafo.agregar_rama("Sacatepéquez", "Jalapa", 187)
grafo.agregar_rama("Sacatepéquez", "El Progreso", 176)
grafo.agregar_rama("Escuintla", "Izabal", 167)
grafo.agregar_rama("Escuintla", "Petén", 176)
grafo.agregar_rama("Santa Rosa", "El Progreso", 156)
grafo.agregar_rama("Jutiapa", "Chiquimula", 165)
grafo.agregar_rama("Jutiapa", "Baja Verapaz", 178)
grafo.agregar_rama("Chiquimula", "Zacapa", 187)
grafo.agregar_rama("Chiquimula", "Alta Verapaz", 187)
grafo.agregar_rama("Jalapa", "Izabal", 186)
grafo.agregar_rama("Jalapa", "Petén", 176)
grafo.agregar_rama("El Progreso", "Alta Verapaz", 145)
grafo.agregar_rama("Zacapa", "Quiché", 143)
grafo.agregar_rama("Izabal", "Baja Verapaz", 153)
grafo.agregar_rama("Izabal", "Petén", 153)
grafo.agregar_rama("Petén", "Quiché", 132)
grafo.agregar_rama("Alta Verapaz", "Huehuetenango", 134)
grafo.agregar_rama("Baja Verapaz", "Totonicapán", 154)
grafo.agregar_rama("Quiché", "San Marcos", 124)
grafo.agregar_rama("Huehuetenango", "Quetzaltenango", 132)
grafo.agregar_rama("San Marcos", "Sololá", 133)
grafo.agregar_rama("Quetzaltenango", "Totonicapán", 26)
grafo.agregar_rama("Totonicapán", "Retalhuleu", 123)
grafo.agregar_rama("Sololá", "Suchitepéquez", 200)
grafo.agregar_rama("Retalhuleu", "Suchitepéquez", 100)



grafo.recorrer_grafo("Totonicapán","Suchitepéquez")
