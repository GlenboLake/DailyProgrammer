import networkx


def graph_from_file(filename):
    with open(filename) as f:
        node_count = int(f.readline())
        graph = networkx.Graph()
        graph.add_nodes_from(range(1, node_count + 1))
        graph.add_edges_from(list(map(int, edge.split())) for edge in f.read().splitlines())
    return graph


def count_degrees(graph):
    return {n: len(graph.neighbors(n)) for n in graph.nodes()}


def adjacency_matrix(graph):
    sz = len(graph.nodes())
    mat = [[0] * sz for _ in range(sz)]
    for u, v in graph.edges():
        mat[u - 1][v - 1] = mat[v - 1][u - 1] = 1
    return mat


def matrix_to_s(mat):
    return '\n'.join(' '.join(str(x) for x in row) for row in mat)

if __name__ == '__main__':
    g = graph_from_file('input/C266e.txt')
    degrees = count_degrees(g)
    for node, degree in degrees.items():
        print('Node {} has a degree of {}'.format(node, degree))
    print(matrix_to_s(adjacency_matrix(g)))
