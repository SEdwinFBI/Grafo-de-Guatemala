import Grafica as Grap

grafo = Grap.Grafica()

grafo.agregar_nodo("Guatemala")
grafo.agregar_nodo("Chimaltenango")
grafo.agregar_nodo("Sacatepequez")
grafo.agregar_nodo("Escuintla")
grafo.agregar_nodo("Santa Rosa")
grafo.agregar_nodo("Jutiapa")
grafo.agregar_nodo("Chiquimula")
grafo.agregar_nodo("Jalapa")
grafo.agregar_nodo("El Progreso")
grafo.agregar_nodo("Zacapa")
grafo.agregar_nodo("Izabal")
grafo.agregar_nodo("Peten")
grafo.agregar_nodo("Alta Verapaz")
grafo.agregar_nodo("Baja Verapaz")
grafo.agregar_nodo("Quiche")
grafo.agregar_nodo("Huehuetenango")
grafo.agregar_nodo("San Marcos")
grafo.agregar_nodo("Quetzaltenango")
grafo.agregar_nodo("Totonicapan")
grafo.agregar_nodo("Solola")
grafo.agregar_nodo("Retalhuleu")
grafo.agregar_nodo("Suchitepequez")

# nodo a y nodo b, y kilometros en enteros
# grafo.agregar_rama("Guatemala","Chimaltenango",000000)

# Ramas 0-4
# ciudad Capital
grafo.agregar_rama("Guatemala", "El Progreso", 80)
grafo.agregar_rama("Guatemala", "Baja Verapaz", 120)
grafo.agregar_rama("Guatemala", "Jalapa", 100)
grafo.agregar_rama("Guatemala", "Escuintla", 60)
grafo.agregar_rama("Guatemala", "Santa Rosa", 75)
grafo.agregar_rama("Guatemala", "Sacatepequez", 54)
grafo.agregar_rama("Guatemala", "Chimaltenango", 52)

# Chimaltenango
grafo.agregar_rama("Chimaltenango", "Quiche", 110)
grafo.agregar_rama("Chimaltenango", "Baja Verapaz", 130)
grafo.agregar_rama("Chimaltenango", "Sacatepequez", 54)
grafo.agregar_rama("Chimaltenango", "Escuintla", 53)
grafo.agregar_rama("Chimaltenango", "Suchitepequez", 128)
grafo.agregar_rama("Chimaltenango", "Solola", 86)

# Sacatepequez
grafo.agregar_rama("Sacatepequez", "Escuintla", 37)

# Escuintla
grafo.agregar_rama("Escuintla", "Santa Rosa", 89)
grafo.agregar_rama("Escuintla", "Suchitepequez", 70)

# Santa Rosa
grafo.agregar_rama("Santa Rosa", "Jutiapa", 70)
grafo.agregar_rama("Santa Rosa", "Jalapa", 110)

# Ramas 15-21
# Huehuetenango
grafo.agregar_rama("Huehuetenango", "Quiche", 140)
grafo.agregar_rama("Huehuetenango", "Totonicapan", 85)
grafo.agregar_rama("Huehuetenango", "Quetzaltenango", 70)
grafo.agregar_rama("Huehuetenango", "San Marcos", 120)

# San Marcos
grafo.agregar_rama("San Marcos", "Quetzaltenango", 55)
grafo.agregar_rama("San Marcos", "Retalhuleu", 90)

# Quetzaltenango
grafo.agregar_rama("Quetzaltenango", "Totonicapan", 25)
grafo.agregar_rama("Quetzaltenango", "Solola", 50)
grafo.agregar_rama("Quetzaltenango", "Retalhuleu", 65)
grafo.agregar_rama("Quetzaltenango", "Suchitepequez", 85)

# Totonicapan
grafo.agregar_rama("Totonicapan", "Quiche", 65)
grafo.agregar_rama("Totonicapan", "Solola", 50)

# Solola
grafo.agregar_rama("Solola", "Quiche", 100)
grafo.agregar_rama("Solola", "Suchitepequez", 75)

# Retalhuleu
grafo.agregar_rama("Retalhuleu", "Suchitepequez", 45)

# Suchitepequez

# ramas 10-14
# Izabal
grafo.agregar_rama("Izabal", "Peten", 292)
grafo.agregar_rama("Izabal", "Alta Verapaz", 260)
grafo.agregar_rama("Izabal", "Zacapa", 116)
#Peten
grafo.agregar_rama("Peten", "Quiche", 421)
grafo.agregar_rama("Peten", "Alta Verapaz", 256)
#alta Verapaz
grafo.agregar_rama("Alta Verapaz", "Quiche", 167)
grafo.agregar_rama("Alta Verapaz", "Baja Verapaz", 66)
grafo.agregar_rama("Alta Verapaz", "Zacapa", 188)
#baja verapaz
grafo.agregar_rama("Baja Verapaz", "El progreso", 77)
grafo.agregar_rama("Baja Verapaz", "Guatemala", 91)
grafo.agregar_rama("Baja Verapaz", "Quiche", 134)
#Quiche
#->Ramas ya enlazadas
#5-9
# Jutiapa
grafo.agregar_rama("Jutiapa", "Santa Rosa", 75)        
grafo.agregar_rama("Jutiapa", "Jalapa", 58)             
grafo.agregar_rama("Jutiapa", "Chiquimula", 94)         

# Chiquimula
grafo.agregar_rama("Chiquimula", "Jalapa", 81)          
grafo.agregar_rama("Chiquimula", "Zacapa", 26)          

# Jalapa
grafo.agregar_rama("Jalapa", "el Progreso", 55)        
grafo.agregar_rama("Jalapa", "Zacapa", 60)           

# Zacapa
grafo.agregar_rama("Zacapa", "el Progreso", 40)  

deparamentoSalida = str(input("Ingrese el departamento de salida: "))
departamentoLlegada = str(input("Ingrese el departamento de llegada: "))

#deparamentoSalida = "santa rosa"
#departamentoLlegada = "peten"

try:
    grafo.recorrer_grafo(deparamentoSalida, departamentoLlegada)
except Exception as e:
    print(f"Ocurrio un error al ejecutar la aplicacion")


