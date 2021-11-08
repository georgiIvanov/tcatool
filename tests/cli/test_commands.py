import unittest
from unittest.mock import patch

from click.testing import CliRunner
from src.tcatool.main import main
from test_utilities import get_last_part_of_path

class Test_Cli_Commands(unittest.TestCase):

  @patch('src.tcatool.main.generate_code')
  def test_gen_default(self, generate_code):
    runner = CliRunner()
    runner.invoke(main, ["gen", "Foo", "/FooPath"])
    args, kwargs = generate_code.call_args

    self.assertEqual(args[0], "Foo")
    self.assertEqual(get_last_part_of_path(args[1]), "FooPath")

  @patch('src.tcatool.main.generate_code')
  def test_gen_dot_path(self, generate_code):
    runner = CliRunner()
    runner.invoke(main, ["gen", "Foo", "."])
    args, kwargs = generate_code.call_args

    self.assertEqual(args[0], "Foo")
    self.assertEqual(get_last_part_of_path(args[1]), "tcatool")

  @patch('src.tcatool.main.generate_code')
  def test_gen_slash_path(self, generate_code):
    runner = CliRunner()
    runner.invoke(main, ["gen", "Foo", "/"])
    args, kwargs = generate_code.call_args

    self.assertEqual(args[0], "Foo")
    self.assertEqual(get_last_part_of_path(args[1]), "tcatool")

  @patch('src.tcatool.main.generate_code')
  def test_gen_slash_append(self, generate_code):
    runner = CliRunner()
    runner.invoke(main, ["gen", "Foo", "FooPath/"])
    args, kwargs = generate_code.call_args

    self.assertEqual(args[0], "Foo")
    self.assertEqual(get_last_part_of_path(args[1]), "FooPath")