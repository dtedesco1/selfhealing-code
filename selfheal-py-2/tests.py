import unittest
import output
import wikipediaapi

class TestOutput(unittest.TestCase):

    def test_install_libraries(self):
        output.install_libraries()
        self.assertTrue(hasattr(output, "requests"))
        self.assertTrue(hasattr(output, "wikipediaapi"))

    def test_search_attractions(self):
        query = "Tourism_in_Paris"
        result = output.search_attractions(query)
        self.assertTrue(isinstance(result, wikipediaapi.WikipediaPage))

    def test_extract_relevant_sections(self):
        query = "Tourism_in_Paris"
        page = output.search_attractions(query)
        sections = output.extract_relevant_sections(page)
        self.assertTrue(len(sections) > 0)

    def test_parse_attractions(self):
        query = "Tourism_in_Paris"
        page = output.search_attractions(query)
        sections = output.extract_relevant_sections(page)
        attractions = output.parse_attractions(sections)
        self.assertEqual(len(attractions), 5)

    def test_display_results(self):
        attractions = [('Attraction 1', 'Description 1'), ('Attraction 2', 'Description 2')]
        with self.assertLogs() as captured:
            output.display_results(attractions)
            self.assertEqual(len(captured.records), 2)
            self.assertIn("Attraction 1", captured.output[0])
            self.assertIn("Description 1", captured.output[0])
            self.assertIn("Attraction 2", captured.output[1])
            self.assertIn("Description 2", captured.output[1])


if __name__ == '__main__':
    unittest.main()