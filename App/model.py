"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as inser
from DISClib.Algorithms.Sorting import selectionsort as selc
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo_de_lista):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    if tipo_de_lista==1:
        lista=str("SINGLE_LINKED")
    elif tipo_de_lista==2:
        lista=str("ARRAY_LIST")
    catalog = {
                "Video": None,
                'video_id': None
               }
    catalog['Video'] = lt.newList(lista)           
    catalog['video_id'] = lt.newList(lista)

    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, videos):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog["Video"], videos)

    # Se obtienen los autores del libro
       

def addVideoCategory_id(catalog, categoriavid):
    """
    Adiciona un tag a la lista de tags
    """
    t = newVidcategoria(categoriavid['id'], categoriavid['name'])
    lt.addLast(catalog["video_id"], t)

# Funciones para creacion de datos

def newVidcategoria(_id, category_id):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    categoriavid = {'id': _id, 'category_id': category_id}
    return categoriavid


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una list

def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return (float(video1['views']) < float(video2['views']))

# Funciones de ordenamiento

def sortBooks_byViews(catalog, size, algoritmo):
    sub_list = lt.subList(catalog['Video'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if algoritmo==1:
        sorted_list = selec.sort(sub_list, cmpVideosByViews)
    elif algoritmo==2:
        sorted_list = inser.sort(sub_list, cmpVideosByViews)
    else:
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg#sorted_list,
    

