import random

class Gato:
    def __init__(self):
        self.tablero = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.turno = random.choice([1,2])

        self.mostrarTablero()
    
    def mostrarTablero(self):
        for i, row in enumerate(self.tablero):
            print(' ' + ' | '.join(row))
            if i < len(self.tablero) - 1:
                print('-----------')

        if not self.checkWinner('X') and not self.checkWinner('O') and not self.checkEmpate():
            self.turnoJugador() if self.turno == 1 else self.turnoMinMax()


    def turnoJugador(self):
        print("Turno Jugador")
        i = input("Ingresar la fila: ")
        j = input("Ingresar la columna: ")

        if not i.isdigit() or not j.isdigit() or int(i) > 2 or int(j) > 2:
            print("Coordenadas no válidas")
            self.turnoJugador()

        i = int(i)
        j = int(j)

        if self.tablero[i][j] != 'X' and self.tablero[i][j] != 'O':
            self.tablero[i][j] = 'X'
            self.turno = 2
            self.mostrarTablero()
        else:
            print("Posición ocupada. Por favor, ingresa una posición válida.")
            self.turnoJugador()


    def turnoMinMax(self):
        state = float('-inf')
        best_move = None

        for i,row in enumerate(self.tablero):
            for j,column in enumerate(row):
                if self.tablero[i][j] != 'X' and self.tablero[i][j] != 'O':
                    self.tablero[i][j] = 'O'
                    puntos = self.min_function()
                    self.tablero[i][j] = ' '

                    if state < puntos:
                        state = puntos
                        best_move = (i,j)

        if(best_move):
            fila,columna = best_move
            self.tablero[fila][columna] = 'O'
            self.turno = 1
            self.mostrarTablero()


    def min_function(self):
        if self.checkWinner('O'):
            return 1
        elif self.checkWinner('X'):
            return -1
        elif self.checkEmpate():
            return 0
        
        min_state = float('inf')

        for i,row in enumerate(self.tablero):
            for j,column in enumerate(row):
                if self.tablero[i][j] != 'X' and self.tablero[i][j] != 'O':
                    self.tablero[i][j] = 'X'
                    puntos = self.max_function()
                    self.tablero[i][j] = ' '

                    min_state = min(min_state, puntos)

        return min_state

    def max_function(self):
        if self.checkWinner('O'):
            return 1
        elif self.checkWinner('X'):
            return -1
        elif self.checkEmpate():
            return 0
        
        max_state = float('-inf')

        for i,row in enumerate(self.tablero):
            for j,column in enumerate(row):
                if self.tablero[i][j] != 'X' and self.tablero[i][j] != 'O':
                    self.tablero[i][j] = 'O'
                    puntos = self.min_function()
                    self.tablero[i][j] = ' '

                    max_state = max(max_state,puntos)

        return max_state

        

    def checkWinner(self,player):
        # Comprobación de filas
        for row in self.tablero:
            if row[0] == row[1] == row[2] == player:
                return True

        # Comprobación de columnas
        for col in range(3):
            if self.tablero[0][col] == self.tablero[1][col] == self.tablero[2][col] == player:
                return True

        # Comprobación de diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == player:
            return True
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == player:
            return True

        return False
    
    def checkEmpate(self):
        for row in self.tablero:
            for cell in row:
                if cell != 'X' and cell != 'O':
                    return False
        return True
        


gato = Gato()