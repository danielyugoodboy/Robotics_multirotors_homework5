import numpy as np
import xlrd

def get_datas():
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    data_set = np.zeros((table.nrows-1, table.ncols))
    for r in range(table.nrows-1):
        for c in range(table.ncols):
            data_set[r][c] = float(table.row_values(r+1)[c])
    #print(data_set)
    return data_set

def error_func(q, d, s):
    result = np.kron(np.linalg.inv(q),d)

def main():
    data_set = get_datas()



if __name__ == '__main__':
    file = 'HW5-2.xls'
    gravity = np.array([[0],
                        [0],
                        [-9.81]])
    main()
