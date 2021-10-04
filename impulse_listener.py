from __future__ import annotations

from random import choice
from time import sleep


class ImpulseListener:
    """
    Class to listen for and return serial output from impulse electrodes.
    """

    def __init__(self, port: int, tentacle_num: int) -> None:
        self.port = port
        self.loop = False
        self.tentacle_num = tentacle_num

    def __repr__(self) -> str:
        return f"ImpulseListener(port: {self.port}, tentacle_num: {self.tentacle_num})"

    def start_listening(self) -> int | None:
        """
        Listen for serial output on the serial port given when initializing the class.
        -> tentacle_num: (x, y, z) [0-1023]
        """

        self.loop = True
        while self.loop:
            print(
                f"{self.tentacle_num}: ({choice(range(0, 1024))}, {choice(range(0, 1024))}, {choice(range(0, 1024))})"
            )
            sleep(1 / 60)

        return None

    def stop_listening(self) -> None:
        """
        Stop listening for serial output.
        """

        self.loop = False