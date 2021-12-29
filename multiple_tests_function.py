import unittest
from eleven_chapter_function import get_formatted_name

class FullNameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('khojiakbar', 'isomiddinov')
        self.assertEqual(formatted_name, 'Khojiakbar Isomiddinov')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('khojiakbar', 'isomiddinov', 'shukhrat ugli')
        self.assertEqual(formatted_name, 'Khojiakbar Shukhrat Ugli Isomiddinov')

if __name__ == '__main__':
    unittest.main()