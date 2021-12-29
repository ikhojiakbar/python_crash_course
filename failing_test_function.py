import unittest
from eleven_chapter_function import get_formatted_name

class FullNameTestCase(unittest.TestCase):

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('khojiakbar', 'shukhrat', 'ugli', 'isomiddinov')   # 4 attributes instead of 2/3 were given
        self.assertEqual(formatted_name, 'Khojiakbar Shukhrat Ugli Isomiddinov')

if __name__ == '__main__':
    unittest.main()