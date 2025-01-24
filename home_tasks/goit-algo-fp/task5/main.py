import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, pause_time=1.0):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.clf()
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.draw()
    plt.pause(pause_time)

def generate_colors(n):
    colors = []
    for i in range(n):
        hue = 0.6  # Відтінок (синій)
        lightness = 0.3 + (0.7 * i / (n - 0.5))  # Від темного до світлого
        saturation = 0.8
        r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
        colors.append("#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255)))
    return colors

def breadth_first_traversal(tree_root):
    queue = deque([tree_root])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node:
            traversal_order.append(node)
            queue.append(node.left)
            queue.append(node.right)

    return traversal_order

def depth_first_traversal(tree_root):
    stack = [tree_root]
    traversal_order = []

    while stack:
        node = stack.pop()
        if node:
            traversal_order.append(node)
            stack.append(node.right)
            stack.append(node.left)

    return traversal_order

def visualize_traversal(tree_root, traversal_order):
    colors = generate_colors(len(traversal_order))

    for i, node in enumerate(traversal_order):
        node.color = colors[i]
        draw_tree(tree_root)

def heap_to_tree(heap):
    if not heap:
        return None

    nodes = [Node(val) for val in heap]  # Створення вузлів для кожного елемента масиву

    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(heap):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap):
            nodes[i].right = nodes[right_index]

    return nodes[0]

def main():
    heap = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # Бінарна макс-купа
    root = heap_to_tree(heap)

    # Обхід в ширину
    bfs_order = breadth_first_traversal(root)
    print("Breadth-First Traversal:", [node.val for node in bfs_order])
    visualize_traversal(root, bfs_order)

    # Обхід в глибину
    dfs_order = depth_first_traversal(root)
    print("Depth-First Traversal:", [node.val for node in dfs_order])
    visualize_traversal(root, dfs_order)

if __name__ == "__main__":
    main()