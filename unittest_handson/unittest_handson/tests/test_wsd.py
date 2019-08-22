from unittest import TestCase

from unittest_handson.wsd import Wsd


class CoverageTestWsd(TestCase):
    def test_asd_method(self):
        asd = Wsd()
        self.assertEqual(asd.asd_method(1, 2), 3)

    def test_b_method(self):
        asd = Wsd()
        self.assertEqual(asd.b_method(1, 2), 3)
