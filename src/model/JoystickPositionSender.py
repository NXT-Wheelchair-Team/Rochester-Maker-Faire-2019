"""
Contains the JoystickPositionSender class.

@author Adam Del Rosso
@date 11/20/2019
"""
import logging

import zmq

from src.model.JoystickPositionObserver import JoystickPositionObserver
from src.model.JoystickPositionSubject import JoystickPositionSubject


class JoystickPositionSender(JoystickPositionObserver):
    """
    Concrete observer in the joystick position observer pattern.
    Responsible for sending joystick position requests to the joystick manipulator control software.
    """

    def __init__(self, joystick_position_subject: JoystickPositionSubject, ip: str, port: int, zmq_context: zmq.Context) -> None:
        super().__init__()
        self.joystick_position_subject = joystick_position_subject
        self.joystick_position_subject.attach(self)
        self.socket = zmq_context.socket(zmq.PAIR)
        self.socket.bind("tcp://{}:{}".format(ip, port))  # this class is the server

    def update_position(self, magnitude: float, angle: int) -> None:
        msg = {"Angle": angle, "Magnitude": magnitude}
        self.socket.send_json(msg)
        logging.info("Sent joystick position: {}".format(msg))
