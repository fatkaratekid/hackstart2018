from drone_interface import *

if __name__ == "__main__":
    print("CONTROLLING DRONE")
    drone = DroneInterface()
    drone.start()
    drone.lift_off()
    drone.move_forward()
    drone.stop()