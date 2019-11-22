"""
Contains the HeadTiltJoystickController class.

@author Adam Del Rosso
@date 11/20/2019
"""
import logging
import math

from src.model.HeadTiltObserver import HeadTiltObserver
from src.model.HeadTiltSubject import HeadTiltSubject
from src.model.JoystickPositionSubject import JoystickPositionSubject

import numpy as np

from src.model.MovementState import MovementState


class HeadTiltJoystickController(JoystickPositionSubject, HeadTiltObserver):
    """
    Concrete subject in the joystick position observer pattern.
    Concrete observer in the head tilt data observer pattern.
    Responsible for translating the head tilt data into polar coordinates and notify()ing its observers.
    """

    def __init__(self, head_tilt_subject: HeadTiltSubject, movement_state: MovementState) -> None:
        super().__init__()
        self.head_tilt_subject = head_tilt_subject
        self.head_tilt_subject.attach(self)
        self.movement_state = movement_state

    def update_head_tilt(self, pitch: float, roll: float) -> None:
        if self.movement_state.state == MovementState.State.GO:
            magnitude, angle = self.cart2pol(roll, pitch)
            if magnitude > 1.0:  # max rho is 100%
                magnitude = 1.0
            angle = math.degrees(angle)
            if angle < 0:  # translate negative degrees in quadrants 3 & 4 into positive
                angle = 360 + angle
            angle = int(angle)
            logging.debug(
                "HeadTiltJoystickController: Got pitch: {}, roll: {}. Magnitude: {}, Angle: {}".format(pitch, roll, magnitude, angle))
            self.notify_position(magnitude, angle)
        else:
            logging.debug("Stop state active, not controlling joystick.")

    @staticmethod
    def cart2pol(x, y):
        rho = np.sqrt(x ** 2 + y ** 2)
        phi = np.arctan2(y, x)
        return rho, phi
