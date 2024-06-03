g_n = {}
h_n = {}

n = int(input("Enter the number of nodes: "))

for _ in range(n):
    node = input("Enter the node: ")
    neighbors = input("Enter the neighbors: ").split(',')
    if neighbors == ['']:
        g_n[node] = []
    else:
        g_n[node] = [(neighbor, int(input(f"Enter the cost of the path to {neighbor}: "))) for neighbor in neighbors]

print("Graph (g_n):", g_n)

for node in g_n:
    h_n[node] = int(input(f"Enter the heuristic cost for node {node}: "))

print("Heuristic (h_n):", h_n)

def search(start, goal, path):
    if start == goal:
        print(path)
        return
    next_node, _ = min(g_n[start], key=lambda x: x[1] + h_n[x[0]])
    path.append(next_node)
    search(next_node, goal, path)

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

search(start, goal, [start])
