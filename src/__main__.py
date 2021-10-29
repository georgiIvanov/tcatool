import sys
import click
from code_gen import generate_code


@click.group()
@click.version_option("0.1.0")
def main():
  """CLI for The Comopsable Architecture"""
  print("Hi!")
  pass


if __name__ == '__main__':
  args = sys.argv
  if "--help" in args or len(args) == 1:
    print("TCA Tool")
  main()