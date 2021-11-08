import unittest
import pathlib as pl

class TestCaseBase(unittest.TestCase):
  def assert_not_file(self, path):
    """Throws an assertion if a file exists.
    Please take note that you probably need to delete the file manually to retry test.
    """

    if pl.Path(path).resolve().is_file():
      raise AssertionError(f"File exists at path: {str(path)}")
