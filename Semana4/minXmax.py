import tkinter as tk
import random

class Gato:
    def __init__(self,canvas):
        self.canvas = canvas
        self.gato_state = [['','',''],['','',''],['','','']]
        self.tablero = [[None]*3 for _ in range(3)]
        self.turno = random.choice([1,2])

        self.generarTablero()

        if(self.turno == 2):
            self.solutionMinMax()

    def generarTablero(self):
        for i in range(3):
            for j in range(3):
                self.tablero[i][j] = self.canvas.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, outline="black")
                # Agregar el evento de clic para el turno del jugador
                self.canvas.tag_bind(self.tablero[i][j], '<Button-1>', lambda event, x=i, y=j: self.turnoJugador(event, x, y))


    def turnoJugador(self,event,x,y):
        # Verificar si es el turno del jugador y si el cuadro está vacío
        if self.turno == 1 and self.gato_state[x][y] == '':
            self.gato_state[x][y] = 'X'  # Marcar el cuadro con la ficha del jugador
            self.dibujarEnTablero(x, y)  # Dibujar la ficha en el tablero
            if self.checkWinner('X'):
                print("¡Felicidades! ¡Has ganado!")
                return
            elif self.empate():
                print("¡El juego terminó en empate!")
                return
            self.turno = 2  # Cambiar el turno al otro jugador
            self.solutionMinMax()

    def solutionMinMax(self):
        goal_state = float('-inf')
        best_option = None

        for i in range(3):
            for j in range(3):
                if self.gato_state[i][j] == '':
                    self.gato_state[i][j] = '0'
                    puntuaje = self.min_value()
                    self.gato_state[i][j] = ''

                    if puntuaje > goal_state:
                        goal_state = puntuaje
                        best_option = (i, j)

        # Realizamos el mejor movimiento encontrado por el algoritmo Minimax
        if best_option:
            fila, columna = best_option
            self.gato_state[fila][columna] = 'O'
            self.dibujarEnTablero(fila, columna)
        
        self.turno = 1  # Cambiar el turno al otro jugador

    def min_value(self):
        if self.checkWinner('O'):
            return 1
        elif self.checkWinner('X'):
            return -1
        elif self.empate():
            return 0

        worst_state = float('inf')

        for i in range(3):
            for j in range(3):
                if self.gato_state[i][j] == '':
                    self.gato_state[i][j] = 'X' 
                    puntaje = self.max_value()
                    self.gato_state[i][j] = ''

                    worst_state = min(worst_state, puntaje)

        return worst_state

    def max_value(self):
        if self.checkWinner('O'):
            return 1
        elif self.checkWinner('X'):
            return -1
        elif self.empate():
            return 0
        
        best_state = float('-inf')
        for i in range(3):
            for j in range(3):
                if self.gato_state[i][j] == '':
                    self.gato_state[i][j] = 'X' 
                    puntaje = self.min_value()
                    self.gato_state[i][j] = ''

                    best_state = max(best_state, puntaje)

        return best_state

    def checkWinner(self,player):
        pass
        
    def empate(self):
        pass

    def dibujarEnTablero(self,fila,columna):
        color = 'green' if self.turno == 1 else 'red'
        self.canvas.itemconfig(self.tablero[fila][columna], fill=color)
        self.canvas.update()



    

ventana = tk.Tk()
ventana.title("Gato Min-Max")
canvas = tk.Canvas(ventana, width=3 * 100, height=3 * 100)
canvas.pack()

gato = Gato(canvas)

ventana.mainloop()