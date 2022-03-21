eq = [[2, 2, 3, 6],
      [4, 5, 6, 12],
      [7, 8, 10, 20],
      [11, 12, 13, 27]]#the main matrix

va1 = [100, 200, 300, 400]#vector b in Ax=b


def print_mat(ls):#print the matrix
    for i in ls:
        print(f'{i}')
    print('\n')

def print_mul(m1, m2):#print the matrix in multiplivation
    length = len(m1)
    for i in range(length):
        if length % 2 == 0 and length / 2 == i:
            print(f'({m1[i]}) x ({m2[i]}) = ')
            continue
        elif length % 2 == 1 and int(length / 2) == i:
            print(f'({m1[i]}) x ({m2[i]}) = ')
            continue
        print(f'({m1[i]})   ({m2[i]})')
    print('\n')


def matrix_mul(m1, m2):#function that calculate the matrices multiplication result and returns it
    result = []
    print_mul(m1, m2)
    check = any([True for item in m2 if type(item) is list])#check if the second matrix is b vector in Ax=b
    result1 = []
    if check is False:#if b vector
        for i in range(len(m2)):
            result1.append(find_num(m1, m2, i, 0))
        return result1
    else:
        for i in range(len(m1)):
            for j in range(len(m1)):
                result1.append(find_num(m1, m2, i, j))
            result.append(result1)
            result1 = []
        return result


def find_num(m1, m2, row, column):#function to calculate the number in new matrix
    result = 0
    check = any([True for item in m2 if type(item) is list])
    if check is False:
        for i in range(len(m2)):
            result += m1[row][i]*m2[i]
    else:
        for i in range(len(m1)):
            result += m1[row][i]*m2[i][column]
    return result


def make_matrix_unit(ls):#function to make a singletone default matrix
    temp_ls = []
    for i in range(len(ls)):
        temp_ls1 = []
        for j in range(len(ls)):
            if i == j:
                temp_ls1.append(1)
                continue
            temp_ls1.append(0)
        temp_ls.append(temp_ls1)
    return temp_ls


def linear_equation_solving(ls, va):
    column = 0
    row = 0
    for i in range(row, len(ls)-1):#gaussian low elimination
        for j in range(column, len(ls)):
            temp_ls2 = make_matrix_unit(ls)
            if i != j:
                temp_ls2[j][i] = -ls[j][i]
            else:
                temp_ls2[j][i] = 1 / ls[j][i]
            ls = matrix_mul(temp_ls2, ls)
            va = matrix_mul(temp_ls2, va)
            print(print_mat(ls), print_mat(va))
        column += 1
        row += 1
    answer = [0 for i in range(len(va))]#vector of answers
    answer[-1] = va[-1]
    for i in range(len(ls)-2, -1, -1):#loops to find the answers in linear equations system
        for k in range(len(ls)-1, i, -1):
            answer[i] += ls[i][k]*answer[k]
        answer[i] = va[i] - answer[i]
        for j in range(len(ls)-1):
            if i != j:
                ls[i][j] = 0
    return answer

def print_ans(mat):
    [print(f'x{i} = {mat[i]}') for i in range(len(mat))]


eq = linear_equation_solving(eq, va1)
print_ans(eq)

