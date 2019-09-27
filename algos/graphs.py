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


v1 = Vertex("v1")
v2 = Vertex("v2")
v3 = Vertex("v3")
v1.add_neighbor(v2, 3)
v1.add_neighbor(v3, 4)
