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
import controller
import model
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Buscar los n videos con más LIKES para el nombre de una categoría específica")

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

#Funciones para imprimir los resultados

        

def printResultsReq1(videoList, numberVideos):
    counter = 0
    for video in lt.iterator(result):
        print("Title: ", video["title"], "| Trending date: ", video["trending_date"], "| Channel title", video["channel_title"],
        "| Publish time: ", video["publish_time"], "| Views: ", video["views"], "| Likes: ", video["likes"], "| Dislikes: ", video["dislikes"])
        counter +=1
        if counter == numberVideos:
            break



catalog = {}

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
        answer = controller.loadData(catalog)
        print('Total de libros cargados: ' + str(lt.size(catalog['videos'])))
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")

    elif int(inputs[0]) == 2:
        numberVideos = int(input("Ingrese el número de videos con más views que desea encontrar: "))
        if numberVideos < 1 or numberVideos > lt.size(catalog["videos"]):
            print("Ingrese un entero positivo mayor a 0 y menor a ", lt.size(catalog["videos"]))
        else:
            bestCategory = str(input("Ingrese la categoria de videos que desea consultar: ")).strip().lower()
            result = controller.firstRequirement(catalog, bestCategory)
            printResultsReq1(catalog, numberVideos)

            


    else:
        sys.exit(0)
sys.exit(0)
