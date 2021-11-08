import io
from src.models.gen_config import GenConfig
from src.code_generation.generate_reducer import generate_reducer
from src.utilities.path_builder import PathBuilder
from tests.test_case_base import TestCaseBase
from tests.test_utilities import build_output_path, build_expected_path

class TestGenerateReducer(TestCaseBase):
  def test_create_reducer(self):
    path_builder = PathBuilder(build_output_path())
    config = GenConfig(
      path_builder,
      {"name": "SignUp", "path": "/SignUp"}
    )
    generate_reducer(config)

    actual_path = path_builder.create_path("/SignUp") + "/SignUpReducer.swift"
    expected_output_path = build_expected_path("/generate_reducer/create_reducer.swift")
    self.assertListEqual(
      list(io.open(actual_path, encoding="ascii")),
      list(io.open(expected_output_path, encoding="ascii"))
    )

  def test_no_reducer_option(self):
    path_builder = PathBuilder(build_output_path())
    config = GenConfig(
      path_builder,
      {"name": "SignUp_No", "n": "r"}
    )
    generate_reducer(config)

    actual_path = path_builder.create_path() + "/SignUp_NoReducer.swift"
    self.assertIsNotFile(actual_path)
