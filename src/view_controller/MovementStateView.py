"""
Contains the MovementStateView Qt widget.

@author Adam Del Rosso  avd5772@rit.edu
@date 11/20/2019
"""
from src.model.MovementStateObserver import MovementStateObserver
from src.model.MovementStateSubject import MovementStateSubject


class MovementStateView(MovementStateObserver):

    def __init__(self, movement_state_subject: MovementStateSubject) -> None:
        self.movement_state_subject = movement_state_subject
        self.movement_state_subject.attach(self)

    def update_state(self, state: MovementStateSubject.State) -> None:
        # TODO create an actual GUI widget
        print("Movement state view: {}".format(state.name))
