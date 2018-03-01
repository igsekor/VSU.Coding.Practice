import sys


def f(x):
    return x ** 2


def draw_matrix(m):
    """Function for printing matrix of chars"""
    for i in range(len(m)):
        out_string = ""
        for j in range(len(m[i])):
            out_string += m[i][j]
        print(out_string)


def is_matrix_rows_equal(m) -> bool:
    """Function for checking if all rows are equal"""
    is_equal = True
    for i in range(len(m)):
        if len(m[i]) != len(m[0]):
            is_equal = False
    return is_equal


def transpose_matrix_element(m, i, j) -> str:
    """Function for getting values of transposing matrix"""
    return m[j][i]


def transposed_matrix(m) -> []:
    """Function for getting of transposed matrix"""
    if is_matrix_rows_equal(m):
        t = []
        for i in range(len(m[0])):
            t.append([])
            for j in range(len(m)):
                t[i].append(transpose_matrix_element(m, i, j))
            t[i] = tuple(t[i])
        return t
    else:
        print("List has rows with different length")
        return None


def reverse_rows(m) -> []:
    """Remove all rows in reverse order"""
    t = []
    for i in range(len(m) - 1, -1, -1):
        t.append(m[i])
    return t


def draw_function(func, min_x, max_x, n_x, n_y, a_type=0, point_char="*", empty_char=" "):
    """Function draws plot in different projection"""
    min_y, max_y = sys.maxsize, -sys.maxsize
    dx = (max_x - min_x) / n_x
    x = []
    y = []

    # Calculation of all values
    for i in range(n_x):
        x.append(min_x + dx * i)
        y.append(func(x[i]))
        if y[i] > max_y:
            max_y = y[i]
        if y[i] < min_y:
            min_y = y[i]

    # Creating the matrix of points
    dy = (max_y - min_y) / n_y
    m = []
    for i in range(n_x):
        m.append([])
        for j in range(n_y):
            y_below = min_y + dy * j
            y_above = min_y + dy * (j + 1)
            if y_above > y[i] >= y_below:
                m[i].append(point_char)
            else:
                m[i].append(empty_char)

    # Drawing the plot
    if a_type == 0:
        # Horizontal Y axe (Algorithm 1)
        draw_matrix(m)
    elif a_type == 1:
        # Horizontal X axe (Algorithm 2)
        draw_matrix(reverse_rows(transposed_matrix(m)))


draw_function(f, -10, 10, 60, 60, 1)
