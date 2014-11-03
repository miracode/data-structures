import unittest
import simple_graph


class GraphTest(unittest.TestCase):

    def test_no_nodes(self):
        g = simple_graph.Graph()
        no_nodes = g.nodes()
        assert no_nodes == []
