"""
Generates random X, Y, Z accelerometer values at a specified rate.
"""

import threading
import socket
import time
import random
import json


def run_generator(ip: str, port: int, rate_hz: int = 60):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    threading.Thread(
        target=generate, args=(sock, ip, port, rate_hz), daemon=True
    ).start()


def generate(sock: socket.socket, ip: str, port: int, rate_hz: int):
    random.seed(1)
    while True:
        msg = {
            "data": [
                random.uniform(0.7, 1.0),
                random.uniform(0.0, 0.3),
                random.uniform(0.3, 0.7),
            ]
        }
        sock.sendto(json.dumps(msg).encode(), (ip, port))

        time.sleep(1.0 / rate_hz)
