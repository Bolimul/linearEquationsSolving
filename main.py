eq = [[0.04, 0.01, -0.01],
     [0.2, 0.5, -0.2],
     [1, 2, 4]]#the main matrix

va1 = [0.06, 0.3, 11]#vector b in Ax=b


def print_mat(ls):#print the matrix
    for i in ls:
        print(f'{i}')
    print('\n')

def absolute(num):
    if num < 0:
        return -num
    return num

def ordering_matrix(m1, m2):
    for j in range(len(m1)):
        for i in range(j, len(m1)):
            if absolute(m1[i][j]) > absolute(m1[j][j]):

                temp_list = make_matrix_unit(m1)
                temp_list1 = temp_list[j]
                temp_list[j] = temp_list[i]
                temp_list[i] = temp_list1
                m1 = matrix_mul(temp_list, m1)
                print_mat(m1)
                m2 = matrix_mul(temp_list, m2)
                print_mat(m2)


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
                temp_ls1.append(1.0)
                continue
            temp_ls1.append(0.0)
        temp_ls.append(temp_ls1)
    return temp_ls


def linear_equation_solving(ls, va):
    ordering_matrix(ls, va)
    for i in range(len(ls)):#gaussian low elimination
        for j in range(i, len(ls)):
            temp_ls2 = make_matrix_unit(ls)
            if i != j:
                temp_ls2[j][i] = -ls[j][i]
            elif ls[j][i] == 0:
                continue
            else:
                if ls[j][i] != 0:
                    temp_ls2[j][i] = 1 / ls[j][i]
            print("Printing multiplication for matrix A")
            ls = matrix_mul(temp_ls2, ls)
            print('Answer for matrix A')
            print_mat(ls)
            print("Printing multiplication for vector b")
            va = matrix_mul(temp_ls2, va)
            print('Answer for vector b')
            print_mat(va)
    for j in range(len(ls)):#upper elimination
        for i in range(j+1, len(ls)):
            temp_ls2 = make_matrix_unit(ls)
            if i != j:
                temp_ls2[j][i] = -ls[j][i]
            elif ls[j][i] == 0:
                continue
            else:
                if ls[j][i] != 0:
                    temp_ls2[j][i] = 1 / ls[j][i]
            print("Printing multiplication for matrix A")
            ls = matrix_mul(temp_ls2, ls)
            print('Answer for matrix A')
            print_mat(ls)
            print("Printing multiplication for vector b")
            va = matrix_mul(temp_ls2, va)
            print('Answer for vector b')
            print_mat(va)
    return va


def print_ans(mat):
    [print(f'x{i+1} = {mat[i]}') for i in range(len(mat))]


eq = linear_equation_solving(eq, va1)
print_ans(eq)

