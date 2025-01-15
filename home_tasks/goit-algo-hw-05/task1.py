class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def delete(self, key):
        key_hash = self.hash_function(key)

        if self.table[key_hash] is not None:
            del self.table[key_hash]
            return True
        return False

        #self.table.remove(key_hash)

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

def main():
    try:
        # Тестуємо нашу хеш-таблицю:
        H = HashTable(10)
        H.insert("apple", 10)
        H.insert("orange", 20)
        H.insert("banana", 30)

        print(H.get("apple"))  # Виведе: 10
        print(H.get("orange"))  # Виведе: 20
        print(H.get("banana"))  # Виведе: 30

        H.insert("pineapple", 40)
        print(H.get("pineapple"))
        H.delete("pineapple")
        print(H.get("pineapple"))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()