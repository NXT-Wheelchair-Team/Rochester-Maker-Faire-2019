"""
Contains the AccelerometerStreamSubject abstract class.
"""

from abc import ABC
from typing import Set
from datetime import time

from model.AccelerometerStreamObserver import AccelerometerStreamObserver


class AccelerometerStreamSubject(ABC):
    """
    Subject in the stream view observer pattern for accelerometer data.
    Contains functionality to keep track of observers and update() them.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.observers: Set[AccelerometerStreamObserver] = []

    def attach(self, observer: AccelerometerStreamObserver) -> None:
        self.observers.add(observer)

    def detach(self, observer: AccelerometerStreamObserver) -> None:
        self.observers.remove(observer)

    def notify(self, x: float, y: float, z: float, timestamp: time) -> None:
        for observer in self.observers:
            observer.update(x, y, z, timestamp)
