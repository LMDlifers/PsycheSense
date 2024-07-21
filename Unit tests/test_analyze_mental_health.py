import unittest
from Backend.analyze_mental_health import analyze_mental_health

class TestAnalyzeMentalHealth(unittest.TestCase):

    def test_analyze_mental_health_valid_input(self):
        embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
        result = analyze_mental_health(embeddings)
        self.assertEqual(result['summary'], "Analysis completed successfully.")
    
    def test_analyze_mental_health_empty_input(self):
        embeddings = []
        with self.assertRaises(ValueError) as context:
            analyze_mental_health(embeddings)
        self.assertTrue("Embeddings cannot be empty" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
