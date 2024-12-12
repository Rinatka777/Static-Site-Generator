
from textnode import TextNode
from textnode import TextType

def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # Print the TextNode object
    print(text_node)


# Call the main function
if __name__ == "__main__":
    main()
