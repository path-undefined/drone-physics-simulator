import unittest
import json

from drone_model.motor import Motor


class TestMotor(unittest.TestCase):
    def test_from_dict(self):
        json_content = """
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
        """
        data = json.loads(json_content)
        motor = Motor.from_dict(data)

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
