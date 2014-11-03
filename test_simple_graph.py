import unittest
import simple_graph


class GraphTest(unittest.TestCase):

    def test_no_nodes(self):
        g = simple_graph.Graph()
        no_nodes = g.nodes()
        assert no_nodes == []

    def test_nodes(self):
        g = simple_graph.Graph()
        g.nodes_list = [simple_graph.Node(), simple_graph.Node()]
        assert len(g.nodes()) == 2

    def test_no_edges(self):
        g = simple_graph.Graph()
        no_edges = g.edges()
        assert no_edges == []
