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
               'categoryIds': None,
               'categoryNames' : None}
    catalog["videos"] = lt.newList('SINGLE_LINKED', cmpVideoIds)

    catalog["categoryIds"]= mp.newMap(67, maptype='PROBING',loadfactor=0.5,comparefunction=cmpCategoryIds)

    catalog["categoryNames"]=mp.newMap(67, maptype='PROBING',loadfactor=0.5,comparefunction=cmpCategoryNames)
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog["videos"], video)
    if mp.contains(catalog["categoryIds"], int(video["category_id"])):
        addVideoToCategory(catalog,video,video["category_id"])
    else:
        addCategoryId(catalog, video["category_id"])
        addVideoToCategory(catalog,video,video["category_id"])
    
def addVideoToCategory(catalog, video, categoryId):
    vidsInCategory = {}
    vidsInCategory = mp.get(catalog['categoryIds'],categoryId)
    videoList = vidsInCategory["value"]
    lt.addLast(videoList, video)
    mp.put(catalog['categoryIds'],categoryId, videoList)


def addCategoryId(catalog, categoryId):
    newCategoryId = lt.newList(datastructure='SINGLE_LINKED')
    mp.put(catalog["categoryIds"], categoryId, newCategoryId)



def addCategory(catalog, category):
    t = newCategory(category['id'], category['name'])
    mp.put(catalog["categoryNames"], t["name"].lower(), t["id"])


# Funciones para creacion de datos

def newCategory(category_id,name):
    category = {'id': int(category_id), 'name': name.strip()}
    return category

# Funciones de consulta

def firstRequirement(catalog, bestCategoryId):
    if mp.contains(catalog["categoryIds"],bestCategoryId):
        videosCategory= mp.get(catalog["categoryIds"],bestCategoryId)
        return videosCategory["value"]
    else:
        return -1

def findCategoryId(catalog, categoryName):
    categoryName.strip()
    if mp.contains(catalog["categoryNames"], categoryName):
        categoryId = mp.get(catalog["categoryNames"], categoryName)
        return categoryId["value"]
    else:
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
        return 0

        
def cmpMapCountries(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0



# Funciones de ordenamiento
