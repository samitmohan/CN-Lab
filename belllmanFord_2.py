# Node class contains 2 things -> distance and previous node
class Node:
    def __init__(self, total_nodes) -> None:
        self.dist = [float('inf')] * total_nodes
        self.previousNode = [None] * total_nodes # empty as of now

def bf(total_nodes, cost):
    node = [Node(total_nodes) for _ in range(total_nodes)]
    # fill up adj matrix
    for i in range(total_nodes):
        for j in range(total_nodes):
            node[i].dist[j], node[i].previousNode[j] = cost[i][j], j # dist i -> j and previous path
    # perform bf
    for _ in range(total_nodes - 1):
        for i in range(total_nodes):
            for j in range(total_nodes):
                for k in range(total_nodes):
                    if node[i].dist[j] > node[i].dist[k] + node[k].dist[j]: # i -> j > (i -> k -> j) then update
                        # update node distance and previous node
                        node[i].dist[j], = node[i].dist[k] + node[k].dist[j]
                        node[i].previousNode[j] = k # update where it came from (not i -> j but i -> k -> j)
    # print
    for i in range(total_nodes):
        print(f"State value for router {i} is")
        for j in range(total_nodes):
            # print matrix
            print(f"Via {node[i].previousNode[j]} Distance {node[i].dist[j]}")


def main():
    total_nodes = int(input("Enter number of nodes : "))
    cost = [list(map(int, input().split())) for _ in range(total_nodes)]
    bf(total_nodes, cost)
main()