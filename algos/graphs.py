import ipdb

class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=0):
        if self.neighbors.get(neighbor.key) is None:
            self.neighbors[neighbor.key] = weight
        else:
            print(f"neighbor {neighbor.key} with weight {self.neighbors[neighbor.key]} already exists.")

    def __str__(self):
        return '{} neighbors: {}'.format(
            self.key, [x.key for x in self.neighbors]
        )

    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor.key]


class Graph(object):
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex):
        self.verticies[vertex.key] = vertex

    def get_vertex(self, key):
        return self.verticies.get(key)

    def get_vertex2(self, key):
        try:
            self.verticies[key]
        except KeyError:
            return None

    def __contains__(self, key):
        if key in self.verticies:
           return True
        else:
            return False

    def add_edge(self, from_key, to_key, weight=0):
        # if from_key Vertex doesn't exist
        if from_key not in self.verticies:
            self.add_vertex(Vertex(from_key))

        # if to_key Vertex doesn't exist
        if to_key not in self.verticies:
            self.add_vertex(Vertex(to_key))

        from_vertex = self.verticies[from_key]
        to_vertex = self.verticies[to_key]

        # if from_vertex is already a neighbor of to_vertex
        if to_vertex not in from_vertex.neighbors:
            from_vertex.add_neighbor(to_vertex)

    def get_verticies(self):
        return self.verticies.values()

    def __iter__(self):
        return iter(self.verticies.values())


v1 = Vertex("v1")
v2 = Vertex("v2")
v3 = Vertex("v3")
v1.add_neighbor(v2, 3)
v1.add_neighbor(v3, 4)

g1 = Graph()
g1.add_vertex(v1)
g1.add_vertex(v2)
g1.add_edge("v1", "v2")
g1.add_edge("v2", "v9", 11)
