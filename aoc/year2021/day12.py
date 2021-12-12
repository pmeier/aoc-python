from collections import Counter, defaultdict


def parse_lines(solver):
    def wrapper(lines):
        graph = defaultdict(list)
        for line in lines:
            node1, node2 = line.split("-")
            graph[node1].append(node2)
            graph[node2].append(node1)

        return solver(graph)

    return wrapper


def traverse(graph, *, small_cond, node="start", path=()):
    path = path + (node,)
    if node == "end":
        yield path
        return

    for connection in graph[node]:
        if connection.isupper() or small_cond(connection, path):
            yield from traverse(
                graph, small_cond=small_cond, node=connection, path=path
            )


@parse_lines
def part1(graph):
    return len(list(traverse(graph, small_cond=lambda node, path: node not in path)))


@parse_lines
def part2(graph):
    def small_cond(node, path):
        if node not in path:
            return True

        if node == "start":
            return False

        count = Counter([node for node in path if node.islower()])
        return count.most_common(1)[0][1] == 1

    return len(list(traverse(graph, small_cond=small_cond)))
