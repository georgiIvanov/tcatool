import unittest
from unittest.mock import patch

from click.testing import CliRunner
from models.gen_config import GenConfig
from src.tcatool.main import main
from test_utilities import get_last_part_of_path, get_config_args

class Test_Cli_Commands(unittest.TestCase):

  @patch('src.tcatool.main.generate_code')
  def test_gen_default(self, generate_code):
    runner = CliRunner()
    runner.invoke(main, ["gen", "Foo", "/FooPath"])
    config = get_config_args(generate_code)

    self.assertEqual(config.name, "Foo")
    self.assertEqual(get_last_part_of_path(config.path), "FooPath")

  @patch('src.tcatool.main.generate_code')
  def test_gen_dot_path(self, generate_code):
    runner = CliRunner()
    runner.invoke(main, ["gen", "Foo", "."])
    config = get_config_args(generate_code)

    self.assertEqual(config.name, "Foo")
    self.assertEqual(get_last_part_of_path(config.path), "tcatool")

  @patch('src.tcatool.main.generate_code')
  def test_gen_slash_path(self, generate_code):
    runner = CliRunner()
    runner.invoke(main, ["gen", "Foo", "/"])
    config = get_config_args(generate_code)

    self.assertEqual(config.name, "Foo")
    self.assertEqual(get_last_part_of_path(config.path), "tcatool")

  @patch('src.tcatool.main.generate_code')
  def test_gen_slash_append(self, generate_code):
    runner = CliRunner()
    runner.invoke(main, ["gen", "Foo", "FooPath/"])
    config = get_config_args(generate_code)

    self.assertEqual(config.name, "Foo")
    self.assertEqual(get_last_part_of_path(config.path), "FooPath")


  @patch('src.tcatool.main.generate_code')
  def test_gen_no_option(self, generate_code):
    runner = CliRunner()
    runner.invoke(main, ["gen", "Foo", "FooPath/", "-naesrv"])
    config = get_config_args(generate_code)

    self.assertEqual(config.name, "Foo")
    self.assertEqual(config.noGen, "aesrv")
    self.assertEqual(get_last_part_of_path(config.path), "FooPath")