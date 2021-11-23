import itertools
import time
from multiprocessing import Process
import floors
import pyinputplus as pyip
from playsound import playsound
import sys


class Lift:
    _ground_floor = 0

    def __init__(self):
        self.door_command = itertools.cycle(("open", "clos"))
        self.current_floor = Lift._ground_floor
        self.floors = floors.Floor()

    def get_user_floor(self):
        """Returns the user floor level as int and
         validates the input to be in the floors range"""

        response = pyip.inputInt(
            prompt='Enter floor level: ',
            min=self.floors.FLOORS[0],
            max=self.floors.FLOORS[-1],
            blank=False
        )
        return response

    def call_lift(self, floor):
        """Runs the lift from the ground floor upwards"""

        process = Process(target=playsound, args=("templates/elevator-music.mp3", False))

        self.run_lift(floor)
        self.door()
        process.start()
        user_floor = self.get_user_floor()
        self.run_lift(user_floor)
        self.door()
        process.terminate()

    def go_up(self, floor):
        """Iterates trough the floors and sets the self.current_floor to floor"""

        for f in range(self.current_floor, floor + 1):
            print(f"Floor {f}")
            time.sleep(1)

        self.current_floor = floor

    def go_down(self, floor):
        """Iterates trough the floors and sets the self.current_floor to floor"""

        for f in range(self.current_floor, floor + 1, -1):
            print(f"Floor {f}")
            time.sleep(1)

        self.current_floor = floor

    def door(self):
        """Opens and closing the doors"""

        commands = {"open": ">", "clos": "<"}
        current_command = next(self.door_command)
        print(f"The door is {current_command}ing.")
        for _ in range(20):
            print(f"{commands[current_command]}", end="")
            time.sleep(0.3)
        print()

    def run_lift(self, floor):
        """Calls the elevator and sets the current floor"""

        if self.current_floor < floor:
            self.go_up(floor)
        elif self.current_floor > floor:
            self.go_down(floor)
        else:
            print("You are on the same floor")

    def __str__(self):
        print(f"This is the lift with current floor: {self.current_floor}")
