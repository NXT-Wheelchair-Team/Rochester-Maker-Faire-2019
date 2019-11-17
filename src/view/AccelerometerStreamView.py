"""
Contains the AccelerometerStreamView Qt widget.
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from collections import deque
from datetime import time
from typing import Dict, Deque, Union
import threading

from src.model.AccelerometerStreamObserver import AccelerometerStreamObserver
from src.model.AccelerometerStreamSubject import AccelerometerStreamSubject


class AccelerometerStreamView(QWidget):
    """
    View for displaying accelerometer data.
    """

    lock = threading.Lock()

    def __init__(self, accel_stream: AccelerometerStreamSubject, parent=None):
        super().__init__(parent=parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.data: Dict[str, Deque[Union[float, str]]] = {
            "x": deque(maxlen=100),
            "y": deque(maxlen=100),
            "z": deque(maxlen=100),
            "time": deque(maxlen=100),
        }

        self.accel_stream = accel_stream
        self.accel_stream.attach(self)

        threading.Thread(daemon=True, target=self.draw_graph).start()

    def update(self, x: float, y: float, z: float, timestamp: time) -> None:
        """
        This is the stream reader thread!! Don't do any long operations or it will drop packets.
        """
        plot_timestamp = "{}:{}".format(timestamp.second, timestamp.microsecond)

        # these dequeue operations should already be thread safe - the lock is to ensure
        # the x, y, z, and time values are updated at the same time before another draw occurs
        with self.lock:
            self.data["x"].append(x)
            self.data["y"].append(y)
            self.data["z"].append(z)
            self.data["time"].append(plot_timestamp)
        # self.draw_graph()  - DON'T DO THIS HERE

    def draw_graph(self):
        """
        TODO this is really slow. Performs at <10 FPS. Look into matplotlib animation using "blit"
        (only re-draws the parts of the figure that have been updated) OR use an entirely different
        plotting library.
        """
        self.figure.clear()
        subplot = self.figure.add_subplot(111)
        with self.lock:
            subplot.plot("time", "x", data=self.data)
            subplot.plot("time", "y", data=self.data)
            subplot.plot("time", "z", data=self.data)
        subplot.axes.get_xaxis().set_visible(False)
        self.canvas.draw()
        self.draw_graph()  # constantly re-draw the graph to achieve a live display
