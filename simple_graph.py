
class Node(object):
    def __init__(self, value=None):
        self.value = value


class Edge(object):
    def __init__(self, n1=Node(), n2=Node()):
        self.n1 = n1
        self.n2 = n2
        self.node_vals = (n1.value, n2.value)


class Graph(object):

    def __init__(self):
        self.nodes_list = []
        self.edges_list = []

    def nodes(self):
        """Return list of all node values in graph"""
        return [node.value for node in self.nodes_list]

    def edges(self):
        """Return list of all edge tuples in graph"""
        return [edge.node_vals for edge in self.edges_list]

    def add_node(self, node_val):
        """Add new node value to the graph"""
        if node_val in self.nodes():
            raise ValueError("Node already exists in graph")
        else:
            node = Node(node_val)
            self.nodes_list.append(node)

    def add_edge(self, n1, n2):
        """Add new edge to graph with given node values"""
        new_edge = Edge(Node(n1), Node(n2))
        self.edges_list.append(new_edge)
        # If new nodes do not exists in list of nodes, add them
        try:
            self.add_node(n1)
        except ValueError:
            pass
        try:
            self.add_node(n2)
        except ValueError:
            pass

    def del_node(self, n):
        """Delete specified node from the graph"""

        # If node exists in list of nodes, remove. Else raise error
        node_in_graph = False
        for node in self.nodes_list:
            if n == node:
                self.nodes_list.remove(n)
                node_in_graph = True

        # Determine if node exists in edges & remove
        if node_in_graph:
            for edge in self.edges_list:
                if n in edge.nodes:
                    self.edges_list.remove(edge)

        else:
            raise IndexError(u"Node does not exist in graph.")

    def del_edge(self, n1, n2):
        """Delete edge connecting specified nodes"""
        edge_in_graph = False
        for edge in self.edges_list:
            if n1 in edge.nodes and n2 in edge.nodes:
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
        if not self.has_node(n):
            raise IndexError(u"Node does not exist in graph")
        else:
            neighb = []
            for edge in self.edges_list:
                if edge.n1 == n:
                    neighb.append(edge.n2)
                if edge.n2 == n:
                    neighb.append(edge.n1)
            return neighb

    def adjacent(self, n1, n2):
        """Returns True if edge connects two nodes, False if not"""
        if not self.has_node(n1):
            raise IndexError(u"Node does not exist in graph")
        elif not self.has_node(n2):
            raise IndexError(u"Node does not exist in graph")
        else:
            edge_in_graph = False
            for edge in self.edges_list:
                if n1 in edge.nodes and n2 in edge.nodes:
                    edge_in_graph = True
            return edge_in_graph
