from typing import Literal


class MotorPerformanceEntry:
  def __init__(
      self,
      throttle: float,
      thrust: float,
      torque: float,
  ):
    self.throttle = throttle
    self.thrust = thrust
    self.torque = torque

  @classmethod
  def from_dict(cls, data):
    return MotorPerformanceEntry(
      throttle = data["throttle"],
      thrust = data["thrust"],
      torque = data["torque"],
    )


class Motor:
  def __init__(
      self,
      name: str,
      direction: Literal["cw", "ccw"],
      position: tuple[float, float, float],
      react_speed: float,
      performance: list[MotorPerformanceEntry],
  ):
    self.name = name
    self.direction = direction
    self.position = position
    self.react_speed = react_speed
    self.performance = performance

  @classmethod
  def from_dict(cls, data):
    performance = []

    for performance_entry_data in data["performance"]:
      performance.append(MotorPerformanceEntry.from_dict(performance_entry_data))

    return Motor(
      name = data["name"],
      direction = data["direction"],
      position = data["position"],
      react_speed = data["reactSpeed"],
      performance = performance,
    )
