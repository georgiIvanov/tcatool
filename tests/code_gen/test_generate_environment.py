import io
from src.models.gen_config import GenConfig
from src.code_generation.generate_environment import generate_environment
from src.utilities.path_builder import PathBuilder
from tests.test_utilities import build_output_path, build_expected_path
from tests.test_case_base import TestCaseBase

class TestGenerateEnvironment(TestCaseBase):
  def test_create_environment(self):
    path_builder = PathBuilder(build_output_path())
    config = GenConfig(
      path_builder,
      {"name": "app", "path": "/App"}
    )
    generate_environment(config)

    actual_path = path_builder.create_path("/App") + "/AppEnvironment.swift"
    expected_output_path = build_expected_path("/generate_environment/create_app_environment.swift")
    self.assertListEqual(
      list(io.open(actual_path, encoding="ascii")),
      list(io.open(expected_output_path, encoding="ascii"))
    )

  def test_no_environment(self):
    path_builder = PathBuilder(build_output_path())
    config = GenConfig(
      path_builder,
      {"name": "App_No", "n": "aerv"}
    )
    generate_environment(config)

    actual_path = path_builder.create_path() + "/App_NoEnvironment.swift"
    self.assert_not_file(actual_path)
