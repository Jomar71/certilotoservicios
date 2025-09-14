import unittest
from pdf_generator import generate_pdf

class TestPDFGenerator(unittest.TestCase):
    def test_generate_pdf(self):
        filename = generate_pdf("John", "Doe", "123456789", "Ciudad", "Enero")
        self.assertTrue(filename.endswith(".pdf"))

if __name__ == '__main__':
    unittest.main()