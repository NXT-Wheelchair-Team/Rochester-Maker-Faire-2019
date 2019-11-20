"""
Contains the MovementStateObserver interface.

@author Adam Del Rosso  avd5772@rit.edu
@date 11/20/2019
"""
from abc import ABC, abstractmethod


class MovementStateObserver(ABC):
    """
    Observer in the observer pattern for movement state.
    """

    @abstractmethod
    def update_state(self, state) -> None:
        pass
