from simulation import Simulation


def create_stop_handler(simulation: Simulation):
    def handle_stop(websocket, data):
        print("stopping simulation ...")
        simulation.stop()

    return handle_stop
