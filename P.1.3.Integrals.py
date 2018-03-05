def integral_square(func, a, b, n):
    """Calcuting integral of the function by square formula

    integral_square(func, a, b, n)

    func - function for integration
    a - first edge (left)
    b - second edge (right)
    n - count of squares (steps)"""
    dx = (b - a) / n
    S = 0
    for i in range(n):
        x_i = a + i * dx
        x_j = a + (i + 1) * dx
        f_i = func(x_i)
        S += f_i * (x_j - x_i)
    return S

def integral_trapeze(func, a, b, n):
    """Calcuting integral of the function by trapeze formula

    integral_square(func, a, b, n)

    func - function for integration
    a - first edge (left)
    b - second edge (right)
    n - count of squares (steps)"""
    dx = (b - a) / n
    S = 0
    for i in range(n):
        x_i = a + i * dx
        x_j = a + (i + 1) * dx
        f_i = func(x_i)
        f_j = func(x_j)
        S += 0.5 * (f_i + f_j) * (x_j - x_i)
    return S

