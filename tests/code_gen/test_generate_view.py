import io
from src.models.gen_config import GenConfig
from src.code_generation.generate_view import generate_view
from src.utilities.path_builder import PathBuilder
from tests.test_case_base import TestCaseBase
from tests.test_utilities import build_output_path, build_expected_path

class TestGenerateView(TestCaseBase):
  def test_create_view(self):
    path_builder = PathBuilder(build_output_path())
    config = GenConfig(
      path_builder,
      {"name": "SignUp", "path": "/SignUp"}
    )
    generate_view(config)

    actual_path = path_builder.create_path("/SignUp") + "/SignUpView.swift"
    expected_output_path = build_expected_path("/generate_view/create_view.swift")
    self.assertListEqual(
      list(io.open(actual_path, encoding="ascii")),
      list(io.open(expected_output_path, encoding="ascii"))
    )


  def test_no_view_option(self):
    path_builder = PathBuilder(build_output_path())
    config = GenConfig(
      path_builder,
      {"name": "SignUp_No", "n": "aerv"}
    )
    generate_view(config)

    actual_path = path_builder.create_path() + "/SignUp_NoView.swift"
    self.assert_not_file(actual_path)
