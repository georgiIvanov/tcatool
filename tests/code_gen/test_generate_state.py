import io
from src.models.gen_config import GenConfig
from src.code_generation.generate_state import generate_state
from src.utilities.path_builder import PathBuilder
from tests.test_case_base import TestCaseBase
from tests.test_utilities import build_output_path, build_expected_path

class TestGenerateState(TestCaseBase):
  def test_create_state(self):
    path_builder = PathBuilder(build_output_path())
    config = GenConfig(
      path_builder,
      {"name": "SignUp", "path": "/SignUp"}
    )
    generate_state(config)

    actual_path = path_builder.create_path("/SignUp") + "/SignUpState.swift"
    expected_output_path = build_expected_path("/generate_state/create_state.swift")
    self.assertListEqual(
      list(io.open(actual_path, encoding="ascii")),
      list(io.open(expected_output_path, encoding="ascii"))
    )

  def test_no_state_option(self):
    path_builder = PathBuilder(build_output_path())
    config = GenConfig(
      path_builder,
      {"name": "SignUp_No", "n": "s"}
    )
    generate_state(config)

    actual_path = path_builder.create_path() + "/SignUp_NoState.swift"
    self.assertIsNotFile(actual_path)
    