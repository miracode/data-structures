
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
        """Add new edge to graph"""
        new_edge = Edge(n1, n2)
        self.edges_list.append(new_edge)
        # If new nodes do not exists in list of nodes, add them
        if n1 not in self.nodes():
            self.add_node(n1)
        if n2 not in self.nodes():
            self.add_node(n2)

    def del_node(self, n):
        """Delete specified node from the graph"""
        # Determine if node exists in edges & remove
        for edge in self.edges_list:
            if n == edge.n1 or n == edge.n2:
                self.edges_list.remove(edge)

        # If node exists in list of nodes, remove. Else raise error
        node_in_graph = False
        for node in self.nodes_list:
            if n == node:
                self.nodes_list.remove(n)
                node_in_graph = True

        if not node_in_graph:
            raise IndexError(u"Node does not exist in graph.")

    def del_edge(self, n1, n2):
        """Delete edge connecting specified nodes"""
        edge_in_graph = False
        for edge in self.edges_list:
            if n1 == edge.n1 and n2 == edge.n2:
                self.edges_list.remove(edge)
                edge_in_graph = True

        if not edge_in_graph:
            raise IndexError(u"Edge does not exist in graph.")

    def has_node(self, n):
        """Returns True if node is in the graph, otherwise False"""
        if n in self.nodes_list:
            return True
        else:
            return False

    def neighbors(self, n):
        """Returns list of nodes connected to given node"""
        #if not self.has_node(n) raise IndexError
        neighb = []
        for edge in self.edges_list:
            if edge.n1 == n:
                neighb.append(edge.n2)
            if edge.n2 == n:
                neighb.append(edge.n1)
        return neighb
