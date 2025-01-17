def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    previous_nodes = {node: None for node in graph}

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex]:
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances, previous_nodes

def shortest_path(previous_nodes, start, target):
    path = []
    current_node = target

    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]

    path.reverse()
    return path if path[0] == start else []

def main():
    try:
        # Приклад графа (орієнтованого)
        graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('C', 2), ('D', 6)],
            'C': [('A', 4), ('B', 2), ('D', 3)],
            'D': [('B', 6), ('C', 3)]
        }

        # Запускаємо алгоритм Дейкстри
        start_node = 'A'
        distances, previous_nodes = dijkstra(graph, start_node)

        # Виведення результатів
        print("Відстані від вершини", start_node, ":")
        for node, distance in distances.items():
            print(f"До вершини {node}: {distance}")

        # Відновлення найкоротшого шляху до кожної вершини
        print("\nНайкоротші шляхи:")
        for target_node in graph:
            path = shortest_path(previous_nodes, start_node, target_node)
            print(f"Шлях до {target_node}: {path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()