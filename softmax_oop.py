import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor):
        total = sum(torch.exp(tensor))
        return torch.exp(tensor) / total


class SoftmaxStable(Softmax):
    def __init__(self):
        super().__init__()

    def forward(self, tensor):
        # lấy max value trong tensor
        max_value = torch.max(tensor)

        # trừ mỗi phần tử của tensor cho max value rồi gán lại cho tensor
        tensor = tensor - max_value

        # tính tổng các phần tử e mũ trong tensor mới
        total = sum(torch.exp(tensor))

        # trả về công thức softmax
        return torch.exp(tensor) / total


# test softmax
data = torch.tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)

# test softmax stable
data2 = torch.tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output2 = softmax_stable(data)
print(output2)
