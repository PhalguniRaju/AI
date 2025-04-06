import heapq
class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, node1, node2, cost):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append((node2, cost))
        self.graph[node2].append((node1, cost))
    def a_star(self, start, goal, heuristic):
        open_list = []
        heapq.heappush(open_list, (0 + heuristic[start], 0, start, []))
        closed_set = set()
        while open_list:
            _, cost, current, path = heapq.heappop(open_list)
            if current in closed_set:
                continue
            path = path + [current]
            closed_set.add(current)
            if current == goal:
                return path, cost
            for neighbor, edge_cost in self.graph.get(current, []):
                if neighbor not in closed_set:
                    heapq.heappush(open_list, (cost + edge_cost + heuristic[neighbor], cost + edge_cost, neighbor, path))
        return None, float("inf")
graph = Graph()
graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 4)
graph.add_edge("B", "C", 2)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 1)
test_heuristic = {"A": 7, "B": 6, "C": 2, "D": 0}
path, cost = graph.a_star("A", "D", test_heuristic)
print("Shortest path:", path)
print("Total cost:", cost)
