import unittest
import io
from src.models.gen_config import GenConfig
from src.code_generation.generate_view import generate_view
from src.utilities.path_builder import PathBuilder
from tests.test_utilities import build_output_path, build_expected_path

class Test_Generate_Action(unittest.TestCase):
  def test_createView(self):
    pathBuilder = PathBuilder(build_output_path())
    config = GenConfig(
      pathBuilder,
      {"name": "SignUp", "path": "/SignUp"}
    )
    generate_view(config)

    pathAndName = pathBuilder.create_path("/SignUp") + "/SignUpView.swift"
    expectedOutputPath = build_expected_path("/generate_view/create_view.swift")
    self.assertListEqual(
      list(io.open(pathAndName)),
      list(io.open(expectedOutputPath))
    )


