import unittest
import io
from src.models.gen_config import GenConfig
from src.code_generation.generate_state import generate_state
from src.utilities.path_builder import PathBuilder
from tests.test_utilities import build_output_path, build_expected_path

class Test_Generate_Action(unittest.TestCase):
  def test_createState(self):
    pathBuilder = PathBuilder(build_output_path())
    config = GenConfig(
      pathBuilder,
      {"name": "SignUp", "path": "/SignUp"}
    )
    generate_state(config)

    pathAndName = pathBuilder.create_path("/SignUp") + "/SignUpState.swift"
    expectedOutputPath = build_expected_path("/generate_state/create_state.swift")
    self.assertListEqual(
      list(io.open(pathAndName)),
      list(io.open(expectedOutputPath))
    )


