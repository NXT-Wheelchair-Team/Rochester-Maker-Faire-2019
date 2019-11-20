"""
Contains the MovementStateSubject abstract class.

@author Adam Del Rosso  avd5772@rit.edu
@date 11/20/2019
"""
from abc import ABC
from enum import Enum, auto
from threading import Lock
from typing import Set

from src.model.MovementStateObserver import MovementStateObserver


class MovementStateSubject(ABC):
    """
    Subject in the observer pattern for movement state.
    Contains functionality to keep track of observers and update() them.
    """

    class State(Enum):
        GO = auto()  # the wheelchair is allowed to move
        STOP = auto()  # the wheelchair should not move

    def __init__(self) -> None:
        super().__init__()
        self.observers: Set[MovementStateObserver] = set()
        self.lock = Lock()

    def attach(self, observer: MovementStateObserver) -> None:
        self.observers.add(observer)

    def detach(self, observer: MovementStateObserver) -> None:
        self.observers.remove(observer)

    def notify(self, state: State) -> None:
        with self.lock:  # one thread can update at a time - observers needn't worry about thread safety
            for observer in self.observers:
                observer.update_state(state)


