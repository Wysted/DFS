#Define lo que es un vertice
class Vertice:
    def __init__(self,i):
        #Identificador del vertice
        self.id = i
        #Si ya fue visitado o no
        self.visitado = False
        #Identificacion del vertice padre
        self.padre = None
        #Si tiene vertices adyacentes
        self.vecinos = []

    #Agrega los vertices adyacentes
    def agregarVecino(self,v):
        if v not in self.vecinos:
            self.vecinos.append(v)
#Funcion general, lo que hace es 'dibujar el laberito'
class Grafica:
    def __init__(self):
        #vertices
        self.vertices = {}
        #Muestra el recorrido
        self.recorrido = []
        

    #Agrega los vertices
    def agregarVertice(self,v):
        if v not in self.vertices:
            #Agrega el objeto Vertice a vertices
            self.vertices[v] = Vertice(v)

    #Agrega las aristas en formato a-b
    def agregarArista(self,a,b):
        if a in self.vertices and b in self.vertices:
            #Tanto como a es vecino de b, b es vecino de a
            self.vertices[a].agregarVecino(b)
            self.vertices[b].agregarVecino(a)

    #Algoritmo en busqueda de profundidad
    #Recibe r = vertice inicial, v = vertice final
    def dfs(self,r,v):
        #Recorre por todos los vertices
        if r in self.vertices :
            # Comprueba que el vertice actual, sea el vertice final
            if r == v:
                #Imprime el vertice objetivo
                print("Se llego al vertice requerido: "+str(v))
                print("El recorrido que se hizo hasta llegar al vertice deseado es el siguiente")
                #Muestra el recorrido desde el vertice inicial hasta llegar al final
                print(' → '.join(str(n) for n in self.recorrido))
                #Cierra el programa
                quit()
            #Marca el vertice actual como visitado
            self.vertices[r].visitado = True
            #Recorre los vertices vecinos
            for nodo in self.vertices[r].vecinos:
                #Revisa que el vertice vecino no este vistitado
                if self.vertices[nodo].visitado == False:
                    #Marca al vertice actual como vertice padre, en el vertice vecino visitado
                    self.vertices[nodo].padre = r
                    #Guarda el recorrido
                    self.recorrido.append(str(r)+"-"+str(nodo))
                    #Se vuelve a llamar a la funcion de forma recursiva
                    self.dfs(nodo,v)
                  

def main():
    #Se crea el objeto
    laberinto = Grafica()
    #Se introduce los vertices y su identificacion
    vertices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37
        ,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]
    #Agrega vertices del 1 al 64
    for nodo in vertices:
        laberinto.agregarVertice(nodo)
    #Se introduce las aristas
    aristas = [1,2, 1,13, 2,3, 3,4, 4,5 ,5,6, 6,7 ,7,8, 8,9, 9,10, 10,11, 11,12, 13,14, 13,15, 15,16 ,16,17 
         ,17,18, 18,19, 19,20, 20,21, 21,22, 22,23, 23,24, 23,25, 25,26, 26,27, 27,28 ,28,29,
         27,30, 30,31, 31,32, 32,33, 33,34 ,34,35,34,36, 36,37 ,37,38 ,38,39, 38,40, 40,41,
         41,42, 42,43, 43,44, 44,45 ,45,46 ,46,47, 47,48, 48,49, 49,50, 47,51, 51,52 ,52,53 ,53,54 
         ,53,55, 55,56, 56,57, 57,58, 58,59 ,59,60 ,59,61 ,58,62 ,62,63, 63,64]
    #Agrega las aristas formato a-b
    for i in range(0,len(aristas) - 1,2):
        laberinto.agregarArista(aristas[i],aristas[i+1])
    #Se da el vertice inicial y final
    laberinto.dfs(1,50)
    
#Llama a la funcion principal
main()
