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

    def test_edges(self):
        g = simple_graph.Graph()
        g.edges_list = [simple_graph.Edge(), simple_graph.Edge()]
        assert len(g.edges()) == 2

    def test_add_node(self):
        g = simple_graph.Graph()
        new_node = simple_graph.Node()
        g.add_node(new_node)
        assert len(g.nodes()) == 1

    def test_add_edge(self):
        g = simple_graph.Graph()
        new_node1 = simple_graph.Node()
        new_node2 = simple_graph.Node()
        g.add_edge(new_node1, new_node2)
        assert g.edges()[0].n1 == new_node1
        assert g.edges()[0].n2 == new_node2

    def test_add_edge_nodes(self):
        g = simple_graph.Graph()
        new_node1 = simple_graph.Node()
        new_node2 = simple_graph.Node()
        g.add_edge(new_node1, new_node2)
        assert new_node1 in g.nodes()
        assert new_node2 in g.nodes()

    def test_del_node_exists(self):
        g = simple_graph.Graph()
        new_node = simple_graph.Node('hello')
        g.add_node(new_node)
        g.del_node(new_node)
        assert len(g.nodes()) == 0

    def test_del_node_not_exist(self):
        g = simple_graph.Graph()
        new_node1 = simple_graph.Node('hello')
        new_node2 = simple_graph.Node('goodbye')
        g.add_node(new_node1)
        with self.assertRaises(IndexError) as context:
            g.del_node(new_node2)
        self.assertEqual(context.exception.message,
                         u"Node does not exist in graph.")

    def test_del_node_deletes_edges(self):
        g = simple_graph.Graph()
        new_node1 = simple_graph.Node()
        new_node2 = simple_graph.Node()
        g.add_edge(new_node1, new_node2)
        g.del_node(new_node1)
        assert len(g.nodes()) == 1
        assert len(g.edges()) == 0

    def test_del_edge_exists(self):
        g = simple_graph.Graph()
        new_node1 = simple_graph.Node()
        new_node2 = simple_graph.Node()
        g.add_edge(new_node1, new_node2)
        g.del_edge(new_node1, new_node2)
        assert len(g.edges()) == 0

    def test_del_edge_not_exists(self):
        g = simple_graph.Graph()
        new_node1 = simple_graph.Node()
        new_node2 = simple_graph.Node()
        new_node3 = simple_graph.Node('nope')
        g.add_edge(new_node1, new_node2)
        with self.assertRaises(IndexError) as context:
            g.del_edge(new_node1, new_node3)
        self.assertEqual(context.exception.message, u"Edge does not exist \
in graph.")
        assert len(g.edges()) == 1


if __name__ == '__main__':
    unittest.main()
