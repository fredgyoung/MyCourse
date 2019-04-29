

class Graph:

    def __init__(self):
        self.numVertices = 0
        self.vertices = {}

    def add_vertex(self, id):

        if id not in self.vertices:
            self.vertices[id] = []
            self.numVertices += 1
            return True
        else:
            return False

    def add_edge(self, src, dst):

        self.add_vertex(src)
        self.add_vertex(dst)

        if dst not in self.vertices[src]:
            self.vertices[src].append(dst)

    def print_graph(self):

        print(self.vertices)

    def pprint_graph(self) -> object:

        print('{')

        for k, v in self.vertices.items():
            print(' ', k, ':', v)

        print('}')


if __name__ == '__main__':

    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('c', 'd')
    g.add_edge('b', 'd')
    g.print_graph()
    g.pprint_graph()


