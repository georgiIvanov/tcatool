from utilities.path_builder import PathBuilder

class GenConfig:
  def __init__(self, pathBuilder: PathBuilder, kwargs: dict[str, any]):
    """Init configuration for the code generation module."""
    name = kwargs.get("name")
    self.name = name[0].upper() + name[1:]

    self.path = pathBuilder.create_path(kwargs.get("path"))
    self._no_gen: str = kwargs.get("n") or ""

  def no_reducer(self) -> bool:
    return "r" in self._no_gen

  def no_state(self) -> bool:
    return "s" in self._no_gen

  def no_action(self) -> bool:
    return "a" in self._no_gen

  def no_environment(self) -> bool:
    return "e" in self._no_gen

  def no_view(self) -> bool:
    return "v" in self._no_gen

  def name_camelcase(self) -> str:
    return ''.join([self.name[0].lower(), self.name[1:]])
