import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    print("Создаем случайную матрицу (10x3):")
    matrix = np.random.rand(10, 3)
    print(matrix)

    print("\nСоздаем экземпляр LinearRegression:")
    model = LinearRegression()
    print(model)

    print("\nHello from a containerized ML app!")

if __name__ == '__main__':
    main()
