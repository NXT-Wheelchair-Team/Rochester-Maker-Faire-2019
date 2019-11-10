import PyQt5
import sys

import src.model.AccelerometerStreamReader

import src.view.AccelerometerStreamView

import src.test.accelerometer_stream_generator

reader = src.model.AccelerometerStreamReader.AccelerometerStreamReader(
    "127.0.0.1", 13500
)
src.test.accelerometer_stream_generator.run_generator("127.0.0.1", 13500, 60)

app = PyQt5.QtWidgets.QApplication(sys.argv)

gui = src.view.AccelerometerStreamView.AccelerometerStreamView(reader)
gui.show()

sys.exit(app.exec_())
