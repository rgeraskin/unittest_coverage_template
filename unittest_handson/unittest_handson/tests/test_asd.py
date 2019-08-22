from unittest import TestCase

from unittest_handson.asd import Asd


class CoverageTestAsd(TestCase):
    def test_asd_method(self):
        asd = Asd()
        self.assertEqual(asd.asd_method(1, 2), 3)

    def test_b_method(self):
        asd = Asd()
        self.assertEqual(asd.b_method(1, 2), 3)
