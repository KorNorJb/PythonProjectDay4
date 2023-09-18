data = ['Roy', 43, 4343, 'Arif', 43, 'Dima', 39, 'Krissanto', 88]
print(data)
new = tuple(reversed(data))
print(new)
new = len(new)
print(f'This tuple contains {new} elements')