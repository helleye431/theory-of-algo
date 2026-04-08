from collections import deque


def check(sample_count, pair_data):
    # 1 = same, 0 = different
    same_graph = [[] for _ in range(sample_count)]
    pairs = []

    for left, right, relation in pair_data:
        left -= 1
        right -= 1
        is_different = relation == 0
        pairs.append((left, right, is_different))

        if not is_different:
            same_graph[left].append(right)
            same_graph[right].append(left)

    component = [-1] * sample_count
    component_count = 0

    for start in range(sample_count):
        if component[start] != -1:
            continue

        queue = deque([start])
        component[start] = component_count

        while queue:
            current = queue.popleft()
            for neighbor in same_graph[current]:
                if component[neighbor] == -1:
                    component[neighbor] = component_count
                    queue.append(neighbor)

        component_count += 1

    different_graph = [[] for _ in range(component_count)]

    for left, right, is_different in pairs:
        if not is_different:
            continue

        left_component = component[left]
        right_component = component[right]

        if left_component == right_component:
            return 'NO'

        different_graph[left_component].append(right_component)
        different_graph[right_component].append(left_component)

    color = [-1] * component_count

    for start in range(component_count):
        if color[start] != -1:
            continue

        queue = deque([start])
        color[start] = 0

        while queue:
            current = queue.popleft()
            for neighbor in different_graph[current]:
                if color[neighbor] == -1:
                    color[neighbor] = color[current] ^ 1
                    queue.append(neighbor)
                elif color[neighbor] == color[current]:
                    return 'NO'

    return 'YES'


sample_count = 5
pair_data = [
    (1, 2, 1),
    (2, 3, 1),
    (3, 4, 0),
    (4, 5, 1),
]

print(check(sample_count, pair_data))
