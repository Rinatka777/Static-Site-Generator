import unittest
from textnode import TextNode
from textnode import TextType


class TestTextNode(unittest.TestCase):

    # Test that two identical nodes are equal
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    # Additional test case to verify behavior when only text is given
    def test_text_only(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.PLAIN)
        self.assertIsNone(node.url)

    # Test that nodes with different text are not equal
    def test_not_equal_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    # Test that nodes with different text types are not equal
    def test_not_equal_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    # Test that nodes with different URLs are not equal
    def test_not_equal_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        self.assertNotEqual(node, node2)

    # Test that the default URL is None
    def test_default_url(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        self.assertIsNone(node.url)



    # Additional Test Cases for Edge Cases

    # Test that nodes with None URL are not equal to those with actual URLs
    def test_none_url_vs_actual_url(self):
        node_with_none_url = TextNode("This is a text node", TextType.BOLD)
        node_with_actual_url = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node_with_none_url, node_with_actual_url)

    # Test that nodes with different text_type are not equal (enum vs. string)
    def test_text_type_enum_vs_string(self):
        node_enum = TextNode("This is a text node", TextType.BOLD)
        node_enum2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node_enum, node_enum2)

    # Test creating a node with an empty string text
    def test_empty_string_text(self):
        node_empty = TextNode("", TextType.PLAIN)
        node_empty2 = TextNode("", TextType.PLAIN)
        self.assertEqual(node_empty, node_empty2)

    # Test nodes with None as text should not be equal to nodes with actual text
    def test_empty_text_vs_actual_text(self):
        node_empty_text = TextNode("", TextType.PLAIN)
        node_actual_text = TextNode("Some text", TextType.PLAIN)
        self.assertNotEqual(node_empty_text, node_actual_text)


if __name__ == "__main__":
    unittest.main()