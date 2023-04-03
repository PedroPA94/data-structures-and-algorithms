class ListStack:
    def __init__(self) -> None:
        self.__stack = []

    def is_empty(self) -> bool:
        return len(self.__stack) == 0

    def size(self) -> int:
        return len(self.__stack)

    def top(self) -> int:
        if (self.is_empty()):
            return None

        return self.__stack[-1]

    def clear(self) -> None:
        self.__stack = []

    def push(self, value) -> None:
        self.__stack.append(value)

    def pop(self):
        if (self.is_empty()):
            return None

        return self.__stack.pop()
