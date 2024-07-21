class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Стек после добавления элементов:", stack)
print("Верхний элемент стека:", stack.peek())
print("Удаление верхнего элемента:", stack.pop())
print("Стек после удаления элемента:", stack)
print("Размер стека:", stack.size())