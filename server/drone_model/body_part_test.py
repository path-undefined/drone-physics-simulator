import unittest
import json

from drone_model.body_part import BodyPart

class TestBodyPart(unittest.TestCase):
  def test_from_dict(self):
    json_content = """
      {
        "name": "body",
        "type": "cube",
        "dimension": [ 30.0, 200.0, 30.0 ],
        "position": [ 0.0, -10.0, 0.0 ],
        "rotation": [ 0.0, 0.0, 0.0 ],
        "weight": 500.0
      }
    """
    data = json.loads(json_content)
    body_part = BodyPart.from_dict(data)

    self.assertEqual(body_part.name, "body")
    self.assertEqual(body_part.type, "cube")
    self.assertListEqual(body_part.dimension, [ 30.0, 200.0, 30.0 ])
    self.assertListEqual(body_part.position, [ 0.0, -10.0, 0.0 ])
    self.assertListEqual(body_part.rotation, [ 0.0, 0.0, 0.0 ])
    self.assertEqual(body_part.weight, 500.0)

if __name__ == '__main__':
  unittest.main()
