import os
import shutil
from textnode import TextNode, TextType

def copy_directory_contents(src, dest):
    """
    Recursively copies everything from src to dest,
    creating dest if it doesn't already exist.
    """

    # 1) We need to *call* os.path.exists(dest), not just reference os.path.exists
    if not os.path.exists(dest):
        os.mkdir(dest)

    # 2) We also need to *call* os.listdir(src), not just reference os.listdir
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        # Check if 'src_path' is a file or directory
        if os.path.isfile(src_path):
            # It's a file, so copy it
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} -> {dest_path}")
        else:
            # It's a directory, so recurse
            print(f"Entering directory: {src_path}")
            copy_directory_contents(src_path, dest_path)

def main():
    public_dir = "public"
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)

    static_dir = os.path.join("..", "static")
    copy_directory_contents(static_dir, public_dir)

    print("All static files successfully copied to 'public'.")

    # Demonstrate the TextNode usage
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()