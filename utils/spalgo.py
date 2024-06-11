import networkx as nx

def dijkstra(graph: nx.MultiDiGraph, source, target):
    # Initialize distances dictionary with source node having distance 0
    distances = {node: float('inf') for node in graph.nodes()}
    distances[source] = 0

    # Initialize priority queue
    priority_queue = [(0, source)]

    while priority_queue:
        # Pop node with minimum distance from priority queue
        current_distance, current_node = min(priority_queue)
        priority_queue.remove((current_distance, current_node))
            
        # If current node is the target, return the distance
        if current_node == target:
            return distances[target]

        # Iterate through neighbors of current node
        for neighbor in graph.neighbors(current_node):
            # Calculate new distance via current node to the neighbor
            distance = current_distance + graph[current_node][neighbor][0]['length']

            # If new distance is shorter, update distances dictionary and add to priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))

    # If target is unreachable from source, return None
    return None

def bellman_ford(graph, source, target):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[source] = 0
    for _ in range(len(graph.nodes()) - 1):
        for u, v in graph.edges():
            distance = distances[u] + graph[u][v][0]['length']
            if distance < distances[v]:
                distances[v] = distance
    for u, v in graph.edges():
        if distances[u] + graph[u][v][0]['length'] < distances[v]:
            return None
    return distances[target]

def bellman_ford(graph, source, target):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[source] = 0
    for _ in range(len(graph.nodes()) - 1):
        for u, v in graph.edges():
            distance = distances[u] + graph[u][v][0]['length']
            if distance < distances[v]:
                distances[v] = distance
    for u, v in graph.edges():
        if distances[u] + graph[u][v][0]['length'] < distances[v]:
            return None
    return distances[target]

def floyd_warshall(graph, source, target):
    # Initialize distance matrix
    num_nodes = len(graph.nodes())
    dist = [[float('inf')] * num_nodes for _ in range(num_nodes)]
    # Initialize diagonal with 0s and edges with their weights
    for u, v, w in graph.edges(data='length'):
        dist[u][v] = w
        dist[v][u] = w

    
    # Update distance matrix
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    print(dist)

    # Retrieve shortest path distance between source and target from the distance matrix
    return dist[source][target]
