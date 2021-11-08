from utilities.path_builder import PathBuilder

class GenConfig:
  def __init__(self, pathBuilder: PathBuilder, kwargs: dict[str, any]):
    """Init configuration for the code generation module."""
    name = kwargs.get("name")
    self.name = name[0].upper() + name[1:]

    self.path = pathBuilder.create_path(kwargs.get("path"))
    self.noGen = kwargs.get("n")

