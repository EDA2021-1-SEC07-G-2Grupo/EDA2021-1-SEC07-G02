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

from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """

    catalog = {
                "Video": None,
                'video_id': None
               }
    catalog['Video'] = lt.newList()           
    catalog['video_id'] = lt.newList("SINGLE_LINKED")

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

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento