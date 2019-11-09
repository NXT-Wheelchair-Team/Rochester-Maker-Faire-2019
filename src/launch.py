import model.AccelerometerStreamReader

reader = model.AccelerometerStreamReader.AccelerometerStreamReader("127.0.0.1", 13500)
reader.thread.join()

