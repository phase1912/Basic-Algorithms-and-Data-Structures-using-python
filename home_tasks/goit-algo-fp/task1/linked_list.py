from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def search_element(self, data) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def reverse_list(self):
        current = self.head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def sort_list(self):
        sorted_list = LinkedList()
        current = self.head

        while current:
            sorted_list = self._sorted_insert(sorted_list, current.data)
            current = current.next

        self.head = sorted_list.head

    def merge_sorted_lists(self, list2):
        dummy = Node(0)
        tail = dummy

        current1 = self.head
        current2 = list2.head

        while current1 and current2:
            if current1.data < current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next

            tail = tail.next

        if current1:
            tail.next = current1
        elif current2:
            tail.next = current2

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def _sorted_insert(self, sorted_list, data):
        new_node = Node(data)

        if not sorted_list.head or data < sorted_list.head.data:
            new_node.next = sorted_list.head
            sorted_list.head = new_node
        else:
            current = sorted_list.head
            while current.next and current.next.data < data:
                current = current.next

            new_node.next = current.next
            current.next = new_node

        return sorted_list