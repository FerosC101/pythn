class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_by_value(self, data):
        current = self.head
        if current is not None:
            if current.data == data:
                self.head = current.next
                current = None
                return
        prev = None
        while current is not None:
            if current.data == data:
                break
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def delete_by_position(self, position):
        if self.head is None:
            return
        current = self.head
        if position == 0:
            self.head = current.next
            current = None
            return
        for _ in range(position - 1):
            current = current.next
            if current is None:
                raise IndexError("Position out of range")
        if current.next is None:
            raise IndexError("Position out of range")
        next_node = current.next.next
        current.next = None
        current.next = next_node

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def display(self):
        elements = self.traverse()
        print(" -> ".join(map(str, elements)))

def menu():
    print("\n--- Singly Linked List Menu ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete by Value")
    print("5. Delete by Position")
    print("6. Display List")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    return choice

if __name__ == "__main__":
    sll = SinglyLinkedList()

    while True:
        choice = menu()
        if choice == 1:
            data = int(input("Enter data to insert at beginning: "))
            sll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data to insert at end: "))
            sll.insert_at_end(data)
        elif choice == 3:
            data = int(input("Enter data to insert: "))
            position = int(input("Enter position to insert at: "))
            try:
                sll.insert_at_position(data, position)
            except IndexError as e:
                print(e)
        elif choice == 4:
            data = int(input("Enter data to delete: "))
            sll.delete_by_value(data)
        elif choice == 5:
            position = int(input("Enter position to delete at: "))
            try:
                sll.delete_by_position(position)
            except IndexError as e:
                print(e)
        elif choice == 6:
            sll.display()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
