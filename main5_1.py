import numpy as np
import xlrd

# x = ((AtA)^-1)AtY
def get_datas():
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    A = np.zeros((table.nrows-1, table.ncols-1))
    Y = np.zeros((table.nrows-1, 1))
    for r in range(table.nrows-1):
        for c in range(table.ncols-1):
            A[r][c] = float(table.col_values(c)[r+1])

    for r in range(table.nrows-1):
        Y[r][0] = float(table.col_values(2)[r+1])

    return A, Y

def linear_opti(A, Y):
    At = np.transpose(A)
    a = np.linalg.inv(np.dot(At, A))
    b = np.dot(At, Y)
    x = np.dot(a, b)

    return x

def main():
    get_datas()
    A, Y = get_datas()
    x = linear_opti(A, Y)
    print('Y = %.1f*X1 + %.1f*X2'%(x[0][0], x[1][0]))

if __name__ == '__main__':
    file = 'HW5-1.xls'
    main()
