import unittest
from find_file import File

class TestFile(unittest.TestCase):

    def setUp(self):
        file = File()

    def tearDown(self):
        pass

    def test_source_folder(self):
        self.assertEqual(file.find_attachment("Downloads")


if __name__ == '__main__':
    unittest.main()