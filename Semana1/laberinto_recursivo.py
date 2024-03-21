import tkinter as tk
import time 

def cargar_laberinto(nombre_archivo):
    laberinto = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            laberinto.append(list(linea.strip()))
    return laberinto

def dibujar_laberinto(laberinto):
    for i, fila in enumerate(laberinto):
        for j, celda in enumerate(fila):
            color = 'black' if celda == '#' else 'white' if celda == '.' else 'green' if celda == 'B' else 'red' if celda == 'S' else 'black'
            canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill=color)
            if color == 'green':
                posicion_inicial = (i, j)
            
    i, j = posicion_inicial
    dibujar_personaje(i,j)
    buscar_salida_recursiva(posicion_inicial,False)

def dibujar_personaje(i, j):
    global personaje_id  # Necesario para actualizar la posición del personaje
    personaje_id = canvas.create_oval(j * 20 + 5, i * 20 + 5, (j + 1) * 20 - 5, (i + 1) * 20 - 5, fill='blue')
    canvas.update()
    time.sleep(.2)

def mover_personaje(nueva_posicion):
    global personaje_id  # Necesario para actualizar la posición del personaje
    i, j = nueva_posicion
    canvas.coords(personaje_id, j * 20 + 5, i * 20 + 5, (j + 1) * 20 - 5, (i + 1) * 20 - 5)
    canvas.update()
    time.sleep(.2)

def buscar_salida_recursiva(posicion_actual, salida_bool):
    i, j = posicion_actual
    direcciones = {"arriba": (i-1, j), "abajo": (i+1, j), "izquierda": (i, j-1), "derecha": (i, j+1)}

    if salida_bool:
        return "fin"

    for direccion, nueva_posicion in direcciones.items():
        new_i, new_j = nueva_posicion
        if 0 <= new_i < len(laberinto) and 0 <= new_j < len(laberinto[0]):
            if laberinto[new_i][new_j] == '.':
                print(f"Hay un camino en la dirección {direccion}")
                
                # Marcar la posición como visitada ('x')
                laberinto[new_i][new_j] = 'x'
                
                # Mover el personaje a la nueva posición
                mover_personaje(nueva_posicion)
                
                # Llamada recursiva para explorar la nueva posición
                resultado = buscar_salida_recursiva(nueva_posicion, salida_bool)
                
                # Si se encontró la salida, salir del bucle
                if resultado == "fin":
                    return "fin"
                
                # Deshacer el marcado si se llega aquí (retroceder)
                laberinto[new_i][new_j] = '.'

            elif laberinto[new_i][new_j] == 'S':
                print("¡Hemos encontrado la salida!")
                return "fin"

    
nombre_archivo = './laberinto.txt'
laberinto = cargar_laberinto(nombre_archivo)

root = tk.Tk()
canvas = tk.Canvas(root, width=len(laberinto[0]) * 20, height=len(laberinto) * 20)
canvas.pack()

dibujar_laberinto(laberinto)

root.mainloop()
