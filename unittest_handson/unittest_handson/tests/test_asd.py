# from unittest import TestCase

import unittest_handson.asd
from unittest_handson._coverage import CoverageTestCase as TestCase


class CoverageTestAsd(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.Asd = cls.setUpCoverage(unittest_handson.asd, "Asd")

    def test_asd_method(self):
        asd = self.Asd()
        self.assertEqual(asd.asd_method(1, 2), 3)

    def test_b_method(self):
        asd = self.Asd()
        self.assertEqual(asd.b_method(1, 2), 3)
