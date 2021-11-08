import unittest
import io
from src.models.gen_config import GenConfig
from src.code_generation.generate_environment import generate_environment
from src.utilities.path_builder import PathBuilder
from tests.test_utilities import build_output_path, build_expected_path

class Test_Generate_Action(unittest.TestCase):
  def test_createEnvironment(self):
    pathBuilder = PathBuilder(build_output_path())
    config = GenConfig(
      pathBuilder,
      {"name": "app", "path": "/App"}
    )
    generate_environment(config)

    pathAndName = pathBuilder.create_path("/App") + "/AppEnvironment.swift"
    expectedOutputPath = build_expected_path("/generate_environment/create_app_environment.swift")
    self.assertListEqual(
      list(io.open(pathAndName)),
      list(io.open(expectedOutputPath))
    )


