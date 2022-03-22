eq = [[-0.2, 10, 50, 13.7],
      [0, 4.9, -6, -1],
      [7, 65.43, 0, 4.678],
      [0, 4.98, -13, -18.99]]#the main matrix

va1 = [6.2, -59, 345, -400]#vector b in Ax=b


def print_mat(ls):#print the matrix
    for i in ls:
        print(f'{i}')
    print('\n')

def ordering_matrix(m1, m2):
    for j in range(len(m1)):
        for i in range(j, len(m1)):
            if abs(m1[i][j]) > abs(m1[j][j]):
                temp_list = m1[j]
                m1[j] = m1[i]
                m1[i] = temp_list
                temp_num = m2[j]
                m2[j] = m2[i]
                m2[i] = temp_num


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
    ordering_matrix(ls, va)
    for i in range(len(ls)):#gaussian low elimination
        for j in range(len(ls)):
            temp_ls2 = make_matrix_unit(ls)
            if i != j:
                temp_ls2[j][i] = -ls[j][i]
            elif ls[j][i] == 0:
                continue
            else:
                if ls[j][i] != 0:
                    temp_ls2[j][i] = 1 / ls[j][i]
            ls = matrix_mul(temp_ls2, ls)
            va = matrix_mul(temp_ls2, va)
            print(print_mat(ls), print_mat(va))
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

