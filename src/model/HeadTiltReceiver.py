"""
Contains the HeadTiltReceiver class.
"""
import logging
from typing import Dict
import zmq
import threading

from src.model.HeadTiltSubject import HeadTiltSubject


class HeadTiltReceiver(HeadTiltSubject):
    """
    Concrete subject in the observer pattern for head tilt data.
    Contains functionality to receive ZMQ messages from the head tilt detection subsystem.
    """

    def __init__(self, ip: str, port: int, zmq_context: zmq.Context, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ip = ip
        self.port = port
        self.socket = zmq_context.socket(zmq.PAIR)
        self.socket.bind("tcp://{}:{}".format(ip, port))  # this class is the server
        self.thread = threading.Thread(target=self._threading_main_loop,
                                       daemon=True  # thread dies with main process
                                       )

    def _threading_main_loop(self):
        logging.info("Head tilt reader thread started")
        try:
            while True:
                msg: Dict = self.socket.recv_json()
                pitch = float(msg["tilt"])
                roll = float(msg["tilt"])
                pitch, roll = self._check_bounds(pitch, roll)
                self.notify(pitch, roll)
        except Exception as e:
            logging.error(
                "Head tilt reader thread raised an exception: {}".format(e)
            )
            raise e

    @staticmethod
    def _check_bounds(pitch: float, roll: float) -> (float, float):
        """
        Ensure pitch and roll values are between -1.0 and 1.0 (-100% and 100%)
        :param pitch: head tilt in the front-back direction
        :param roll: head tilt in the side-to-side direction
        :return: tuple(pitch, roll) with checked bounds
        """
        if pitch > 1.0:
            logging.warning("Pitch value received was greater than 1.0")
            pitch = 1.0
        elif pitch < -1.0:
            logging.warning("Pitch value received less than -1.0")
            pitch = 1.0
        if roll > 1.0:
            logging.warning("Roll value received was greater than 1.0")
            roll = 1.0
        elif roll < -1.0:
            logging.warning("Roll value received was less than -1.0")
            roll = 1.0
        return pitch, roll
