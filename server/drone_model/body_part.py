from typing import Literal


class BodyPart:
    def __init__(
        self,
        name: str,
        type: Literal["cube", "stick", "point"],
        dimension: tuple[float, float, float],
        position: tuple[float, float, float],
        rotation: tuple[float, float, float],
        weight: float,
    ):
        self.name = name
        self.type = type
        self.dimension = dimension
        self.position = position
        self.rotation = rotation
        self.weight = weight

    @classmethod
    def from_dict(cls, data):
        return BodyPart(
            name=data["name"],
            type=data["type"],
            dimension=data["dimension"],
            position=data["position"],
            rotation=data["rotation"],
            weight=data["weight"],
        )
