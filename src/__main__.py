import sys
import click
from code_gen import generate_code


@click.group()
@click.version_option("0.1.0")
def main():
  """CLI for The Comopsable Architecture"""
  pass

@main.command()
@click.argument('name', required=True)
@click.argument('path', required=False)
def gen(**kwargs):
    """Generates action, state and reducer."""
    generate_code(
      kwargs.get('name'), 
      kwargs.get('path')
    )
    pass

if __name__ == '__main__':
  args = sys.argv
  if "--help" in args or len(args) == 1:
    print("TCA Tool")

main()