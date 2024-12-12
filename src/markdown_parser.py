def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    return [block.strip() for block in blocks if block.strip()]

def block_to_block_type(markdown):
    # Strip leading/trailing whitespace
    markdown = markdown.strip()
    
    # Split block into lines for multi-line checks
    lines = markdown.splitlines()

    # Check for code blocks
    if markdown.startswith("```") and markdown.endswith("```"):
        return "code"

    # Check for quotes
    if all(line.startswith(">") for line in lines):
        return "quote"

    # Check for unordered lists
    if all(line.startswith("* ") or line.startswith("- ") for line in lines):
        return "unordered list"

    # Check for ordered lists
    if all(line.split(". ")[0].isdigit() for line in lines):
        # Validate sequential numbering
        expected_number = 1
        for line in lines:
            actual_number = int(line.split(". ")[0])
            if actual_number != expected_number:
                return "paragraph"  # Invalid numbering
            expected_number += 1
        return "ordered list"

    # Check for headings
    if markdown.startswith("#"):
        count = 0
        for char in markdown:
            if char == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and markdown[count] == " ":
            return "heading"

    # Default case: paragraph
    return "paragraph"

