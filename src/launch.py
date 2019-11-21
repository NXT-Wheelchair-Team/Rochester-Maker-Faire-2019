from typing import List

import PyQt5
import sys

import zmq

import src.model.AccelerometerStreamReader

import src.view_controller.AccelerometerStreamView

import src.test.accelerometer_stream_generator
from src.model import HeadTiltReceiver
from src.model.ControlEventSubject import ControlEventSubject
from src.model.HeadTiltJoystickController import HeadTiltJoystickController
from src.model.HeadTiltReceiver import HeadTiltReceiver
from src.model.JoystickPositionSender import JoystickPositionSender
from src.model.MovementState import MovementState
from src.view_controller.HeadTiltView import HeadTiltView
from src.view_controller.KeyboardMovementController import KeyboardMovementController
from src.view_controller.MovementStateView import MovementStateView

MANIPULATOR_CTRL_PORT = 9784
HEAD_TILT_PORT = 5557

reader = src.model.AccelerometerStreamReader.AccelerometerStreamReader(
    "127.0.0.1", 13500
)
src.test.accelerometer_stream_generator.run_generator("127.0.0.1", 13500, 60)

control_events: List[ControlEventSubject] = [KeyboardMovementController()]
movement_state = MovementState(control_events)  # should only be one movement state in system

zmq_context = zmq.Context()
head_tilt_receiver = HeadTiltReceiver("127.0.0.1", HEAD_TILT_PORT, zmq_context)
joystick_pos_controller = HeadTiltJoystickController(head_tilt_receiver)
joystick_pos_sender = JoystickPositionSender(joystick_pos_controller, "127.0.0.1", MANIPULATOR_CTRL_PORT, zmq_context)

# Initialize view components

MovementStateView(movement_state)
HeadTiltView(head_tilt_receiver)

app = PyQt5.QtWidgets.QApplication(sys.argv)

gui = src.view_controller.AccelerometerStreamView.AccelerometerStreamView(reader)
gui.show()

sys.exit(app.exec_())
