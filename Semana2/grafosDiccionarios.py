grafo = {
         "b":"a",
         "c":"a",
         "d":"a",#segudo nivel
         "e":"b",
         "f":"b",
         "h":"c",
         "i":"d",
         "j":"d",
         "k":"e",
         "m":"f",
         "g":"h",
         "l":"j",
         "n":"m",
         "o":"m"
         }

path = []

def buscar (actual, meta):
    path.append(actual)

    if(actual == meta):
        return meta
    
    for hijo,padre in grafo.items():
        if padre == actual:
            ruta = buscar(hijo,meta)

            if ruta:
                return ruta

    path.pop()

    return 0

res = buscar('a','n')
print(path)