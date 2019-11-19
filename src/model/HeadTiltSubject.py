"""
Contains the HeadTiltSubject abstract class.

@author Adam Del Rosso  avd5772@rit.edu
@date 11/19/2019
"""

from abc import ABC
from typing import Set

from src.model.HeadTiltObserver import HeadTiltObserver


class AccelerometerStreamSubject(ABC):
    """
    Subject in the observer pattern for head tilt data.
    Contains functionality to keep track of observers and update() them.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.observers: Set[HeadTiltObserver] = set()

    def attach(self, observer: HeadTiltObserver) -> None:
        self.observers.add(observer)

    def detach(self, observer: HeadTiltObserver) -> None:
        self.observers.remove(observer)

    def notify(self, pitch: float, roll: float) -> None:
        for observer in self.observers:
            observer.update_head_tilt(pitch, roll)
