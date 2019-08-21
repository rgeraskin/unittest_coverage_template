import importlib
import inspect
from unittest import TestCase

import coverage


class CoverageTestCase(TestCase):
    @classmethod
    def setUpCoverage(cls, module, class_str):
        class_ = getattr(module, class_str)
        cov_file = inspect.getfile(class_)
        cls.cov = coverage.Coverage(include=[cov_file])
        cls.cov.start()
        importlib.reload(module)
        return class_

    @classmethod
    def tearDownClass(cls, *args, **kwargs) -> None:
        cls.cov.stop()
        cls.cov.report(skip_covered=True, show_missing=True)
