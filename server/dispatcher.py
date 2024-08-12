import json
import typing

class Dispatcher:
  def __init__(self):
    self.__handlers = {}

  def register_handler(self, command, handler):
    self.__handlers[command] = handler

  def dispatch(self, websocket, raw_data):
    try:
      data = json.loads(raw_data)
      command = data["command"]

      print(f"reccived command {command}")

      if not command in self.__handlers:
        return
      
      self.__handlers[command](websocket, data)
    except json.decoder.JSONDecodeError:
      print(f"cannot parse command {raw_data}")
