import math
n_error = "n must be a positive integer!"


def factorial(n):
    '''
    this functions aims calculate factorial of positive integer n.
    n which positive integer need to calculate factorial is the input
    this function return the factorial of n.
    '''

    # special
    if n == 0 or n == 1:
        return 1

    # calculate
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def approx_sin(x, n):
    '''
    this function aims to calculate the sin of x (radian) following Newton biominal.
    x is the input radian and n is numbers to loop approximately.
    this func return to the sin of x.
    '''

    # condition of n.
    if n < 0:
        return n_error

    # calculate
    sin_x = 0
    for i in range(0, n+1):  # i : 0 --> n
        sin_x = sin_x + ((-1)**i)*(x**(2*i+1)/factorial(2*i+1))

    return sin_x


def approx_cos(x, n):
    '''
    this function aims to calculate the cos of x (radian) following Newton biominal.
    x is the input radian and n is numbers to loop approximately.
    this func return to the cos of x.
    '''

    # condition of n.
    if n < 0:
        return n_error

    # khai báo result
    cos_x = 0

    for i in range(n):
        cos_x = cos_x + ((-1)**i)*(x**(2*i)/factorial(2*i))

    return cos_x


def approx_sinh(x, n):
    '''
    this function aims to calculate the sinh of x (radian) following Newton biominal.
    x is the input radian and n is numbers to loop approximately.
    this func return to the sinh of x.
    '''

    # condition of n.
    if n < 0:
        return n_error

    sinh_x = 0

    for i in range(0, n+1):  # i : 0 --> n
        sinh_x = sinh_x + x**(2*i+1)/factorial(2*i+1)

    return sinh_x


def approx_cosh(x, n):
    '''
    this function aims to calculate the cosh of x (radian) following Newton biominal.
    x is the input radian and n is numbers to loop approximately.
    this func return to the cosh of x.
    '''

    # condition of n.
    if n < 0:
        return n_error
    # khai báo result
    cosh_x = 0

    for i in range(n):
        cosh_x = cosh_x + (x**(2*i)/factorial(2*i))

    return cosh_x


if __name__ == "__main__":
    print(approx_sin(x=3.14, n=10))
    print(approx_cos(x=3.14, n=10))
    print(approx_sinh(x=3.14, n=10))
    print(approx_cosh(x=3.14, n=10))
