class DictStack:
    def __init__(self) -> None:
        self.__top = -1
        self.__stack = {}

    def is_empty(self) -> bool:
        return self.__top == -1

    def size(self) -> int:
        return self.__top + 1

    def top(self) -> int:
        if (self.is_empty()):
            return None

        return self.__stack[self.__top]

    def clear(self) -> None:
        self.top = -1
        self.__stack = {}

    def push(self, value) -> None:
        self.__top += 1
        self.__stack[self.__top] = value

    def pop(self):
        if (self.is_empty()):
            return None

        top_value = self.__stack[self.__top]
        del self.__stack[self.__top]
        return top_value
