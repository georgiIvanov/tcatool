from utilities.path_builder import PathBuilder

class GenConfig:
  def __init__(self, pathBuilder: PathBuilder, kwargs: dict[str, any]):
    """Init configuration for the code generation module."""
    self.pathBuilder = pathBuilder
    self.name = kwargs.get("name").capitalize()
    self.path = pathBuilder.create_path(kwargs.get("path"))
    self.noGen = kwargs.get("n")

