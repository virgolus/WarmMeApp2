class Zone:
    id = 0
    name = ''
    sensors = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def addSensors(self, sensor):
        self.sensors.append(sensor)

