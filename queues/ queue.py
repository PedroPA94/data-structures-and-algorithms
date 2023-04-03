class Queue:
    def __init__(self) -> None:
        self.__queue = []

    def is_empty(self) -> bool:
        return len(self.__queue) == 0

    def size(self) -> int:
        return len(self.__queue)

    def clear(self) -> None:
        self.__queue = []

    def peek(self):
        return self.__queue[0]

    def enqueue(self, value) -> None:
        self.__queue.append(value)

    def dequeue(self):
        if self.size() == 0:
            return None

        return self.__queue.pop(0)
