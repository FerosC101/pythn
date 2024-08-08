class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)

def stack_menu():
    stack = Stack()
    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if Stack is Empty")
        print("5. Display Stack")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to push onto stack: "))
            stack.push(data)
        elif choice == 2:
            print("Popped:", stack.pop())
        elif choice == 3:
            print("Top element:", stack.peek())
        elif choice == 4:
            print("Is stack empty?", stack.is_empty())
        elif choice == 5:
            stack.display()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    stack_menu()
