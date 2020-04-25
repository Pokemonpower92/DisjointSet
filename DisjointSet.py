# This is a basic Disjoint set implemented with
# Union by size with path compression.

class Node:
    ''' Every disjoint set holds a list of node objects.
        These are those objects. '''

    def __init__(self, data):
        self.data = str(data)
        self.link = self
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

    # Simply prints the set for bug testing.
    def print(self):
        for v in self.verticies.values():
            print(v.data + ':', v.link.data)
        print("Number of connected components:", self.components)

    # Finds the root of the node with the given data.
    def find(self, data):

        try:
            node = self.verticies[data]

            path = []

            while node.link != node:
                path.append(node)
                node = self.verticies[node.link.data]

            for v in path:
                v.link = node

            return node.data

        except KeyError:
            print('Invalid Key')
            return None




links = {}

for x in range(10):
    n = Node(x)
    links[n.data] = n

links['0'].link = links['2']
links['1'].link = links['2']
links['3'].link = links['1']
links['4'].link = links['3']

set = DisjointSet(links)

set.print()

b = set.find(4)

if b:
    print(b)

set.print()
