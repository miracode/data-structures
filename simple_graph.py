
class Node(object):
    def __init__(self, value=None):
        self.value = value


class Edge(object):
    def __init__(self, n1=None, n2=None):
        self.n1 = n1
        self.n2 = n2


class Graph(object):

    def __init__(self):
        self.nodes_list = []
        self.edges_list = []

    def nodes(self):
        """Return list of all nodes in graph"""
        return self.nodes_list

    def edges(self):
        """Return list of all edges in graph"""
        return self.edges_list

    def add_node(self, node):
        """Add new node to the graph"""
        self.nodes_list.append(node)

    def add_edge(self, n1, n2):
        new_edge = Edge(n1, n2)
        self.edges_list.append(new_edge)
