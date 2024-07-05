import math

# given check_number_function


def is_number(n):
    try:
        float(n)    # Type - casting the string to ‘float ‘.
        # If string is not a valid ‘float ‘ ,
        # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


def calculate_activation_function():
    '''
    this function aims to implement and calculate threes activate function: logistic function, ReLU function, ELU function.
    this function return values of function which input is x and type of activate function.
    '''

    # nhap input
    x = input("Input x = ")

    activation_function = input(
        "Input activation Function ( sigmoid | relu | elu ) :")

    # kiểm tra input
    if is_number(x) == False:
        return "x must be a number"

    if activation_function not in ["sigmoid", "relu", "elu"]:
        return f"{activation_function} is not supported"

    # thực hiện công thức theo từng hàm kích hoạt

    alpha = 0.01
    x = float(x)

    if (activation_function == "sigmoid"):

        result = 1/(1 + math.e ** (-x))
        return f"sigmoid: f({x}) = {result}"

    if (activation_function == "relu"):

        if x > 0:
            result = x
        else:
            result = 0

        return f"relu: f({x}) = {result}"

    if (activation_function == "elu"):

        if x > 0:
            result = x
        else:
            result = alpha*(math.e**x-1)

        return f"relu: f({x}) = {result}"


# main_function
if __name__ == "__main__":

    print(calculate_activation_function())
