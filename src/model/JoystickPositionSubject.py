"""
Contains the JoystickPositionSubject class.

@author Adam Del Rosso  avd5772@rit.edu
@date 11/20/2019
"""
from abc import ABC
from typing import Set

from src.model.JoystickPositionObserver import JoystickPositionObserver


class JoystickPositionSubject(ABC):
    """
    Subject in the observer pattern for the joystick position.
    Contains functionality to keep track of observers and update() them.
    """

    def __init__(self) -> None:
        super().__init__()
        self.observers: Set[JoystickPositionObserver] = set()

    def attach(self, observer: JoystickPositionObserver) -> None:
        self.observers.add(observer)

    def detach(self, observer: JoystickPositionObserver) -> None:
        self.observers.remove(observer)

    def notify_position(self, rho: int, phi: float) -> None:
        for observer in self.observers:
            observer.update_position(rho, phi)
