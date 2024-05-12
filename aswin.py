import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, resident, booth, distance):
        if resident not in self.adj_list:
            self.adj_list[resident] = []
        if booth not in self.adj_list:
            self.adj_list[booth] = []
        self.adj_list[resident].append((booth, distance))
        self.adj_list[booth].append((resident, distance))

    def shortest_path(self, start, end):
        min_heap = [(0, start)]  
        distances = {node: float('inf') for node in self.adj_list}  
        distances[start] = 0

        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)

            if current_node == end:
                return distances[end]

            if current_dist > distances[current_node]:
                continue

            for neighbor, edge_weight in self.adj_list[current_node]:
                distance = current_dist + edge_weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return float('inf') 


if __name__ == "__main__":
    graph = Graph()
    num_residents = int(input("Enter the number of residents: "))
    num_booths = int(input("Enter the number of booths: "))

    
    resident_names = [input(f"Enter name of resident {i+1}: ") for i in range(num_residents)]
    booth_names = [input(f"Enter name of booth {i+1}: ") for i in range(num_booths)]

    
    for resident in resident_names:
        for booth in booth_names:
            distance = float(input(f"Enter distance between {resident} and {booth}: "))
            graph.add_edge(resident, booth, distance)
    
    
    for resident in resident_names:
        min_distance = float('inf')
        nearest_booth = None
        for booth in booth_names:
            distance = graph.shortest_path(resident, booth)
            if distance < min_distance:
                min_distance = distance
                nearest_booth = booth
        print(f"{resident} is allocated to {nearest_booth} with distance {min_distance}")




