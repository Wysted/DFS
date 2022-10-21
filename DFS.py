class Vertice:
    def __init__(self,i):
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.padre = None
        self.vecinos = []

    def agregarVecino(self,v):
        if v not in self.vecinos:
            self.vecinos.append(v)

class Grafica:
    def __init__(self):
        self.vertices = {}
        self.recorrido = []
        self.i = 0

    
    def agregarVertice(self,v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)

    def agregarArista(self,a,b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b)
            self.vertices[b].agregarVecino(a)

    def dfs(self,r,v):
        #marca el vertice r como visitado   
        if r in self.vertices :
            if r == v:
                print("Se llego al vertice requerido: "+str(v))
                print("El recorrido que se hizo hasta llegar al vertice deseado es el siguiente")
                print(' → '.join(str(n) for n in self.recorrido))

                quit()
            self.vertices[r].visitado = True
            for nodo in self.vertices[r].vecinos:
                if self.vertices[nodo].visitado == False:
                    self.vertices[nodo].padre = r
                    self.recorrido.append(str(r)+""+str(nodo))
                    self.dfs(nodo,v)
                  
                 
                    
                    
               
                
def main():
    g = Grafica()

    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37
,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]
    #Agrega vertices del 1 al 64
    for nodo in l:
        g.agregarVertice(nodo)

    l = [1,2, 1,13, 2,3, 3,4, 4,5 ,5,6, 6,7 ,7,8, 8,9, 9,10, 10,11, 11,12, 13,14, 13,15, 15,16 ,16,17 
    ,17,18, 18,19, 19,20, 20,21, 21,22, 22,23, 23,24, 23,25, 25,26, 26,27, 27,28 ,28,29,
     27,30, 30,31, 31,32, 32,33, 33,34 ,34,35,
    34,36, 36,37 ,37,38 ,38,39, 38,40, 40,41, 41,42, 42,43, 43,44, 44,45 ,45,46 ,46,47, 47,48, 48,49, 49,50, 47,51,
    51,52 ,52,53 ,53,54 ,53,55, 55,56, 56,57, 57,58, 58,59 ,59,60 ,59,61 ,58,62 ,62,63, 63,64]

    for i in range(0,len(l) - 1,2):
        g.agregarArista(l[i],l[i+1])
    g.dfs(1,50)
main()