import networkx as nx
import matplotlib.pyplot as plt

def main():
    try:
        G = nx.Graph()

        # Вузли - станції метро червоної гілки Києва
        stations = [
            "Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська",
            "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет",
            "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк",
            "Лівобережна", "Дарниця", "Чернігівська", "Лісова"
        ]
        G.add_nodes_from(stations)

        # Ребра - з'єднання між станціями
        edges = [
            ("Академмістечко", "Житомирська", {"weight": 4}),
            ("Житомирська", "Святошин", {"weight": 3}),
            ("Святошин", "Нивки", {"weight": 2}),
            ("Нивки", "Берестейська", {"weight": 3}),
            ("Берестейська", "Шулявська", {"weight": 2}),
            ("Шулявська", "Політехнічний інститут", {"weight": 3}),
            ("Політехнічний інститут", "Вокзальна", {"weight": 2}),
            ("Вокзальна", "Університет", {"weight": 2}),
            ("Університет", "Театральна", {"weight": 2}),
            ("Театральна", "Хрещатик", {"weight": 1}),
            ("Хрещатик", "Арсенальна", {"weight": 3}),
            ("Арсенальна", "Дніпро", {"weight": 2}),
            ("Дніпро", "Гідропарк", {"weight": 3}),
            ("Гідропарк", "Лівобережна", {"weight": 4}),
            ("Лівобережна", "Дарниця", {"weight": 3}),
            ("Дарниця", "Чернігівська", {"weight": 3}),
            ("Чернігівська", "Лісова", {"weight": 2})
        ]
        G.add_edges_from(edges)

        # Візуалізація графу
        pos = nx.spring_layout(G, seed=42)  # Фіксоване розташування вузлів для повторюваності
        plt.figure(figsize=(12, 10))
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue")

        # Додавання ваг на ребрах
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Аналіз характеристик графу
        num_nodes = G.number_of_nodes()
        num_edges = G.number_of_edges()
        degree_dict = dict(G.degree())

        # Додавання тексту з характеристиками графу на графік
        analysis_text = f"Вузли: {num_nodes}\nРебра: {num_edges}\nСтупені: {degree_dict}"

        print(analysis_text)

        plt.gcf().text(0.02, 0.95, analysis_text, fontsize=10, verticalalignment='top',
                       bbox=dict(facecolor='white', alpha=0.5))

        plt.title("Червона гілка метро Києва")
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()