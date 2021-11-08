from utilities.path_builder import PathBuilder

class GenConfig:
  def __init__(self, pathBuilder: PathBuilder, kwargs: dict[str, any]):
    """Init configuration for the code generation module."""
    name = kwargs.get("name")
    self.name = name[0].upper() + name[1:]

    self.path = pathBuilder.create_path(kwargs.get("path"))
    self._noGen: str = kwargs.get("n") or ""

  def noReducer(self) -> bool:
    return "r" in self._noGen

  def noState(self) -> bool:
    return "s" in self._noGen

  def noAction(self) -> bool:
    return "a" in self._noGen

  def noEnvironment(self) -> bool:
    return "e" in self._noGen

  def noView(self) -> bool:
    return "v" in self._noGen