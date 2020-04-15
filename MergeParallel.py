import multiprocessing as mp
import time
import random

def sort(nlist):
    if len(nlist)>1: #Comprobamos que la lista es mayor que 1
        mid = len(nlist)//2 #Dividimos la lista en 2 para aplicar DyV
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        sort(lefthalf) #Realizamos la llamada para la primera mitad
        sort(righthalf) #Realizamos la llamada para la segunda mitad
        i=j=k=0  #Inicializamos variables para recorrer cada mitad de la lista pasada por parametros     
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]: #Ordenamos los elementos de la lista en funcion de si están en la primera mitad o en la segunda
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf): #Añadimos a la lista final de cada una de las mitades
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    return nlist #Devolvemos la lista final

def core_work(list, inicio, fin): #Pasamos el inicio y el final de la sublista que va a trabajar cada core
	sort(list[inicio:fin])

class MergeSort():
	def __init__(self, ncores):#__init__ de ejecuta cada vez que se instancia esa clase
		self.ncores = ncores

	def execute(self, elements): #pasamos al run la lista
		size_core = int(len(elements) / self.ncores) #obtenemos el tamaño de las sublistas con las que trabaja cada core
		cores = []
		for i in range(0, self.ncores): #Dividimos la lista entre el numero de cores
			cores.append(mp.Process(target=core_work, args=(elements, size_core*i, size_core*(i+1))))
			cores[i].start() #Lanzamos la ejecucion del core
		for i in cores:
			i.join() #Bloqueamos cualquier llamada hasta que terminen todos los cores
		sort(elements)

if __name__ == '__main__':
    A = [random.randint(0,215) for j in range(21845538)] #Creamos una lista del tamaño del numero de expediente 21845538
    inicioP = time.time()
    MergeSort(mp.cpu_count()).execute(A)
    finP = time.time()
    # print (A)
    print('\n\nMatriz  A y B se han multiplicado con exito en SECUENCIAL ha tardado ', finP-inicioP)