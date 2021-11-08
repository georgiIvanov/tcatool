import sys
import click
import os
from code_generation.code_gen import generate_code
from models.gen_config import GenConfig
from utilities.path_builder import PathBuilder


@click.group()
@click.version_option("0.1.0")
def main():
  """CLI for The Comopsable Architecture"""

@main.command()
@click.argument('name', required=True)
@click.argument('path', required=False)
@click.option('-n', help='Skip creating file. Use first letter to mark what to exclude. Example -nae will drop action and environment from being created.')
def gen(**kwargs):
    """Generates action, state and reducer."""
    pathBuilder = PathBuilder(os.getcwd())
    config = GenConfig(pathBuilder, kwargs)
    generate_code(config)

if __name__ == '__main__':
  args = sys.argv
  if "--help" in args or len(args) == 1:
    print("TCA Tool")
  
  main()