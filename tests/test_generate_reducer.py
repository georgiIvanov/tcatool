import unittest
import io
from src.code_generation.generate_reducer import generate_reducer
from src.path_builder import PathBuilder
from tests.test_utilities import build_output_path, build_expected_path

class Test_Generate_Action(unittest.TestCase):
  def test_createReducer(self):
    fullPath = PathBuilder(build_output_path()).create_path("/SignUp")
    pathAndName = fullPath + "/SignUpReducer.swift"
    generate_reducer("SignUp", fullPath)

    expectedOutputPath = build_expected_path("/generate_reducer/create_reducer.swift")
    self.assertListEqual(
      list(io.open(pathAndName)),
      list(io.open(expectedOutputPath))
    )


