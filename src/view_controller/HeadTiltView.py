"""
Contains the HeadTiltView Qt widget.

@author Adam Del Rosso
@date 11/19/2019
"""
from PyQt5.QtWidgets import QWidget

from src.model.HeadTiltObserver import HeadTiltObserver
from src.model.HeadTiltSubject import HeadTiltSubject


class HeadTiltView(HeadTiltObserver):
    """
    View for displaying head tilt data.
    """

    def __init__(self, head_tilt_subject: HeadTiltSubject):
        super().__init__()
        self.subject = head_tilt_subject
        self.subject.attach(self)

    def update_head_tilt(self, pitch: float, roll: float) -> None:
        """
        Called by subject.
        """
        # TODO create an actual GUI widget
        print("Head tilt view new data:")
        print("\tPitch: {}%".format(pitch * 100))
        print("\tRoll: {}%".format(roll * 100))
