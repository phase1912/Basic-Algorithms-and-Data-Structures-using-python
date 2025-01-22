class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

# Завдання 1: Знаходження найбільшого значення у дереві
    def find_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.key

# Завдання 2: Знаходження найменшого значення у дереві
    def find_min(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.key

# Завдання 3: Знаходження суми всіх значень у дереві
    def find_sum(self):
        return self._find_sum(self.root)

    def _find_sum(self, node):
        if not node:
            return 0
        return node.key + self._find_sum(node.left) + self._find_sum(node.right)

def main():
    try:
        bst = BinarySearchTree()
        values = [20, 10, 30, 5, 15, 25, 35]
        for value in values:
            bst.insert(value)

        print("Найбільше значення:", bst.find_max())  # Завдання 1
        print("Найменше значення:", bst.find_min())  # Завдання 2
        print("Сума всіх значень:", bst.find_sum())  # Завдання 3
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()