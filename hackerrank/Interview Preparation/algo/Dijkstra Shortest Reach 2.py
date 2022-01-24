def build_graph(N, M):
    graph = Graph(N)
    while M > 0:
        (x, y, R) = read_integers()
        graph.get_vertex(x).add_edge(y, R)
        graph.get_vertex(y).add_edge(x, R)
        M -= 1
    return graph


def print_distances(distances, N, S):
    for i in range(1, N + 1):
        if i == S:
            continue
        distance = -1 if i not in distances else distances[i]
        print(distance, end=" ")
    print()


def execute_test_case():
    (N, M) = read_integers()
    graph = build_graph(N, M)
    dijkstra = Dijkstra(graph)
    S = int(sys.stdin.readline())
    distances = dijkstra.calculate(S)
    print_distances(distances, N, S)


def main():
    T = int(sys.stdin.readline())
    while T > 0:
        execute_test_case()
        T -= 1


if __name__ == "__main__":
    main()
# Input (stdin)

# Download
# 1
# 4 4
# 1 2 24
# 1 4 20
# 3 1 3
# 4 3 12
# 1
# Expected Output

# Download
# 24 3 15