import unittest
import io
from models.gen_config import GenConfig
from src.code_generation.generate_action import generate_action
from src.utilities.path_builder import PathBuilder
from tests.test_utilities import build_output_path, build_expected_path

class Test_Generate_Action(unittest.TestCase):
  def test_createAction(self):
    pathBuilder = PathBuilder(build_output_path())
    config = GenConfig(
      pathBuilder,
      {"name": "profile", "path": "/Profile"}
    )
    generate_action(config)

    pathAndName = pathBuilder.create_path("/Profile") + "/ProfileAction.swift"
    expectedOutputPath = build_expected_path("/generate_action/create_action.swift")
    self.assertListEqual(
      list(io.open(pathAndName)),
      list(io.open(expectedOutputPath))
    )


