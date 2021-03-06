# ========= Utils ==========
def mul(arr):
    r = 1
    for el in arr:
        r *= el
    return r


# ==========================


class Pstate:
    # Ф-ія ймовірності знаходження системи в певному стані

    def __init__(self, P):
        self.P = P
        self.Q = [1 - pi for pi in P]

    def __call__(self, s):
        return mul([
            self.P[i] if si == 1 else self.Q[i]
            for i, si in enumerate(s)
        ])


class ExistPath:
    # Ф-ія існування шляху між вершинами графа через множину проміжних вершин

    def __init__(self, graph):
        self.graph = graph

    def __call__(self, *, from_, to_, through):
        for v in self.graph[from_]:
            if v == to_:
                return True
            if v in through:
                through_ = [vertex for vertex in through if vertex != v]
                if self(from_=v, to_=to_, through=through_):
                    return True
        return False


def get_state(i, n):
    return [1 if i & (1 << k) else 0 for k in range(n)]


class Workable:
    # Ф-ія працездатності стану

    def __init__(self, graph, start_index, end_index):
        self.start_index = start_index
        self.end_index = end_index
        self.exist_path = ExistPath(graph)

    def __call__(self, s):
        through = [i + 1 for i, si in enumerate(s) if si == 1]
        return self.exist_path(
            from_=self.start_index,
            to_=self.end_index,
            through=through
        )


# ========= Дані за варіантом ===========

n = 7  # Кількість вершин

# Граф зв'язності системи
start_index = 0
end_index = n + 1

E = {
    0: [1],  # start
    1: [0, 2],  # 1
    2: [1, 3, 4],  # 2
    3: [2, 4, 5, 7],  # 3
    4: [2, 3, 6, 7, 8],  # 4
    5: [3, 6, 7],  # 5
    6: [4, 5, 7, 8],  # 6
    7: [3, 5, 4, 6, 8],  # 7
    8: [4, 6, 7,],  # 8
    }

# Ймовірності безвідмовної роботи елементів
P = [
    0.80,  # 1
    0.42,  # 2
    0.72,  # 3
    0.30,  # 4
    0.60,  # 5
    0.79,  # 6
    0.70,  # 7
]

# ==========================================

# =========== Підготовка основних ф-ій =============
workable = Workable(E, start_index, end_index)
p_state = Pstate(P)
# ==================================================

# ================== Виконання завдання ======================

# Перебір всіх можливих станів системи 
all_states = [get_state(i, n) for i in range(2 ** n)]
# Вибірка лише працездатних станів
workable_states = [*filter(workable, all_states)]
print(len(workable_states))
# Обрахукнок ймовірності безвідмовної роботи
p_system = sum([p_state(s) for s in workable_states])
# Вивід результатів
print("Ймовірність безвідмовної роботи системи:", p_system)

# ============================================================