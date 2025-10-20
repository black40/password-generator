import string
import unittest

from app.gui import Root


class DummyCheckBox:
    def __init__(self, active):
        self.active = active


class TestPasswordGeneratorGUI(unittest.TestCase):
    def setUp(self):
        self.root = Root()

    def test_generate_default_length(self):
        self.root.ids.clear()
        self.root.ids.update({
            'letters': DummyCheckBox(True),
            'numbers': DummyCheckBox(True),
            'symbols': DummyCheckBox(True),
        })
        pw = self.root.generate_password()
        self.assertEqual(len(pw), 8)

    def test_generate_custom_length(self):
        self.root.ids.clear()
        self.root.ids.update({
            'letters': DummyCheckBox(True),
            'numbers': DummyCheckBox(True),
            'symbols': DummyCheckBox(True),
        })
        pw = self.root.generate_password('16')
        self.assertEqual(len(pw), 16)

    def test_generate_min_length(self):
        self.root.ids.clear()
        self.root.ids.update({
            'letters': DummyCheckBox(True),
            'numbers': DummyCheckBox(True),
            'symbols': DummyCheckBox(True),
        })
        pw = self.root.generate_password('2')
        self.assertEqual(len(pw), 4)  # min length is 4

    def test_generate_max_length(self):
        self.root.ids.clear()
        self.root.ids.update({
            'letters': DummyCheckBox(True),
            'numbers': DummyCheckBox(True),
            'symbols': DummyCheckBox(True),
        })
        pw = self.root.generate_password('100')
        self.assertEqual(len(pw), 64)  # max length is 64

    def test_letters_only(self):
        self.root.ids.clear()
        self.root.ids.update({
            'letters': DummyCheckBox(True),
            'numbers': DummyCheckBox(False),
            'symbols': DummyCheckBox(False),
        })
        pw = self.root.generate_password('12')
        self.assertTrue(all(c in string.ascii_letters for c in pw))

    def test_digits_only(self):
        self.root.ids.clear()
        self.root.ids.update({
            'letters': DummyCheckBox(False),
            'numbers': DummyCheckBox(True),
            'symbols': DummyCheckBox(False),
        })
        pw = self.root.generate_password('12')
        self.assertTrue(all(c in string.digits for c in pw))

    def test_symbols_only(self):
        self.root.ids.clear()
        self.root.ids.update({
            'letters': DummyCheckBox(False),
            'numbers': DummyCheckBox(False),
            'symbols': DummyCheckBox(True),
        })
        pw = self.root.generate_password('12')
        self.assertTrue(all(c in string.punctuation for c in pw))

    def test_letters_and_digits(self):
        self.root.ids.clear()
        self.root.ids.update({
            'letters': DummyCheckBox(True),
            'numbers': DummyCheckBox(True),
            'symbols': DummyCheckBox(False),
        })
        pw = self.root.generate_password('20')
        self.assertTrue(any(c in string.ascii_letters for c in pw))
        self.assertTrue(any(c in string.digits for c in pw))

if __name__ == '__main__':
    unittest.main()
