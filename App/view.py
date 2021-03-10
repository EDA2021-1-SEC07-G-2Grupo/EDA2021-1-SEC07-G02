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
    print("5- Consultar los n videos con más likes por 'tag' de acuerdo a un país especifico")
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


def separador():
    return("-------------------------------------------------------------------------")    



def print_primero_de_lista(Primer_elemento):
    print(" -Title: "+str(Primer_elemento["title"]))
    print(" -Channel title: "+str(Primer_elemento["channel_title"]))
    print(" -Trending Date: "+str(Primer_elemento["trending_date"]))
    print(" -Country: "+str(Primer_elemento["country"]))
    print(" -Views: "+str(Primer_elemento["views"]))
    print(" -Likes: "+str(Primer_elemento["likes"]))
    print(" -Dislikes "+str(Primer_elemento["dislikes"]))


def print_todo_elemento(catalog)->None:
    n=1
    while n < lt.size(catalog):
          print(lt.getElement(catalog,n))
          n+=1
def imprime_toda_lista_econtrada_req1(catalog):
     n=0
     while n<lt.size(video_ordenados_por_vistas):
            video_ordenado=lt.getElement(catalog,n)
            print("Posición: "+str(1+n))
            print("-"+"Trending_date: "+video_ordenado["trending_date"])
            print("-"+"Title: "+video_ordenado["title"])
            print("-"+"Chanel_title: "+video_ordenado["channel_title"])
            print("-"+"Publish_time: "+video_ordenado["publish_time"])
            print("-"+"Views: "+video_ordenado["views"])
            print("-"+"Likes: "+video_ordenado["likes"])
            print("-"+"Dislikes: "+video_ordenado["dislikes"])
            print(separador())
            n+=1
def print_req3(catalog):
    vid=lt.getElement(catalog,1)
    print("-"+"Title: "+vid["title"])
    print("-"+"Channel title: "+vid["Channel title"])
    print("-"+"Country: "+vid["country"])
    print("-"+"Días: "+str(vid["dias"]))
    print(separador())
           
def print_req4(catalog):
    n=0
    while lt.size(video_por_likes)>n:
            vid=lt.getElement(video_por_likes,n)
            print("Video "+str(n+1))
            print("-"+"Title: "+vid["title"])
            print("-"+"Chanel_title: "+vid["channel_title"])
            print("-"+"Publish_time: "+vid["publish_time"])
            print("-"+"Likes: "+vid["likes"])
            print("-"+"Dislikes: "+vid["dislikes"])
            print("-"+"Tags: "+vid["tags"])
            print(separador())
            n+=1


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
        print(separador())
        print("Material audiovisual cargados: " + str(lt.size(catalog['Video'])))
        print(separador())
        print("Primer elemento de la lista:")
        Primer_elemento=lt.firstElement(catalog["Video"])
        print_primero_de_lista(Primer_elemento)
        print(separador())
        print( "Numero de categorias cargadas: " + str(lt.size(catalog['video_id'])))
        print("Categorias cargadas:") 
        print_todo_elemento(catalog["video_id"])
        print(separador())
    elif int(inputs[0]) == 2:
        pais = str(input("Escriba el nombre del país que desea consultar (ingles): "))
        catalogo=catalog["Video"]
        country=controller.getvideobycountry(catalogo, pais)
        if lt.size(country)==0 :
            print("No se ha encontrado videos del país que ha escrito")
            print(separador())
        else:
            categoria = int(input("Escriba el numero de la categoría a consultar: "))
            categoria=str(categoria)
            categ= controller.GetVideosbycategoria(country, categoria)
            if lt.size(categ)==0:
                print("No se ha encontrado videos de "+pais+" en al categoría "+ categoria)
                print(separador())
            else:
                size = int(input("Escriba el Numero de videos que desea consultar: "))       
                video_ordenados_por_vistas=controller.sortVideos(categ, size)
                print(separador())
                print("-"+"País: "+pais)
                imprime_toda_lista_econtrada_req1(video_ordenados_por_vistas)
               
    elif int(inputs[0]) == 3:
        pais = input("Nombre del pais a consultar: ")
        video = controller.getTrendingVideo(catalog, pais) #Hay que hacer la función controller.getTrendingVideo
        printTrendingVideo(video)

    elif int(inputs[0]) == 4:
        category_name = int (input("Escriba el numero de la categoría que quiere consultar: "))
        print(separador())
        category_name=str(category_name)
        video_categoria = controller.GetVideosbycategoria(catalog["Video"], category_name)
        if lt.size(video_categoria)==0:
            print(separador())
            print("No se ha encontrado videos en la categoría "+category_name)
            print(separador())
        else:
            separador()
            video_por_dias= controller.Get_rending_categoria(video_categoria)
            Primero_por_categoria=controller.sortVideos_byDias(video_por_dias)
            print_req3(Primero_por_categoria)

    elif int(inputs[0]) == 5:
         pais = str(input("Escriba el nombre del país que desea consultar (ingles): "))
         print(separador())
         catalogo=catalog["Video"]
         country=controller.getvideobycountry(catalogo, pais)
         if lt.size(country)==0 :
            print("No se ha encontrado videos del país que ha escrito")
            print(separador())
         else:
             label = str(input("Etiqueta a buscar: "))
             videos_etiquetados=controller.video_por_etiqueta(country,label)
             if lt.size(videos_etiquetados)==0:
                print("no se ha encontrado un video con la etiqueta"+ label)
             else:
                print("Se han encontrado un total de "+ str(lt.size(videos_etiquetados))+" videos con la etiqueta "+label+", por favor pida una cantidad de datos dentro del rango")
                size=int(input("Escriba la cantidad de videos que desea consultar "))
                print(separador())
                video_por_likes=controller.videos_por_likes(videos_etiquetados, size)
                print_req4(video_por_likes)
                
    else:
        sys.exit(0)
sys.exit(0)
