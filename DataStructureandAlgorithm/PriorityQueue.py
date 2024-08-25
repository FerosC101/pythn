import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, priority, element):
        heapq.heappush(self.heap, (-priority, element))

    def extract_max(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]
        return None

    def peek_max(self):
        if not self.is_empty():
            return self.heap[0][1]
        return None

    def is_empty(self):
        return len(self.heap) == 0

    def display(self):
        print([(-priority, element) for priority, element in self.heap])

def priority_queue_menu():
    pq = PriorityQueue()
    while True:
        print("\n--- Priority Queue Menu ---")
        print("1. Insert")
        print("2. Extract Max")
        print("3. Peek Max")
        print("4. Display Queue")
        print("5. Check if Empty")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = input("Enter element: ")
            priority = int(input("Enter priority: "))
            pq.insert(priority, element)
        elif choice == 2:
            print("Extracted:", pq.extract_max())
        elif choice == 3:
            print("Max element:", pq.peek_max())
        elif choice == 4:
            pq.display()
        elif choice == 5:
            print("Is empty:", pq.is_empty())
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    priority_queue_menu()
