"""
Contains the ControlEventSubject abstract class.

@author Adam Del Rosso  avd5772@rit.edu
@date 11/19/2019
"""
from abc import ABC
from typing import Set

from src.model.ControlEventObserver import ControlEventObserver


class ControlEventSubject(ABC):
    """
    Subject in the observer pattern for control events.
    Contains functionality to keep track of observers and update() them.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.observers: Set[ControlEventObserver] = set()

    def attach(self, observer: ControlEventObserver) -> None:
        self.observers.add(observer)

    def detach(self, observer: ControlEventObserver) -> None:
        self.observers.remove(observer)

    def notify_go_event(self) -> None:
        for observer in self.observers:
            observer.notify_go_event()

    def notify_stop_event(self) -> None:
        for observer in self.observers:
            observer.notify_stop_event()