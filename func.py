def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}  # Соответствие закрывающих и открывающих скобок

    for char in s:
        if char in mapping:  # Если символ - это закрывающая скобка
            if not stack:  # Если стек пуст
                return False
            top_element = stack.pop()  # Берем верхний элемент из стека
            if mapping[char] != top_element:  # Сравниваем с соответствующей открывающей скобкой
                return False
        else:
            stack.append(char)  # Если символ - открывающая скобка, добавляем в стек

    return not stack  # Проверяем, пуст ли стек после обработки всей строки


# Примеры использования:
print(is_valid("()"))  # Вывод: True
print(is_valid("()[]{}"))  # Вывод: True
print(is_valid("(]"))  # Вывод: False
print(is_valid("([)]"))  # Вывод: False
print(is_valid("{[]}"))  # Вывод: True
