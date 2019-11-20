"""
Contains the MovementState class.

@author Adam Del Rosso  avd5772@rit.edu
@date 11/20/2019
"""
from typing import List

from src.model.ControlEventObserver import ControlEventObserver
from src.model.ControlEventSubject import ControlEventSubject
from src.model.MovementStateSubject import MovementStateSubject


class MovementState(ControlEventObserver, MovementStateSubject):
    """
    Holds the state of movement for the wheelchair, GO or STOP
    """

    def __init__(self, control_events: List[ControlEventSubject]) -> None:
        super().__init__()
        self.state: MovementStateSubject.State = self.State.STOP  # initialize in the STOP state
        self.control_events = control_events
        for control_event in control_events:
            control_event.attach(self)  # register us as a listener to the control events

    def notify_go_event(self) -> None:
        self.state = self.State.GO
        self.notify(self.state)  # notify observers of the state change

    def notify_stop_event(self) -> None:
        self.state = self.State.STOP
        self.notify(self.state)  # notify observers of the state change

