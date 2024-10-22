import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

# New Test Cases
    def test_leafnode_to_html_with_tag(self):
        # Test rendering of LeafNode with a tag and properties
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leafnode_to_html_without_tag(self):
        # Test rendering of LeafNode without a tag (should return value as raw text)
        node = LeafNode(
            None,
            "Just some raw text",
        )
        self.assertEqual(
            node.to_html(),
            "Just some raw text",
        )

    def test_leafnode_value_error(self):
        # Test that a LeafNode without a value raises a ValueError
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    def test_htmlnode_children(self):
        # Test that HTMLNode can properly have children nodes
        child1 = HTMLNode("span", "Child 1")
        child2 = HTMLNode("span", "Child 2")
        parent = HTMLNode("div", None, [child1, child2])
        
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0].tag, "span")
        self.assertEqual(parent.children[1].value, "Child 2")

    def test_htmlnode_to_html_with_children(self):
        # Test that HTMLNode renders with children nodes properly
        child1 = HTMLNode("span", "Child 1")
        child2 = HTMLNode("span", "Child 2")
        parent = HTMLNode("div", None, [child1, child2])
        
        expected_html = (
            "<div>"
            "<span>Child 1</span>"
            "<span>Child 2</span>"
            "</div>"
        )
        parent_html = f"<{parent.tag}>{''.join([child.to_html() for child in parent.children])}</{parent.tag}>"
        self.assertEqual(parent_html, expected_html)

if __name__ == "__main__":
    unittest.main()