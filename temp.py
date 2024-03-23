def flood_fill(image, x, y, target_color, replacement_color):
    if image[y][x] != target_color:
        return

    rows, cols = len(image), len(image[0])
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        image[y][x] = replacement_color

        # Check neighboring pixels
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for nx, ny in neighbors:
            if 0 <= nx < cols and 0 <= ny < rows and image[ny][nx] == target_color:
                stack.append((nx, ny))

# Приклад використання:
image = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

print("Початкове зображення:")
for row in image:
    print(row)

flood_fill(image, 2, 2, 0, 2)  # Заповнюємо область з початковою точкою (2, 2) кольором 2

print("\nЗображення після застосування алгоритму зафарбування:")
for row in image:
    print(row)
