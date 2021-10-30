import unittest
import io
from src.code_generation.generate_view import generate_view
from src.path_builder import PathBuilder
from tests.test_utilities import build_output_path, build_expected_path

class Test_Generate_Action(unittest.TestCase):
  def test_createView(self):
    fullPath = PathBuilder(build_output_path()).create_path("/SignUp")
    pathAndName = fullPath + "/SignUpView.swift"
    generate_view("SignUp", fullPath)

    expectedOutputPath = build_expected_path("/generate_view/create_view.swift")
    self.assertListEqual(
      list(io.open(pathAndName)),
      list(io.open(expectedOutputPath))
    )

