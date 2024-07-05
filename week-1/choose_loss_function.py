import math
import random


def loss_function():
    '''
    this function aims to calculate value of regression lost function.
    function has inputs num_samples and loss_name. 
    this function returns result is value of threes function: MAE, MSE, RMSE.
    '''

    # khai báo input
    num_samples = input(
        "Input number of samples (integer number) which are generated: ")
    loss_name = input("Input loss name: ")

    # kiểm tra tính hợp lệ của num_samples

    if num_samples.isnumeric() == True:
        num_samples = int(num_samples)
    else:
        return print("number of samples must be an integer number.")

    # implement function
    if (loss_name == "MAE"):
        for i in range(0, num_samples):
            mae_result = 0
            predict = random.uniform(0, 10)
            target = random.uniform(0, 10)
            mae_result += abs(target-predict)
            print(f"loss name: {loss_name}, sample : {i}, pred: {
                predict}, target: {target}, loss: {mae_result} ")

        mean_mae_result = (1/num_samples)*mae_result
        print("final MAE: ", mean_mae_result)

    if (loss_name == "MSE"):
        for i in range(0, num_samples):
            mse_result = 0
            predict = random.uniform(0, 10)
            target = random.uniform(0, 10)
            MSE_result += abs(target-predict)**2
            print(f"loss name: {loss_name}, sample : {i}, pred: {
                predict}, target: {target}, loss: {mse_result} ")

        mean_mse_result = (1/num_samples)*mse_result
        print("final MSE: ", mean_mse_result)

    if (loss_name == "RMSE"):
        for i in range(0, num_samples):
            rmse_result = 0
            predict = random.uniform(0, 10)
            target = random.uniform(0, 10)
            rmse_result += abs(target-predict)**2
            print(f"loss name: {loss_name}, sample : {i}, pred: {
                predict}, target: {target}, loss: {rmse_result} ")

            mean_rmse_result = math.sqrt((1/num_samples)*rmse_result)
            print("final RMSE:", mean_rmse_result)


if __name__ == "__main__":
    loss_function()
