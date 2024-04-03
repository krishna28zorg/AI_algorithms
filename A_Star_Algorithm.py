# Define the graph representing the road network in Romania
# Each city is a node with its neighbors and corresponding edge costs.
# Replace this with your actual graph representation.

romania_graph = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101)],
}

# Define the heuristic distance (h) from each city to the goal city (Bucharest)
# Replace this with your actual heuristic values.

heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Fagaras': 178,
    'Lugoj': 244,
    'Mehadia': 241,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Zerind': 374,
}

import heapq

def a_star(start, goal, graph, heuristic):
    # Initialize the open set, came_from dictionary, and g_score dictionary
    open_set, came_from, g_score = [(0, start)], {}, {city: float('inf') for city in graph}
    g_score[start] = 0

    # Loop until the open set is empty
    while open_set:
        # Pop the city with the lowest cost from the open set
        current_cost, current_city = heapq.heappop(open_set)

        # If the current city is the goal, reconstruct and return the path
        if current_city == goal:
            path = [current_city]
            while current_city := came_from.get(current_city):
                path.append(current_city)
            return path[::-1]

        # Iterate through the neighbors of the current city
        for neighbor, cost in graph[current_city]:
            # Calculate the tentative g_score for the neighbor
            tentative_g_score = g_score[current_city] + cost
            # If the tentative g_score is lower than the current g_score of the neighbor
            if tentative_g_score < g_score[neighbor]:
                # Update the came_from and g_score dictionaries
                came_from[neighbor] = current_city
                g_score[neighbor] = tentative_g_score
                # Add the neighbor to the open set with its priority
                heapq.heappush(open_set, (tentative_g_score + heuristic[neighbor], neighbor))

    # Return None if no path is found
    return None

# Example usage
start_city, goal_city = 'Arad', 'Bucharest'
path = a_star(start_city, goal_city, romania_graph, heuristic)
print("Optimal Path:", path)
