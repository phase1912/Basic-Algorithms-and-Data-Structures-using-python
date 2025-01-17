import networkx as nx
import matplotlib.pyplot as plt

def dfs_recursive(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs_recursive(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None

def bfs_iterative(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
    return None

def main():
    try:
        # Створення графу для моделювання маршруту від залізничного вокзалу Києва
        G = nx.Graph()

        locations = [
            "Залізничний вокзал", "Університет", "Театральна", "Хрещатик", "Майдан Незалежності",
            "Арсенальна", "Печерськ", "Дружби Народів", "Либідська", "Палац Україна", "Олімпійська"
        ]
        G.add_nodes_from(locations)

        edges = [
            ("Залізничний вокзал", "Університет", {"weight": 2}),
            ("Університет", "Театральна", {"weight": 1}),
            ("Театральна", "Хрещатик", {"weight": 2}),
            ("Хрещатик", "Майдан Незалежності", {"weight": 1}),
            ("Майдан Незалежності", "Арсенальна", {"weight": 3}),
            ("Арсенальна", "Печерськ", {"weight": 2}),
            ("Печерськ", "Дружби Народів", {"weight": 2}),
            ("Дружби Народів", "Либідська", {"weight": 2}),
            ("Либідська", "Палац Україна", {"weight": 1}),
            ("Палац Україна", "Олімпійська", {"weight": 2}),
            ("Університет", "Олімпійська", {"weight": 4}),
            ("Хрещатик", "Печерськ", {"weight": 3})
        ]
        G.add_edges_from(edges)

        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(12, 10))
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue")

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        num_nodes = G.number_of_nodes()
        num_edges = G.number_of_edges()
        degree_dict = dict(G.degree())

        analysis_text = f"Вузли: {num_nodes}\nРебра: {num_edges}\nСтупені: {degree_dict}"
        plt.gcf().text(0.02, 0.95, analysis_text, fontsize=10, verticalalignment='top',
                       bbox=dict(facecolor='white', alpha=0.5))

        plt.title("Маршрут від залізничного вокзалу Києва")
        plt.show()

        start_node = "Залізничний вокзал"
        end_node = "Олімпійська"

        # Знаходження шляхів
        dfs_result = dfs_recursive(G, start_node, end_node)
        bfs_result = bfs_iterative(G, start_node, end_node)

        # Порівняння результатів
        print("Шлях DFS:", dfs_result)
        print("Шлях BFS:", bfs_result)

        # Пояснення відмінностей
        explanation = (
            "DFS (пошук в глибину) намагається йти до кінця гілки, перш ніж повернутися назад, тому шлях може бути довшим або незвичним.\n"
            "BFS (пошук в ширину) обчислює найкоротший шлях в сенсі кількості вузлів, що робить його ефективнішим для пошуку мінімального шляху."
        )
        print("\nПояснення:")
        print(explanation)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()