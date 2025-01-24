import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    parent = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, parent

def shortest_path(previous_nodes, start, target):
    path = []
    current_node = target

    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]

    path.reverse()
    return path if path[0] == start else []

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def main():
    start_vertex = input("Введіть початкову вершину: ")
    distances, parent = dijkstra(graph, start_vertex)

    print("Найкоротші відстані від вершини", start_vertex)
    for vertex, distance in distances.items():
        print(f"Відстань до {vertex}: {distance}")

    target_vertex = input("Введіть кінцеву вершину для пошуку шляху: ")
    path = shortest_path(parent, start_vertex, target_vertex)
    print("Найкоротший шлях:", " -> ".join(path))

if __name__ == "__main__":
    main()