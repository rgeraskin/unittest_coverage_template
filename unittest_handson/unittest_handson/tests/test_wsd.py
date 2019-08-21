# from unittest import TestCase

import unittest_handson.wsd
from unittest_handson._coverage import CoverageTestCase as TestCase


class CoverageTestWsd(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.Wsd = cls.setUpCoverage(unittest_handson.wsd, "Wsd")

    def test_asd_method(self):
        asd = self.Wsd()
        self.assertEqual(asd.asd_method(1, 2), 3)

    def test_b_method(self):
        asd = self.Wsd()
        self.assertEqual(asd.b_method(1, 2), 3)
