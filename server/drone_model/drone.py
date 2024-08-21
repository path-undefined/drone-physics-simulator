import json

from drone_model.body_part import BodyPart
from drone_model.motor import Motor


class Drone:
    def __init__(
        self,
        body_parts: list[BodyPart],
        motors: list[Motor],
    ):
        self.body_parts = body_parts
        self.motors = motors

    @classmethod
    def from_dict(cls, data):
        body_parts = []
        motors = []

        for body_part_data in data["bodyParts"]:
            body_parts.append(BodyPart.from_dict(body_part_data))

        for motor_data in data["motors"]:
            motors.append(Motor.from_dict(motor_data))

        return Drone(
            body_parts=body_parts,
            motors=motors,
        )

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls.from_dict(data)
