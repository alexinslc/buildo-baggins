import unittest
from block import block_to_block_type
from blocktype import BlockType

class TestBlock(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a regular paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        block = "This is a paragraph\nwith multiple lines"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading(self):
        # Test h1
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        # Test h6
        block = "###### Heading 6"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        # Test invalid heading (no space after #)
        block = "#Heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Test invalid heading (too many #)
        block = "####### Invalid heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code(self):
        # Test single line code block
        block = "```print('hello')```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
        # Test multi-line code block
        block = "```\ndef hello():\n    print('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
        # Test invalid code block (missing closing backticks)
        block = "```print('hello')"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote(self):
        # Test single line quote
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
        # Test multi-line quote
        block = "> This is a quote\n> with multiple lines"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
        # Test invalid quote (missing > on one line)
        block = "> This is a quote\nThis is not a quote"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        # Test single item list
        block = "- List item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        # Test multi-item list
        block = "- First item\n- Second item\n- Third item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        # Test invalid list (missing space after -)
        block = "-First item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        # Test single item list
        block = "1. List item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
        # Test multi-item list
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
        # Test invalid list (wrong numbering)
        block = "1. First item\n3. Second item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Test invalid list (missing space after number)
        block = "1.List item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main() 