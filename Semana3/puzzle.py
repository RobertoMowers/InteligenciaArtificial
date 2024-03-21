from queue import Queue
import time

class SolucionPuzzle:
    def __init__(self,initial_state,goal_state):
        self.path = []
        self.cola = Queue()
        self.initial_state = initial_state
        self.goal_state = goal_state

    def movimientoArriba(self,current_state):
        empty_space = current_state.index(0)
        new_state = current_state[:empty_space-3] + [0] + current_state[empty_space-2:empty_space] + [current_state[empty_space-3]] + current_state[empty_space+1:]
        return new_state

    def movimientoAbajo(self,current_state):
        empty_space = current_state.index(0)
        new_state = current_state[:empty_space] + [current_state[empty_space+3]] + current_state[empty_space+1:empty_space+3] + [0] + current_state[empty_space+4:]
        return new_state
    
    def movimientoDerecha(self,current_state):
        empty_space = current_state.index(0)
        new_state = current_state[:empty_space] + [current_state[empty_space+1]] + [0] + current_state[empty_space+2:]
        return new_state
    
    def movimientoIzquierda(self,current_state):
        empty_space = current_state.index(0)
        new_state = current_state[:empty_space-1] + [0] + [current_state[empty_space-1]] + current_state[empty_space+1:]
        return new_state
    

    def possibleOptions(self,current_state):
        options = {"Arriba": [],"Abajo": [],"Izquierda": [],"Derecha": []}
        empty_space = current_state.index(0)

        if(empty_space % 3 < 2):
            options["Derecha"] = self.movimientoDerecha(current_state)
        if(empty_space % 3 > 0):
            options["Izquierda"] = self.movimientoIzquierda(current_state)
        if(empty_space > 2):
            options["Arriba"] = self.movimientoArriba(current_state)
        if(empty_space < 6):
            options["Abajo"] = self.movimientoAbajo(current_state)

        return(options)


    def solution(self):
        self.cola.put(self.initial_state)

        while(not self.cola.empty()):
            current_state = self.cola.get()
            print(current_state)
            #time.sleep(1)

            if current_state == self.goal_state:
                return self.path 

            options = self.possibleOptions(current_state)
            #print(options)

            for direccion, state in options.items():
                if state not in self.path and state: 
                        self.cola.put(state)


        return "No solution"


                


initial_state = [1,2,3,4,5,6,7,0,8]
goal_state = [1,2,3,4,5,6,7,8,0]
solver = SolucionPuzzle(initial_state, goal_state)
path = solver.solution()
print(path)

