from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

def dijkstra_menu():
    graph = Graph()
    while True:
        print("\n--- Dijkstra's Algorithm Menu ---")
        print("1. Add Edge")
        print("2. Find Shortest Paths")
        print("3. Display Graph")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            u = input("Enter start vertex: ")
            v = input("Enter end vertex: ")
            weight = int(input("Enter weight: "))
            graph.add_edge(u, v, weight)
        elif choice == 2:
            start = input("Enter start vertex: ")
            distances = graph.dijkstra(start)
            for vertex in distances:
                print(f"Distance from {start} to {vertex}: {distances[vertex]}")
        elif choice == 3:
            graph.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    dijkstra_menu()
