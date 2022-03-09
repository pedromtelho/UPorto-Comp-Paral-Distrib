import time
import numpy as np

class MatrixProblem():
    def __init__(self, lin, col):
        self.lin = lin
        self.col = col
        self.matrixA = np.zeros(lin * col)
        self.matrixB = np.zeros(lin * col)
        

    def fill_matrix(self):
        for i in range(0, self.lin):
            for j in range(0, self.col):
                self.matrixA[i * self.lin + j] = 1
                self.matrixB[i * self.col + j] = i + 1
    
    def mult(self):
        print("\nMultiplication algorithm:\n")
        matrixC = np.zeros(self.lin * self.col)
        t0 = time.time()
        for i in range(0, self.lin):
            for j in range(0, self.col):
                temp = 0
                for k in range(0, self.lin):
                    temp += self.matrixA[i * self.lin + k] * self.matrixB[k * self.col + j]
                matrixC[i * self.lin + j] = temp
        tf = time.time()
        print("Total time: ", tf - t0)
        print(matrixC[0:10])
        return
    
    def line_mult(self):
        print("\nLine multiplication algorithm:\n")
        matrixC = np.zeros(self.lin * self.col)
        t0 = time.time()
        for i in range(0, self.lin):    
            for k in range(0, self.lin):
                for j in range(0, self.col):
                    matrixC[i * self.lin + j] += self.matrixA[i * self.lin + k] * self.matrixB[k * self.col + j]
        tf = time.time()
        print("Total time: ", tf - t0)
        print(matrixC[0:10])
        return


if __name__ == "__main__":
    selection = int(input("\n1. Multiplication\n2. Line Multiplication\n3. Block Multiplication\n"))
    data_input = int(input("lin X cols: "))
    matrix_object = MatrixProblem(data_input, data_input)
    matrix_object.fill_matrix()

    if selection == 1:
        matrix_object.mult()
    if selection == 2:
        matrix_object.line_mult()
    
