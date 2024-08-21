import asyncio
import websockets
from dispatcher import Dispatcher
from simulation import Simulation
from handler_start import create_start_handler
from handler_stop import create_stop_handler

simulation = Simulation()

dispatcher = Dispatcher()
dispatcher.register_handler("start", create_start_handler(simulation))
dispatcher.register_handler("stop", create_stop_handler(simulation))


async def on_connect(websocket):
    print("received new connection")
    while True:
        try:
            raw_data = await websocket.recv()
            dispatcher.dispatch(websocket, raw_data)
        except websockets.ConnectionClosedOK:
            print("connection closed")
            break


async def main():
    async with websockets.serve(on_connect, "", 3000):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
