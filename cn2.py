class Node:
    def __init__(self, num_nodes):
        self.dist = [float('inf')] * num_nodes
        self.from_node = [None] * num_nodes


def bf(num_nodes, cost):
    nodes = [Node(num_nodes) for _ in range(num_nodes)]

    for i in range(num_nodes):
        for j in range(num_nodes):
            nodes[i].dist[j] = cost[i][j]
            nodes[i].from_node[j] = j

    for _ in range(num_nodes - 1):
        for i in range(num_nodes):
            for j in range(num_nodes):
                for k in range(num_nodes):
                    if nodes[i].dist[j] > nodes[i].dist[k] + nodes[k].dist[j]:
                        nodes[i].dist[j] = nodes[i].dist[k] + nodes[k].dist[j]
                        nodes[i].from_node[j] = k

    for i in range(num_nodes):
        print(f"State Value For Router {i} Is")
        for j in range(num_nodes):
            print(f"\t\tVia {nodes[i].from_node[j]} Distance {nodes[i].dist[j]}")


def main():
    num_nodes = int(input("Enter The Number Of Nodes: "))
    cost = []

    print("Enter The Cost Matrix:")
    for i in range(num_nodes):
        row = list(map(int, input().split()))
        cost.append(row)

    bf(num_nodes, cost)


if __name__ == "__main__":
    main()
