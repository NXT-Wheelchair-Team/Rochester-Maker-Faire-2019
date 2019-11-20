"""
Contains the ControlEventObserver interface.
Interfaces (abstract classes with no implemented functions) are not necessary in Python
but this is here for code documentation purposes along with optimal type hinting.

@author Adam Del Rosso  avd5772@rit.edu
@date 11/19/2019
"""
from abc import ABC, abstractmethod


class ControlEventObserver(ABC):
    """
    Observer in the observer pattern for control events.
    """

    @abstractmethod
    def notify_go_event(self) -> None:
        """
        A GO event has occurred, signalling that head tilt control should be engaged.
        """
        pass

    @abstractmethod
    def notify_stop_event(self) -> None:
        """
        A STOP event has occurred, signalling that head tilt control should be disengaged.
        """
        pass
