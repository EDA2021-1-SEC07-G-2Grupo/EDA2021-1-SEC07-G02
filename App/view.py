"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
from DISClib.ADT import list as lt
assert cf
import controller


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo") 
    print("2- Consultar n numero de videos más vistos por país y en una categoria especifica(categoria, pais, numero de videos)")
    print("3- Consultar el video más trending por país(pais)")
    print("4- Consultar el video más trending por categoría (categoría)")
    print("5- Consultar los n videos con más likes por categoría")
    print("0- Salir")


def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

    
catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print("Material audiovisual cargados: " + str(lt.size(catalog['Video'])))
        print("primer elemento de la lista:")
        print(lt.firstElement(catalog["Video"]))
        print( "Numero de categorias cargadas: " + str(lt.size(catalog['video_id'])))
        print("Categorias cargadas:")
        n=1
        while n < lt.size(catalog['video_id']):
            print(lt.getElement(catalog["video_id"],n))
            n+=1

       
        

    elif int(inputs[0]) == 2:
       #pais = input("Nombre del país que desea consultar: ")
        #categoria = input("La categoría de los videos: ")
        size = int(input("Numero de videos que desea consultar: "))
        print("Qué algoritmo de ordenamiento desea utilizar: ")
        print("-1 selection ")
        print("-2 insertion ")
        print("-3 shell  ")
        print("-4 quick  ")
        print("-5 Merge \n ")
        algoritmo = int(input())
        vid=controller.sortVideos(catalog, size, algoritmo)
        print(vid)
 
    elif int(inputs[0]) == 3:
        pais = input("Nombre del pais a consultar: ")
        video = controller.getTrendingVideo(catalog, pais) #Hay que hacer la función controller.getTrendingVideo
        printTrendingVideo(video)

    elif int(inputs[0]) == 4:
        category_name = input("Categoría a buscar: ")
        video_categoría = controller.countTrendingByTags(catalog, category_name) #Hay que hacer la función controller.countTrendingByTags
        printTrendingByTags(video_categoría)

    elif int(inputs[0]) == 5:
        label = input("Etiqueta a buscar: ")
        book_count = controller.countBooksByTag(catalog, label) #TOCA VER COMO SE HACE ESTA COSA
        print('Se encontraron: ', book_count, ' Libros')

    else:
        sys.exit(0)
sys.exit(0)
