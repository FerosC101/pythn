from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def remove_vertex(self, v):
        if v in self.graph:
            del self.graph[v]
            for key in self.graph:
                if v in self.graph[key]:
                    self.graph[key].remove(v)

    def add_edge(self, v, w):
        self.graph[v].append(w)

    def remove_edge(self, v, w):
        if v in self.graph and w in self.graph[v]:
            self.graph[v].remove(w)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, v):
        visited = set()
        self.dfs_util(v, visited)

    def bfs(self, s):
        visited = set()
        queue = deque([s])
        visited.add(s)
        while queue:
            v = queue.popleft()
            print(v, end=' ')
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

def graph_menu():
    graph = Graph()
    while True:
        print("\n--- Graph Menu ---")
        print("1. Add Vertex")
        print("2. Remove Vertex")
        print("3. Add Edge")
        print("4. Remove Edge")
        print("5. Perform DFS")
        print("6. Perform BFS")
        print("7. Display Graph")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            v = input("Enter vertex: ")
            graph.add_vertex(v)
        elif choice == 2:
            v = input("Enter vertex: ")
            graph.remove_vertex(v)
        elif choice == 3:
            v = input("Enter start vertex: ")
            w = input("Enter end vertex: ")
            graph.add_edge(v, w)
        elif choice == 4:
            v = input("Enter start vertex: ")
            w = input("Enter end vertex: ")
            graph.remove_edge(v, w)
        elif choice == 5:
            v = input("Enter start vertex: ")
            print("DFS traversal: ", end='')
            graph.dfs(v)
            print()
        elif choice == 6:
            v = input("Enter start vertex: ")
            print("BFS traversal: ", end='')
            graph.bfs(v)
            print()
        elif choice == 7:
            graph.display()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    graph_menu()
