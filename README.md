# Drone Physics Simulator

This project is going to be used for simulating the drone physics. It consists of three parts:
1. `visualization`: built with Vue and Three.js, responsible for display 3D graphics, and collecting user inputs.
1. `server`: communicates with visualization part using websocket. It will create a physical simulating environment (with physical laws, sensor data simulation and user input signal simulation implemented).
1. `drone_flight_controller`: the real brain of the drone. Linked to this project using git submodule.

