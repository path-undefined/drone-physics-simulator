import asyncio

class Simulation:
  def __init__(self):
    self.__websocket = None
    self.__async_task = None

  def start(self, websocket):
    self.__websocket = websocket
    self.__async_task = asyncio.create_task(self.__simulate())

  def stop(self):
    self.__async_task.cancel()
    self.__async_task = None

  async def __simulate(self):
    pass
