"""
Contains the KeyboardMovementController class.

@author Adam Del Rosso  avd5772@rit.edu
@date 11/20/2019
"""
import logging

from pynput import keyboard

from src.model.ControlEventSubject import ControlEventSubject


class KeyboardMovementController(ControlEventSubject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # start thread to throw events on keyboard presses
        self.listener = keyboard.Listener(on_release=self.on_release, dameon=True)
        self.listener.start()
        # ideally these keybindings should be provided by some non-code config - this will do for now
        self.keybindings = {
            keyboard.Key.ctrl_r: self.notify_go_event,
            keyboard.Key.space: self.notify_stop_event
        }
        print("Keyboard listener started... keybindings:")
        print("\t<space>: STOP")
        print("\t<r_ctrl>: GO")

    def on_release(self, key):
        if key in self.keybindings:
            logging.info("Keyboard key: {} was pressed".format(key))
            self.keybindings[key]()  # call either notify_stop or notify_go based on keybindings


if __name__ == "__main__":
    # test logger by join()ing the listener thread - runs until force stopped
    logging.basicConfig(level=logging.INFO)
    KeyboardMovementController().listener.join()
