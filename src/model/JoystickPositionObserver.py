"""
Contains the JoystickPositionObserver interface.

@author Adam Del Rosso
@date 11/20/2019
"""
from abc import ABC, abstractmethod


class JoystickPositionObserver(ABC):
    """
    Observer in the observer pattern for joystick position.
    """

    @abstractmethod
    def update_position(self, rho: int, phi: float) -> None:
        """
        :param rho: Angular component of the polar coordinate (0-359 - East is 0)
        :param phi: Scalar component of the polar coordinate (0.0-1.0 - 0%-100% of max joystick position)
        """
        pass
