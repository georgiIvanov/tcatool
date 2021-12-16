# pylint: disable=W0212

import unittest
from src.utilities.path_builder import PathBuilder

class TestPathBuilder(unittest.TestCase):
  def test_path_builder_assemble_paths(self):
    path_builder = PathBuilder("test/path")
    self.assertEqual(
      path_builder._assemble_path("."),
      "test/path"
    )

    self.assertEqual(
      path_builder._assemble_path("/"),
      "test/path"
    )

    self.assertEqual(
      path_builder._assemble_path("recipe"),
      "test/path/recipe"
    )

    self.assertEqual(
      path_builder._assemble_path("/recipe"),
      "test/path/recipe"
    )

