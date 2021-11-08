import unittest
import pathlib as pl

class TestCaseBase(unittest.TestCase):
    def assertIsNotFile(self, path):
      """Throws an assertion if a file exists. 
      Please take note that you probably need to delete the file manually to retry test.
      """
      
      if pl.Path(path).resolve().is_file():
        raise AssertionError("File exists at path: %s" % str(path))