class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        for i, kv in enumerate(self.table[hash_key]):
            if kv[0] == key:
                self.table[hash_key][i] = (key, value)
                return
        self.table[hash_key].append((key, value))

    def delete(self, key):
        hash_key = self.hash_function(key)
        for i, kv in enumerate(self.table[hash_key]):
            if kv[0] == key:
                del self.table[hash_key][i]
                return

    def search(self, key):
        hash_key = self.hash_function(key)
        for kv in self.table[hash_key]:
            if kv[0] == key:
                return kv[1]
        return None

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

def hash_table_menu():
    hash_table = HashTable()
    while True:
        print("\n--- Hash Table Menu ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = input("Enter key: ")
            value = input("Enter value: ")
            hash_table.insert(key, value)
        elif choice == 2:
            key = input("Enter key to delete: ")
            hash_table.delete(key)
        elif choice == 3:
            key = input("Enter key to search: ")
            result = hash_table.search(key)
            if result:
                print("Value:", result)
            else:
                print("Key not found")
        elif choice == 4:
            hash_table.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    hash_table_menu()
