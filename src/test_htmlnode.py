import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_def(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        props = {
            "test" : "test/link.html",
            "check" : "this/out.png",
        }
        node = HTMLNode(props=props)
        self.assertRegex(node.props_to_html(), r'(?:\s{1}[\w:-]+="[^"]*")*')

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()