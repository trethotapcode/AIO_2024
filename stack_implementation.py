class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def pop(self):
        return self.__stack.pop(-1)

    def push(self, element):
        self.__stack.append(element)

    def top(self):
        return self.__stack[-1]


# test case 1
stack1 = MyStack(capacity=5)

stack1.push(1)
stack1.push(2)

print(stack1.is_full())

print(stack1.top())
print(stack1.pop())

print(stack1.top())
print(stack1.pop())


print(stack1.is_empty())
