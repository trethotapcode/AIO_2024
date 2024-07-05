import math


def mean_difference_root_error(target, predict, n, p):
    num_samples = (input("Input num of samples: "))
    mean_value = 0
    if num_samples.isnumeric() == True:
        num_samples = int(num_samples)
    else:
        return "num of samples must be an integer!"

    for _ in range(num_samples):
        mean_value = mean_value + (target**(1/n) - predict**(1/n))**p

    mean_value = (1/num_samples) * mean_value
    return mean_value


if __name__ == "__main__":
    print(mean_difference_root_error(100, 99.5, 2, 1))
