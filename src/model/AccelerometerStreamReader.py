"""
Contains the AccelerometerStreamReader class.
"""

import socket
import threading
import logging
import datetime
import json

from src.model.AccelerometerStreamSubject import AccelerometerStreamSubject


class AccelerometerStreamReader(AccelerometerStreamSubject):
    """
    Concrete subject in the stream view observer pattern for accelerometer data.

    Launches a thread to continually read from the accelerometer data stream.
    """

    def __init__(self, ip: str, port: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip, self.port))

        self.thread = threading.Thread(
            daemon=True, target=self._thread_main_loop  # thread stops with main process
        )
        self.thread.start()

    def _thread_main_loop(self):
        logging.info("Accelerometer stream reader thread started")
        try:
            while True:
                accel_data, addr = self.socket.recvfrom(1024)
                timestamp = datetime.datetime.now().time()

                accel_dict = json.loads(accel_data)
                x = accel_dict["data"][0]
                y = accel_dict["data"][1]
                z = accel_dict["data"][2]

                self.notify(x, y, z, timestamp)
        except Exception as e:
            logging.error(
                "Accelerometer stream reader thread raised an excpetion: {}".format(e)
            )
            raise e
