"""
Contains the AccelerometerStreamView Qt widget.
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from collections import deque
from datetime import time

from model.AccelerometerStreamObserver import AccelerometerStreamObserver


class AccelerometerStreamView(QWidget, AccelerometerStreamObserver):
    """
    View for displaying accelerometer data.
    """

    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

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

        self.data_queue = deque(maxlen=100)

    def update(self, x: float, y: float, z: float, timestamp: time) -> None:
        self.data_queue.append(tuple(tuple(x, y, z), time))
        self.draw_graph()

    def draw_graph(self):
        pass
