import unittest

from drone_model.drone import Drone


class TestBodyPart(unittest.TestCase):
    def test_from_json(self):
        json_content = """
          {
            "bodyParts": [
              {
                "name": "body",
                "type": "cube",
                "dimension": [ 30.0, 200.0, 30.0 ],
                "position": [ 0.0, -10.0, 0.0 ],
                "rotation": [ 0.0, 0.0, 0.0 ],
                "weight": 500.0
              }
            ],
            "motors": [
              {
                "name": "motor-fr",
                "direction": "ccw",
                "position": [
                  71.0, 71.0, 0.0
                ],
                "reactSpeed": 0.03,
                "performance": [
                  { "throttle": 0.0, "thrust": 0.0, "torque": 0.0 },
                  { "throttle": 100.0, "thrust": 566.0, "torque": 0.1073771356 }
                ]
              }
            ]
          }
        """
        drone = Drone.from_json(json_content)

        body_part = drone.body_parts[0]

        self.assertEqual(body_part.name, "body")
        self.assertEqual(body_part.type, "cube")
        self.assertListEqual(body_part.dimension, [30.0, 200.0, 30.0])
        self.assertListEqual(body_part.position, [0.0, -10.0, 0.0])
        self.assertListEqual(body_part.rotation, [0.0, 0.0, 0.0])
        self.assertEqual(body_part.weight, 500.0)

        motor = drone.motors[0]

        self.assertEqual(motor.name, "motor-fr")
        self.assertEqual(motor.direction, "ccw")
        self.assertListEqual(motor.position, [71.0, 71.0, 0.0])
        self.assertEqual(motor.react_speed, 0.03)

        self.assertEqual(motor.performance[0].throttle, 0.0)
        self.assertEqual(motor.performance[0].thrust, 0.0)
        self.assertEqual(motor.performance[0].torque, 0.0)

        self.assertEqual(motor.performance[1].throttle, 100.0)
        self.assertEqual(motor.performance[1].thrust, 566.0)
        self.assertEqual(motor.performance[1].torque, 0.1073771356)


if __name__ == '__main__':
    unittest.main()
