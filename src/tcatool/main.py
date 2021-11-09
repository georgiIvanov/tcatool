import sys
import os
import click
from code_generation.code_gen import generate_code
from models.gen_config import GenConfig
from utilities.path_builder import PathBuilder


@click.group()
@click.version_option("0.2.0")
def main():
  """CLI for The Comopsable Architecture"""

@main.command()
@click.argument('name', required=True)
@click.argument('path', required=False)
@click.option('-n', help="""Skip creating file. Use first letter to mark what to exclude.
Example -nae will drop action and environment from being created.""")
def gen(**kwargs):
  """Generates action, state and reducer."""
  path_builder = PathBuilder(os.getcwd())
  config = GenConfig(path_builder, kwargs)
  generate_code(config)

if __name__ == '__main__':
  args = sys.argv
  if "--help" in args or len(args) == 1:
    print("TCA Tool")

  main()
