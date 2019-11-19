"""
Contains the HeadTiltObserver interface.
Interfaces (abstract classes with no implemented functions) are not necessary in Python 
but this is here for code documentation purposes along with optimal type hinting.

@author Adam Del Rosso
@date 11/19/2019
"""

from abc import ABC, abstractmethod


class HeadTiltObserver(ABC):
    """
    Observer in the observer pattern for head tilt data.
    """

    @abstractmethod
    def update_head_tilt(self, pitch: float, roll: float) -> None:
        """
        Update the observer with the new head tilt and roll values.
        """
        pass
