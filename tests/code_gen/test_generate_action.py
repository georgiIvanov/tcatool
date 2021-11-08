import io
from models.gen_config import GenConfig
from src.code_generation.generate_action import generate_action
from src.utilities.path_builder import PathBuilder
from tests.test_utilities import build_output_path, build_expected_path
from tests.test_case_base import TestCaseBase

class TestGenerateAction(TestCaseBase):
  def test_create_action(self):
    path_builder = PathBuilder(build_output_path())
    config = GenConfig(
      path_builder,
      {"name": "profile", "path": "/Profile"}
    )
    generate_action(config)

    actual_path = path_builder.create_path("/Profile") + "/ProfileAction.swift"
    expected_output_path = build_expected_path("/generate_action/create_action.swift")
    self.assertListEqual(
      list(io.open(actual_path, encoding="ascii")),
      list(io.open(expected_output_path, encoding="ascii"))
    )

  def test_no_action(self):
    path_builder = PathBuilder(build_output_path())
    config = GenConfig(
      path_builder,
      {"name": "Profile_No", "n": "vera"}
    )
    generate_action(config)

    actual_path = path_builder.create_path() + "/Profile_NoAction.swift"
    self.assertIsNotFile(actual_path)
  