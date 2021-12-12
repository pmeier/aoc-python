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


def traverse(graph, *, node="start", path=(), relax_cond=lambda node, path: False):
    path = path + (node,)
    if node == "end":
        yield path
        return

    for connection in graph[node]:
        if (
            connection.isupper()
            or connection not in path
            or relax_cond(connection, path)
        ):
            yield from traverse(
                graph, node=connection, path=path, relax_cond=relax_cond
            )


@parse_lines
def part1(graph):
    return len(list(traverse(graph)))


@parse_lines
def part2(graph):
    def relax_cond(node, path):
        if node == "start":
            return False

        return (
            Counter([node for node in path if node.islower()]).most_common(1)[0][1] == 1
        )

    return len(list(traverse(graph, relax_cond=relax_cond)))
