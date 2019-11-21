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

    def update_position(self, rho: int, phi: float) -> None:
        logging.info("Sending joystick position: {}".format({"Angle": rho, "Magnitude": phi}))
        self.socket.send_json({"Angle": rho, "Magnitude": phi})
