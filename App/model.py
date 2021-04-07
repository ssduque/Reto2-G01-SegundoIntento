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
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'videos': None,
               'categoryVideos': None,
               'categoryNames' : None}
    catalog["videos"] = lt.newList('SINGLE_LINKED', cmpVideoIds)

    catalog["categoryVideos"]= mp.newMap(67, maptype='PROBING',loadfactor=0.8,comparefunction=cmpCategoryIds)

    catalog["categoryNames"]= lt.newList(datastructure='ARRAY_LIST')
    return catalog

# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    lt.addLast(catalog["videos"], video)
    addVideoToCategory(catalog, int(video["category_id"]), video)


def addVideoToCategory(catalog, categoryId, video):
    categoryVideos = catalog["categoryVideos"]
    existCategory = mp.contains(categoryVideos, int(categoryId))
    if existCategory:
        entry = mp.get(categoryVideos, categoryId)
        category = me.getValue(entry)
    else:
        category = newCategoryVideos(int(categoryId))
        mp.put(categoryVideos, int(categoryId), category)
    lt.addLast(category["videos"], video)


def addCategory(catalog, category):
    t = newCategory(category['id'], category['name'])
    lt.addLast(catalog['categoryNames'], t)


# Funciones para creacion de datos


def newCategory(categoryId,name):
    category = {'id': int(categoryId), 'name': name.strip()}
    return category


def newCategoryVideos(categoryId):
    category = {"categoryId": 0, "videos": None}
    category["categoryId"] = int(categoryId)
    category["videos"] = lt.newList("SINGLE_LINKED", cmpCategoryIds)
    return category


# Funciones de consulta


def firstRequirement(catalog, bestCategoryId):
    videosCategory= mp.get(catalog["categoryVideos"],int(bestCategoryId))
    if videosCategory:
        return me.getValue(videosCategory)["videos"]
    return -2


def findCategoryid(catalog, category):
    for cat in lt.iterator(catalog["categoryNames"]):
        if (cat["name"].strip().lower() == category.strip().lower()):
            return cat["id"]
    return -1


# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideoIds(id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def cmpCategoryIds(id, catid):
    catentry = me.getKey(catid)
    if (int(id) == int(catentry)):
        return 0
    elif (int(id) > int(catentry)):
        return 1
    else:
        return 0


def cmpCategoryNames(name,catname):
    nameEntry = me.getKey(catname)
    if name.strip()==nameEntry.strip():
        return 0
    elif name.strip() > nameEntry.strip():
        return 1
    else:
        return -1

        
def cmpMapCountries(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return -1


def cmpVideosByLikes(video1, video2):
    if float(video1['likes']) < float(video2['likes']):
        return False
    else:
        return True

def cmpVideosByViews(video1, video2):
    if float(video1['views']) < float(video2['views']):
        return False
    else:
        return True

# Funciones de ordenamiento

def mergeSortBylikes(videoList):
    sortedList = merge.sort(videoList, cmpVideosByLikes)
    return sortedList

def mergeSortByViews(videoList):
    sortedList = merge.sort(videoList, cmpVideosByViews)
    return sortedList