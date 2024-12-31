import os
import shutil

from textnode import TextNode, TextType
from copystatic import copy_files_recursive
from gencontent import generate_page

def main():
    # Determine the directory where main.py is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define paths relative to script_dir
    static_dir = os.path.join(script_dir, '..', 'static')
    public_dir = os.path.join(script_dir, '..', 'public')
    content_dir = os.path.join(script_dir, '..', 'content')
    template_path = os.path.join(script_dir, '..', 'template.html')

    print("Deleting public directory...")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    print("Copying static files to public directory...")
    copy_files_recursive(static_dir, public_dir)

    print("Generating page...")
    generate_page(
        os.path.join(content_dir, "index.md"),
        template_path,
        os.path.join(public_dir, "index.html"),
    )

    print("All operations completed successfully.")

    # Demonstrate the TextNode usage
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()
