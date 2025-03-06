import unittest
from src.web_scraper import WebScraper

class TestWebScraper(unittest.TestCase):
    def test_lookup_definition(self):
        scraper = WebScraper()
        definition = scraper.lookup_definition("apple")
        self.assertNotEqual(definition, "Definition not found.")

if __name__ == "__main__":
    unittest.main()