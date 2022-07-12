class Queue:
    def __init__(self):
        self.__queue = []
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        self.__queue.append(value)
        self.__length += 1

    def dequeue(self):
        self.__length -= 1
        return self.__queue.pop(0)

    def search(self, index):
        if index not in range(self.__length):
            raise(IndexError)
        return self.__queue[index]
