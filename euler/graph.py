class Graph:
    def __init__(self, origin_dict):
        self.vertices = {}
        for key in origin_dict:
            self.vertices[key] = []
            for x in origin_dict[key]:
                self.vertices[x] = []
        for key in origin_dict:
            for x in origin_dict[key]:
                try:
                    self.connect(x, key)
                except Exception:
                    pass

    @property
    def len(self):
        return len(self.vertices)

    @property
    def keys(self):
        return list(self.vertices.keys())

    def __getitem__(self, key):
        return self.vertices[key]

    def __setitem__(self, key, value):
        self.vertices[key] = value

    def connect(self, a, b):
        if a in self[b] or b in self[a]:
            raise Exception("cant be 2 or more edges")
        self[a].append(b)
        self[b].append(a)

    def disconnect(self, a, b):
        if a not in self[b] or b not in self[a]:
            raise Exception("no such edge")
        self[a].remove(b)
        self[b].remove(a)

    def __repr__(self):
        out = ""
        for key in self.vertices:
            out += f"{key}: {self.vertices[key]}"
        return out


def foo(graph, ind, connectivity_components):
    connectivity_components.append(ind)
    for vert in graph[ind]:
        if vert not in connectivity_components:
            foo(graph, vert, connectivity_components)


def find_connectivity_components(graph):
    connectivity_components = []
    all_calculated_components = []
    for key in graph.keys:
        if key not in all_calculated_components:
            current_component = []
            connectivity_components.append(current_component)
            foo(graph, key, current_component)
            all_calculated_components += current_component
    return connectivity_components


def is_eulerian(graph):
    return len(find_connectivity_components(graph)) == 1 and sum(
        [len(graph[x]) % 2 == 0 for x in graph.vertices]) == graph.len


def color_up(graph, ind, is_red, red_ones, blue_ones):
    if is_red:
        red_ones.append(ind)
    else:
        blue_ones.append(ind)
    for vert in graph[ind]:
        if (is_red and vert in red_ones) or (not is_red and vert in blue_ones):
            raise Exception("not bipartite")
        if vert in blue_ones or vert in red_ones:
            continue
        color_up(graph, vert, not is_red, red_ones, blue_ones)


def find_bipartite(graph):
    if graph.len == 1:
        raise Exception("only 1 el")
    red_ones = []
    blue_ones = []
    for vert in graph.vertices:
        if vert not in red_ones and vert not in blue_ones:
            color_up(graph, vert, True, red_ones, blue_ones)
    if graph.len != len(red_ones) + len(blue_ones):
        raise Exception("more than 1 component")
    return red_ones, blue_ones


def is_bipartite(graph):
    try:
        find_bipartite(graph)
        return True
    except Exception:
        return False


def find_euler_path(graph):
    if not is_eulerian(graph):
        raise Exception("it is not euler graph")
    current = graph.keys[0]
    stack = []
    result = []
    ind = 0
    degrees = [len(graph[x]) for x in graph.vertices]
    assert sum(degrees) % 2 == 0
    while len(result) != sum(degrees) / 2 - 1:
        if ind >= len(graph[current]):
            result.append(stack.pop())
            current = stack[-1][0]
            ind = 0
        edge = (graph[current][ind], current)
        if edge not in stack and edge not in result and tuple(reversed(edge)) not in stack and tuple(
                reversed(edge)) not in result:
            current = graph[current][ind]
            stack.append(edge)
            ind = 0
        else:
            ind += 1
    result.append(stack.pop())
    return result
