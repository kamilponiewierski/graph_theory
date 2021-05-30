def djikstra(graph, start, end):
    distance = {start: 0}
    prev = dict()
    q = []

    for v in graph:
        distance[v] = 10 ** 50  # infinity
        q.append(v)

    distance[start] = 0

    while len(q) > 0:
        vertices = sorted(q, key=lambda x: distance[x])
        current_vertex = vertices.pop(0)
        q = vertices
        for v in graph[current_vertex]:
            old_distance = distance[v]
            new_distance = distance[current_vertex] + (graph[current_vertex])[v]
            if old_distance > new_distance:
                distance[v] = new_distance
                prev[v] = current_vertex

    print(f'Shortest path is {distance[end]}')

    curr = end

    path = []

    while curr != start:
        path.append(curr)
        curr = prev[curr]
    path.append(start)
    path.reverse()

    print(*path, sep=' => ')


if __name__ == '__main__':
    n = int(input('How many vertices?\n'))
    graph = dict()
    for i in range(n):
        line = input()
        words = line.split(' ')
        graph[words[0]] = {}
        assert (len(words) % 2 == 1)
        for vertex, weight in zip(words[1::2], words[2::2]):
            (graph[words[0]])[vertex] = int(weight)

    while True:
        starting = input('Finding path from?\n')
        if starting in graph:
            break
        print('Vertex not found in the graph, please try again\n')
    while True:
        ending = input('Finding path to?\n')
        if starting in graph:
            break
        print('Vertex not found in the graph, please try again\n')

    djikstra(graph, starting, ending)
