import unittest
import cap

# Create a test class that inherit from unit test
class TestCap(unittest.TestCase):

    # Make the test function
    def test_one_word(self):
        text = 'python'
        # Call whatever function you want to test
        result = cap.cap_text(text)
        # Verify that the results are what you expected
        self.assertEqual(result, 'Python')

    # Make as many tests as you need
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__=='__main__':
    unittest.main()