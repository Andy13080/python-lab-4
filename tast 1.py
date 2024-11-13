
items = {
    'r': ('Винтовка', 3, 25),
    'p': ('Пистолет', 2, 15),
    'a': ('Боекомплект', 2, 15),
    'm': ('Аптечка', 2, 20),
    'i': ('Ингалятор', 1, 5),
    'k': ('Нож', 1, 15),
    'x': ('Топор', 3, 20),
    't': ('Оберег', 1, 25),
    'f': ('Фляжка', 1, 15),
    'd': ('Антидот', 1, 10),
    's': ('Еда', 2, 20),
    'c': ('Арбалет', 2, 20)
}


max_capacity = 2 * 4


current_survival_points = 20
has_asthma = False
has_infection = True


survival_matrix = [[0 for _ in range(max_capacity + 1)] for _ in range(len(items) + 1)]


for i, item in enumerate(items.values()):
    symbol, size, points = item
    for capacity in range(max_capacity + 1):
        if size > capacity:
            survival_matrix[i + 1][capacity] = survival_matrix[i][capacity]
        else:
            survival_matrix[i + 1][capacity] = max(
                survival_matrix[i][capacity],
                survival_matrix[i + 1][capacity - size] + points
            )


selected_items = []
capacity = max_capacity
for i in range(len(items), 0, -1):
    if survival_matrix[i][capacity] != survival_matrix[i - 1][capacity]:
        selected_items.append(list(items.keys())[i - 1])
        capacity -= items[selected_items[-1]][1]

inventory = [selected_items[i:i+4] for i in range(0, len(selected_items), 4)]


if 'i' not in selected_items and has_asthma:
    selected_items.append('i')
if 'd' not in selected_items and has_infection:
    selected_items.append('d')


print("Ивентарь:")
for row in inventory:
    print(row)
print(f"Итоговые очки выживания: {survival_matrix[len(items)][max_capacity]}")