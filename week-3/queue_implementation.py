class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    # xóa giá trị đầu tiên
    def dequeue(self):
        return self.__queue.pop(0)

    # thêm giá trị cuối cùng
    def enqueue(self, element):
        self.__queue.append(element)

    # lấy giá trị first element
    def front(self):
        return self.__queue[0]


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())

print(queue1.front())
print(queue1.dequeue())

print(queue1.front())
print(queue1.dequeue())

print(queue1.is_empty())
