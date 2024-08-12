from simulation import Simulation

def create_start_handler(simulation: Simulation):
  def handle_start(websocket, data):
    print("starting simulation ...")
    simulation.start(websocket)

  return handle_start
