# This is a basic Disjoint set implemented with
# Union by size with path compression.

class Node:
    ''' Every disjoint set holds a list of node objects.
        These are those objects. '''

    def __init__(self, data):
        self.data = str(data)
        self.link = None
        self.size = 1

    def clear(self):
        self.link = None
        self.size = 1

class DisjointSet:
    ''' This is a union by size with path compression implementation. '''
    ''' Verticies are stored as a dictionary of nodes keyed on their data. '''

    def __init__(self, verticies):
        self.verticies = verticies
        self.size = len(verticies)
        self.components = self.size

    def print(self):
        for v in self.verticies.values():
            print(v.data + ':', v.link)
        print("Number of connected components:", self.components)

    def find(self, data):
        return

links = {}

for x in range(10):
    n = Node(x)
    links[n.data] = n

set = DisjointSet(links)

set.print()
