from typing import List

import PyQt5
import sys

import src.model.AccelerometerStreamReader

import src.view_controller.AccelerometerStreamView

import src.test.accelerometer_stream_generator
from src.model.ControlEventSubject import ControlEventSubject
from src.model.MovementState import MovementState
from src.view_controller.KeyboardMovementController import KeyboardMovementController
from src.view_controller.MovementStateView import MovementStateView

reader = src.model.AccelerometerStreamReader.AccelerometerStreamReader(
    "127.0.0.1", 13500
)
src.test.accelerometer_stream_generator.run_generator("127.0.0.1", 13500, 60)

control_events: List[ControlEventSubject] = [KeyboardMovementController()]
movement_state = MovementState(control_events)  # should only be one movement state in system

# Initialize view components

MovementStateView(movement_state)

app = PyQt5.QtWidgets.QApplication(sys.argv)

gui = src.view_controller.AccelerometerStreamView.AccelerometerStreamView(reader)
gui.show()

sys.exit(app.exec_())
