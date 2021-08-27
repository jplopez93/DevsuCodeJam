import re

def searchEngine(query= None, elements=None):
    query = "cartoon"
    elements=["car", "cartouches", "carpet", "cartoonist", "carrot", "cared", "carton","captain", "cartoon", "carter"]
    elements.sort()
    lista_resultados = []
    lista_encontrados = []
    contador_lista = 0
    contador_query = 1
    xx = query[0:contador_query]
    for items in range(0,len(query)*len(query)):
        if len(lista_resultados) == 5:
            break
        if len(lista_encontrados) == 3:
            lista_encontrados = []
        
        for word in elements:
            if len(lista_encontrados) != 3:
                
                resultado = re.search(f"^{query[0:contador_query]}",word)
                if resultado == None:
                    pass
                if resultado != None:
                    lista_encontrados.append(word)
                    contador_query +=1
                
            if len(lista_encontrados) > 3:
                lista_encontrados = []
            else:
                continue
        lista_resultados.append(sorted(lista_encontrados))

    return print(sorted(lista_resultados))
searchEngine()

        