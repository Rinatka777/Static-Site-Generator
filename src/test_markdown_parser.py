from markdown_parser import markdown_to_blocks

def test_markdown_to_blocks():
    # Test 1: Basic case - two simple blocks
    markdown = "First block\n\nSecond block"
    expected = ["First block", "Second block"]
    result = markdown_to_blocks(markdown)
    assert result == expected

    # Test 2: Handle extra whitespace
    markdown = "  Block with spaces  \n\n  Another block  "
    expected = ["Block with spaces", "Another block"]
    result = markdown_to_blocks(markdown)
    assert result == expected

    #Test 3: single block
    markdown = "Only 1 block"
    expected = ["Only 1 block"]
    result = markdown_to_blocks(markdown)
    assert result == expected

    #Test 4: empty string
    markdown = ""
    expected = []
    result = markdown_to_blocks(markdown)
    assert result == expected
    
    #Test 5: Multiple consecutive empty lines
    markdown = "Block 1\n\n\n\nBlock 2"
    expected = ["Block 1", "Block 2"]
    result = markdown_to_blocks(markdown)
    assert result == expected

    #Test 6: multi-line block
    markdown = "* Line 1\n* Line 2\n* Line 3\n\nNext block"
    expected = ["* Line 1\n* Line 2\n* Line 3", "Next block"]
    result = markdown_to_blocks(markdown)
    assert result == expected