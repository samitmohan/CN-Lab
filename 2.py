class Node:
    def __init__(self, total_nodes) -> None:
        self.dist = [float('inf')] * total_nodes
        self.prevsNode = [None] * total_nodes

def bf(total_nodes, cost):
    node = [Node(total_nodes) for _ in range(total_nodes)]
    for i in range(total_nodes):
        for j in range(total_nodes):
            node[i].dist[j], node[i].prevsNode[j] = cost[i][j], j
    for _ in range(total_nodes-1):
        for i in range(total_nodes):
            for j in range(total_nodes):
                for k in range(total_nodes):
                    if node[i].dist[j] > node[i].dist[k] + node[k].dist[j]:
                        node[i].dist[j] = node[i].dist[k] + node[k].dist[j]
                        node[i].prevsNode[j] = k
    for i in range(total_nodes):
        print(f"State value of router {i} is ")
        for j in range(total_nodes):
            print(f"Via {node[i].prevsNode[j]}  Distance {node[i].dist[j]}")

def main():
    total_nodes = int(input("Enter total nodes : "))
    cost = [list(map(int, input().split())) for _ in range(total_nodes)]
    bf(total_nodes, cost)
main()