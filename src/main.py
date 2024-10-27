import re
from textnode import TextNode
from textnode import TextType

def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # Print the TextNode object
    print(text_node)

# Call the main function
if __name__ == "__main__":
    main()

def extract_markdown_images(text):
    matches_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return (matches_images)
def extract_markdown_links(text):
    matches_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return (matches_links)