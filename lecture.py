# Мемоїзація

# def fibonacci(n, memo):
#     # Перевіряємо, чи вже обчислювали значення для n
#     if n in memo:
#         return memo[n]
#     # Якщо n менше або дорівнює 2, повертаємо 1 (основні випадки)
#     if n <= 2:
#         return 1
#     # Обчислюємо значення для n як суму двох попередніх значень
#     memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
#     # Повертаємо обчислене значення для n, збережене в memo
#     return memo[n]

# n = 10
# memo = {}
# fib_number = fibonacci(n, memo)
# print(fib_number)


# =========================
# Висхідне динамічне програмування

# def fibonacci_bottom_up(n):
#     # Базові випадки: якщо n дорівнює 0, повертаємо 0
#     if n == 0:
#         return 0
#     # Якщо n дорівнює 1, повертаємо 1
#     elif n == 1:
#         return 1

#     # Ініціалізуємо список для зберігання чисел Фібоначчі до n включно
#     fib_numbers = [0] * (n + 1)
#     # Значення для n = 1 дорівнює 1
#     fib_numbers[1] = 1

#     # Обчислюємо числа Фібоначчі для всіх індексів від 2 до n
#     for i in range(2, n + 1):
#         # Кожне число Фібоначчі є сумою двох попередніх чисел
#         fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]

#     # Повертаємо число Фібоначчі для n
#     return fib_numbers[n]

# # Встановлюємо значення n для обчислення
# n = 10
# # Викликаємо функцію і зберігаємо результат
# fib_number_bottom_up = fibonacci_bottom_up(n)
# # Виводимо результат на екран
# print(fib_number_bottom_up)


# =========================
# Задача про рюкзак

# 1. Предмет 1: вага = 10, вартість = 60
# 2. Предмет 2: вага = 20, вартість = 100
# 3. Предмет 3: вага = 30, вартість = 120
# =========================

# ======== Брудфорс

# Функція для обчислення максимальної вартості
# def knapSack(W, wt, val, n):
#     # Базовий випадок
#     if n == 0 or W == 0:
#         return 0
#     # Якщо вага n-го предмета більше, ніж місткість рюкзака, то цей предмет не можна включити у рюкзак
#     if wt[n - 1] > W:
#         return knapSack(W, wt, val, n - 1)
#     # повертаємо максимум із двох випадків:
#     # (1) n-ий предмет включено
#     # (2) не включено
#     else:
#         return max(
#             val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
#             knapSack(W, wt, val, n - 1),
#         )
# # ваги та вартість предметів
# value = [60, 100, 120]
# weight = [10, 20, 30]
# # місткість рюкзака
# capacity = 50
# # кількість предметів
# n = len(value)
# # викликаємо функцію
# print(knapSack(capacity, weight, value, n))  # 220

# ======== Жадібний алгоритм (відношення вартість/вага )

# class Item:
#     def __init__(self, weight, value):
#         self.weight = weight
#         self.value = value
#         self.ratio = value / weight

# def knapSack(items: list[Item], capacity: int) -> int:
#     items.sort(key=lambda x: x.ratio, reverse=True)
#     total_value = 0
#     for item in items:
#         if capacity >= item.weight:
#             capacity -= item.weight
#             total_value += item.value
#     return total_value

# # Дані предметів
# items = [Item(10, 60), Item(20, 100), Item(30, 120)]
# # Місткість рюкзака
# capacity = 50
# # Виклик функції
# print(knapSack(items, capacity))  # 160

# ======== Динамычне програмування

# def knapSack(W, wt, val, n):
#     # створюємо таблицю K для зберігання оптимальних значень підзадач
#     K = [[0 for w in range(W + 1)] for i in range(n + 1)]

#     # будуємо таблицю K знизу вгору
#     for i in range(n + 1):
#         for w in range(W + 1):
#             if i == 0 or w == 0:
#                 K[i][w] = 0
#             elif wt[i - 1] <= w:
#                 K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
#             else:
#                 K[i][w] = K[i - 1][w]

#     return K[n][W]

# # ваги та вартість предметів
# value = [60, 100, 120]
# weight = [10, 20, 30]
# # місткість рюкзака
# capacity = 50
# # кількість предметів
# n = len(value)
# # виклик функції
# print(knapSack(capacity, weight, value, n))  # 220

# =========================
# Задача про комівояжера

# A: (0, 0),
# B: (1, 5),
# C: (2, 2),
# D: (3, 3),
# E: (5, 1).
# =========================

# Метод повного перебору

# from itertools import permutations
# from math import sqrt

# # Визначити координати для 5 міст
# cities = {"A": (0, 0), "B": (1, 5), "C": (2, 2), "D": (3, 3), "E": (5, 1)}

# # Функція для обчислення відстані між двома містами
# def distance(first_city_name, second_city_name):
#     x1, y1 = cities[first_city_name]
#     x2, y2 = cities[second_city_name]
#     return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# def total_distance_with_return(tour):
#     # Загальна відстань, включаючи повернення до початкової точки
#     return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)) + distance(
#         tour[-1], tour[0]
#     )

# # Знайти найкоротший маршрут
# all_tours = permutations(cities.keys())
# shortest_tour = min(all_tours, key=total_distance_with_return)
# # Переобчислити відстань найкоротшого маршруту з урахуванням зворотного шляху
# shortest_distance_with_return = total_distance_with_return(shortest_tour)

# print(shortest_tour, shortest_distance_with_return)


# =================== Алгоритм Хелда-Карпа

# from math import sqrt
# from itertools import combinations

# def held_karp(distance_matrix):
#     n = len(distance_matrix)
#     # Ініціалізація таблиці динамічного програмування
#     # Та використання кортежів для представлення наборів міст
#     dp = {(frozenset([0, i]), i): (distance_matrix[0][i], [0, i]) for i in range(1, n)}
#     # Встановити базовий випадок - відстань від першого міста до себе дорівнює 0
#     dp[(frozenset([0]), 0)] = (0, [0])

#     # Перебираємо підмножини зростаючого розміру і знаходимо мінімальну відстань до кінцевого міста
#     for r in range(2, n + 1):
#         for subset in combinations(range(1, n), r):
#             subset = frozenset(subset) | frozenset([0])
#             for next_city in subset:
#                 if next_city == 0:
#                     continue
#                 prev_subset = subset - frozenset([next_city])
#                 dp[(subset, next_city)] = min(
#                     (
#                         dp[(prev_subset, last_city)][0]
#                         + distance_matrix[last_city][next_city],
#                         dp[(prev_subset, last_city)][1] + [next_city],
#                     )
#                     for last_city in prev_subset
#                     if last_city != 0
#                 )

#     # Знаходимо мінімальну вартість, щоб завершити тур і повернутися до початкового міста
#     all_cities = frozenset(range(n))
#     result = min(
#         (
#             dp[(all_cities, last_city)][0] + distance_matrix[last_city][0],
#             dp[(all_cities, last_city)][1] + [0],
#         )
#         for last_city in range(1, n)
#     )

#     return result

# # Функція для обчислення відстані між двома точками
# def calculate_distance(coord1, coord2):  
#     return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# if __name__ == '__main__':

#     # Словник із координатами міст
#     cities = {"A": (0, 0), "B": (1, 5), "C": (2, 2), "D": (3, 3), "E": (5, 1)}

#     # Створення матриці відстаней
#     distance_matrix = []
#     for i, source in enumerate(cities.values()):
#         distance_matrix.append([])
#         for target in cities.values():
#             # Додавання розрахованої відстані до матриці
#             distance_matrix[i].append(calculate_distance(source, target))

#     # Виклик функції алгоритму з матрицею відстаней
#     result, path = held_karp(distance_matrix)
#     print(result, path)
#     # Переводимо шлях від індексів до назв міст
#     city_names = list(cities.keys())
#     path_with_names = [city_names[i] for i in path]

#     print(result, path_with_names)



# =================== Алгоритм Флойда-Воршала

# def floyd_warshall(graph):
#     # Кількість вершин у графі
#     n = len(graph)
    
#     # Ініціалізація матриці відстаней
#     distance = [[float('inf')] * n for _ in range(n)]
    
#     # Заповнення діагоналі нулями (відстань від вершини до самої себе)
#     for i in range(n):
#         distance[i][i] = 0
    
#     # Заповнення матриці відстаней вагами ребер
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] != 0:
#                 distance[i][j] = graph[i][j]
    
#     # Оновлення матриці відстаней
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
#     return distance

# # матриця суміжності, де 0 означає відсутність ребра між вершинами
# graph = [
#     [0, 3, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 7, 0, 2],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 2, 0, 3],
#     [0, 0, 0, 0, 0, 0]
# ]

# distance_matrix = floyd_warshall(graph)
# for row in distance_matrix:
#     print(row)



# =================== Алгоритм Краскала

# import networkx as nx

# # Функція для побудови Мінімального Остовного Дерева за алгоритмом Краскала
# def kruskal_mst(graph):
#     # Створюємо ліс, кожне дерево якого є окремою вершиною графа
#     forest = nx.Graph()
#     for node in graph.nodes():
#         forest.add_node(node)

#     # Сортування ребер графа за вагою в порядку зростання
#     sorted_edges = sorted(graph.edges(data=True), key=lambda t: t[2].get('weight', 1))

#     # Мінімальне остовне дерево
#     mst = nx.Graph()

#     # Додаємо ребра до МОД з урахуванням того, що додавання ребра не формує циклу
#     for edge in sorted_edges:
#         u, v, weight  = edge
#         # Якщо u та v знаходяться в різних компонентах зв'язності, додаємо ребро
#         if not nx.has_path(forest, u, v):
#             forest.add_edge(u, v)
#             mst.add_edge(u, v, weight=weight['weight'])

#     return mst

# # Створення зваженого графа
# G = nx.Graph()
# G.add_edge('A', 'B', weight=7)
# G.add_edge('A', 'D', weight=5)
# G.add_edge('B', 'C', weight=8)
# G.add_edge('B', 'D', weight=9)
# G.add_edge('B', 'E', weight=7)
# G.add_edge('C', 'E', weight=5)
# G.add_edge('D', 'E', weight=15)
# G.add_edge('D', 'F', weight=6)
# G.add_edge('E', 'F', weight=8)
# G.add_edge('E', 'G', weight=9)
# G.add_edge('F', 'G', weight=11)

# # Побудова мінімального остовного дерева за допомогою алгоритму Краскала
# mst = kruskal_mst(G)

# # Вивід ребер МОД
# print("Edges in the MST:")
# for edge in mst.edges(data=True):
#     print(edge)


# =================== Алгоритм Прима

# from heapq import heappush, heappop

# import networkx as nx

# def prim_mst(graph):
#     # Створення порожнього МОД
#     mst = nx.Graph()

#     # Відвідані вершини, починаючи з випадкової початкової вершини
#     visited = {list(graph.nodes())[0]}

#     # Черга з пріоритетами для ребер, яка ініціалізується ребрами початкової вершини
#     edges = []
#     for _, v, weight in graph.edges(data='weight', nbunch=visited):
#         heappush(edges, (weight, _, v))

#     # Поки в МОД не всі вершини
#     while visited != set(graph.nodes()):
#         # Вибираємо ребро з найменшою вагою, що з'єднує дерево з новою вершиною
#         weight, u, v = heappop(edges)
#         if v not in visited:
#             # Додаємо нову вершину до МОД
#             visited.add(v)
#             mst.add_edge(u, v, weight=weight)
#             # Додаємо всі ребра з нової вершини до черги з пріоритетами
#             for _, new_v, new_weight in graph.edges(data='weight', nbunch=[v]):
#                 if new_v not in visited:
#                     heappush(edges, (new_weight, v, new_v))

#     return mst

# # Створення графа для демонстрації
# G = nx.Graph()
# G.add_edge('A', 'B', weight=7)
# G.add_edge('A', 'D', weight=5)
# G.add_edge('B', 'C', weight=8)
# G.add_edge('B', 'D', weight=9)
# G.add_edge('B', 'E', weight=7)
# G.add_edge('C', 'E', weight=5)
# G.add_edge('D', 'E', weight=15)
# G.add_edge('D', 'F', weight=6)
# G.add_edge('E', 'F', weight=8)
# G.add_edge('E', 'G', weight=9)
# G.add_edge('F', 'G', weight=11)

# # Виконання алгоритму Прима на графі G
# mst = prim_mst(G)

# # Виведення ребер мінімального остовного дерева
# print("Edges in the MST:")
# for edge in mst.edges(data=True):
#     print(edge)

