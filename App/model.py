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
                "video_id": None,
               'trending_date': None,
               'title': None,
               'channel_title': None,
               'category_id': None,
               'publish_time': None,
               'tags': None,
               'views': None,
               'likes': None,
               'dislikes': None,
               'country': None 
               }
    catalog['video_id'] = lt.newList("ARRAY_LIST")           
    catalog['trending_date'] = lt.newList("ARRAY_LIST")
    catalog['title'] = lt.newList("ARRAY_LIST")
    catalog['channel_title'] = lt.newList('ARRAY_LIST')
    catalog['category_id'] = lt.newList('ARRAY_LIST')
    catalog['publish_time'] = lt.newList('ARRAY_LIST')
    catalog['tags'] = lt.newList('ARRAY_LIST')
    catalog['views'] = lt.newList('ARRAY_LIST')
    catalog['likes'] = lt.newList('ARRAY_LIST')
    catalog['dislikes'] = lt.newList('ARRAY_LIST')
    catalog['country'] = lt.newList('ARRAY_LIST')
    catalog['categoryid'] = lt.newList('ARRAY_LIST')
    
    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['video_id'], video)
    # Se obtienen los autores del libro
    trending_date = video['trending_date'].split(",")
    title = video['title'].split(",")
    channel_title = video['channel_title'].split(",")
    category_id = video['category_id'].split(",")
    publish_time = video['publish_time'].split(",")
    tags = video['tags'].split(",")
    views = video['views'].split(",")
    likes = video['likes'].split(",")
    dislikes = video['dislikes'].split(",")
    country = video['country'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for trending_date in trending_date:
        addBookAuthor(catalog, trending_date.strip(), video)
    for title in title:
        addBookAuthor(catalog, title.strip(), video)
    for channel_title in channel_title:
        addBookAuthor(catalog, channel_title.strip(), video)
    for category_id in category_id:
        addBookAuthor(catalog, category_id.strip(), video)
    for publish_time in publish_time:
        addBookAuthor(catalog, publish_time.strip(), video)
    for tags in tags:
        addBookAuthor(catalog, tags.strip(), video)
    for views in views:
        addBookAuthor(catalog, views.strip(), video)
    for likes in likes:
        addBookAuthor(catalog, likes.strip(), video)
    for dislikes in dislikes:
        addBookAuthor(catalog, dislikes.strip(), video)
    for country in country:
        addBookAuthor(catalog, country.strip(), video)


def addBookAuthor(catalog, authorname, video):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    authors = catalog['authors']
    posauthor = lt.isPresent(authors, authorname)
    if posauthor > 0:
        author = lt.getElement(authors, posauthor)
    else:
        author = newAuthor(authorname)
        lt.addLast(authors, author)
    lt.addLast(author['books'], book)


def addVideoCategory_id(catalog, categoriavid):
    """
    Adiciona un tag a la lista de tags
    """
    t = newVidcategoria(categoria['id'], categoria['name'])
    lt.addLast(catalog['category-id'], t)

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