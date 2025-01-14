"""
==> 2048 - Game Implementation

==> Author:- Amar kumar 
==> contact:- amarkumar968579691@gmail.com

"""

import random

class GAMECLASS:
    
    _current_status = {
        0: "GAME NOT OVER",
        1: "WON",
        2: "LOST",
        3: "TIE"
    }

    def _addNumber(self, matrix):
        row = random.randint(0, 3)
        col = random.randint(0, 3)

        while matrix[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        
        matrix[row][col] = 2

    def _reverseMatrix(self, matrix):
        newMatrix = []
        for i in range(4):
            newMatrix.append([matrix[i][3 - j] for j in range(4)])
        return newMatrix

    def _transPoseMatrix(self, matrix):       
        return [[matrix[j][i] for j in range(4)] for i in range(4)]

    def _compressMatrix(self, matrix):
        newMatrix = []
        changed = False

        for i in range(4):
            newMatrix.append([0]*4)
         
        for i in range(4):
            pos = 0

            for j in range(4):
                if matrix[i][j] != 0:
                    newMatrix[i][pos] = matrix[i][j]
                    if j != pos:
                        changed = True
                    pos += 1
        
        return newMatrix, changed

    def _mergeMatrix(self, matrix):
        changed = False
         
        for i in range(4):
            for j in range(3):
                if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0:
                    matrix[i][j] *= 2
                    matrix[i][j + 1] = 0
                    changed = True
        return matrix, changed

    def _moveLeft(self, matrix):
        newMatrix, changed1 = self._compressMatrix(matrix)
        newMatrix, changed2 = self._mergeMatrix(newMatrix)
        newMatrix, changed3 = self._compressMatrix(newMatrix)
        changed = changed1 or changed2 or changed3
        return newMatrix, changed

    def _moveRight(self, matrix):
        newMatrix = self._reverseMatrix(matrix)
        newMatrix, changed = self._moveLeft(newMatrix)
        newMatrix = self._reverseMatrix(newMatrix)
        return newMatrix, changed

    def _moveTop(self, matrix):
        newMatrix = self._transPoseMatrix(matrix)
        newMatrix, changed = self._moveLeft(newMatrix)
        newMatrix = self._transPoseMatrix(newMatrix)
        return newMatrix, changed

    def _moveBottom(self, matrix):
        newMatrix = self._transPoseMatrix(matrix)
        newMatrix, changed = self._moveRight(newMatrix)
        newMatrix = self._transPoseMatrix(newMatrix)
        return newMatrix, changed

    def _getCurrentState(self, matrix):
      
        for i in range(4):
            for j in range(4):
                if matrix[i][j] == 2048:
                   return self._current_status[1]

       
        for i in range(4):
            for j in range(4):
                if matrix[i][j] == 0:
                    return self._current_status[0]

       
        for i in range(4):
            for j in range(3):
                if matrix[i][j] == matrix[i][j + 1]:
                    return self._current_status[0]

      
        for i in range(3):
            for j in range(4):
                if matrix[i][j] == matrix[i + 1][j]:
                    return self._current_status[0]

        return self._current_status[2]  
    def _startState(self):
        matrix = [[0]*4 for _ in range(4)]
        self._addNumber(matrix)
        return matrix

    def _displayMatrix(self, matrix):
        for row in matrix:
            print(row)

    def _displayInstruction(self):
        print("Please follow the instructions to enter your next move: ")
        print("Press 1 for move in top direction ")
        print("Press 2 for move in down direction ")
        print("Press 3 for move in left direction ")
        print("Press 4 for move in right direction ")

    def Play(self):
        matrix = self._startState()
        self._displayMatrix(matrix)
        self._displayInstruction()

        try:
            while True:
                while True:
                    try:
                        choice = int(input("Enter your move: "))
                        if choice in [1, 2, 3, 4]:
                            break
                        else:
                            print("Invalid choice. Please enter 1, 2, 3, or 4.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                if choice == 1:
                    newMatrix, flag = self._moveTop(matrix)
                elif choice == 2:
                    newMatrix, flag = self._moveBottom(matrix)
                elif choice == 3:
                    newMatrix, flag = self._moveLeft(matrix)
                elif choice == 4:
                    newMatrix, flag = self._moveRight(matrix)

               
                if flag:
                    matrix = newMatrix
                    self._addNumber(matrix)

               
                currentState = self._getCurrentState(matrix)
                print(currentState)

                
                if currentState != self._current_status[0]:
                    break

             
                self._displayMatrix(matrix)

        except Exception as e:
            print("Game Over! See you again.")
            exit(0)

if __name__ == "__main__":
    print("Welcome! Start Playing 2048 Game")
    app = GAMECLASS()
    app.Play()
