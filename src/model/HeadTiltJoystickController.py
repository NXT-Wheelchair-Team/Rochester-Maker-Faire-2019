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


class HeadTiltJoystickController(JoystickPositionSubject, HeadTiltObserver):
    """
    Concrete subject in the joystick position observer pattern.
    Concrete observer in the head tilt data observer pattern.
    Responsible for translating the head tilt data into polar coordinates and notify()ing its observers.
    """

    def __init__(self, head_tilt_subject: HeadTiltSubject) -> None:
        super().__init__()
        self.head_tilt_subject = head_tilt_subject
        self.head_tilt_subject.attach(self)

    def update_head_tilt(self, pitch: float, roll: float) -> None:
        rho, phi = self.cart2pol(roll, pitch)
        if rho > 1.0:  # max rho is 100%
            rho = 1.0
        phi = math.degrees(phi)
        if phi < 0:  # translate negative degrees in quadrants 3 & 4 into positive
            phi = 360 + phi
        logging.debug(
            "HeadTiltJoystickController: Got pitch: {}, roll: {}. Rho: {}, Phi: {}".format(pitch, roll, rho, phi))
        self.notify_position(rho, phi)

    @staticmethod
    def cart2pol(x, y):
        rho = np.sqrt(x ** 2 + y ** 2)
        phi = np.arctan2(y, x)
        return rho, phi
