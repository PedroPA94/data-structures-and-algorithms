class Deque:
    def __init__(self) -> None:
        self.__deque = []

    def is_empty(self) -> bool:
        return len(self.__deque) == 0

    def size(self) -> int:
        return len(self.__deque)

    def clear(self) -> None:
        self.__deque = []

    def peek_front(self):
        return self.__deque[0]

    def peek_back(self):
        return self.__deque[-1]

    def add_front(self, value) -> None:
        if self.is_empty():
            self.__deque.append(value)
        else:
            self.__deque.insert(0, value)

    def add_back(self, value) -> None:
        self.__deque.append(value)

    def remove_front(self):
        if self.size() == 0:
            return None

        return self.__deque.pop(0)

    def remove_back(self):
        if self.size() == 0:
            return None

        return self.__deque.pop()
