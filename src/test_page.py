import unittest
import os
import shutil
from page import extract_title, generate_page

class TestPage(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")
        
        markdown = "#  Hello World  "
        self.assertEqual(extract_title(markdown), "Hello World")
        
        markdown = "## Not a title\n# This is a title"
        self.assertEqual(extract_title(markdown), "This is a title")
        
        markdown = "No title here"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_generate_page(self):
        # Create test directories
        os.makedirs("test_content", exist_ok=True)
        os.makedirs("test_public", exist_ok=True)
        
        # Create test files
        with open("test_content/test.md", "w") as f:
            f.write("# Test Title\n\nTest content")
        
        with open("test_template.html", "w") as f:
            f.write("<!DOCTYPE html><html><head><title>{{ Title }}</title></head><body>{{ Content }}</body></html>")
        
        # Generate the page
        generate_page("test_content/test.md", "test_template.html", "test_public/test.html")
        
        # Read the generated file
        with open("test_public/test.html", "r") as f:
            content = f.read()
        
        # Check the content
        self.assertIn("Test Title", content)
        self.assertIn("Test content", content)
        
        # Clean up
        shutil.rmtree("test_content")
        shutil.rmtree("test_public")
        os.remove("test_template.html")

if __name__ == "__main__":
    unittest.main() 