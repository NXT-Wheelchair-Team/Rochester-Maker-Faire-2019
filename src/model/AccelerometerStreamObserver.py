"""
Contains the AccelerometerStreamObserver interface.
Interfaces (abstract classes with no implemented functions) are not necessary in Python 
but this is here for code documentation purposes along with optimal type hinting.
"""

from abc import ABC, abstractmethod
from datetime import time


class AccelerometerStreamObserver(ABC):
    """
    Observer in the stream view observer pattern for accelerometer data.
    """

    @abstractmethod
    def update(self, x: float, y: float, z: float, timestamp: time) -> None:
        """
        Update the observer with the new accelerometer XYZ values and a timestamp 
        representing the time the accelerometer data was received.
        """
        pass
