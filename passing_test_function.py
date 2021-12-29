import unittest
from eleven_chapter_function import get_formatted_name

class FullNameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('khojiakbar', 'isomiddinov')
        self.assertEqual(formatted_name, 'Khojiakbar Isomiddinov')


if __name__ == '__main__':      #pycharm needs this extra line
    unittest.main()