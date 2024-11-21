class Device:
	def __init__(self, state):
		self.state = state

class Lamp(Device):
	def __init__(self, state):
		self.state = state
		self.type = "Lamp"

class Termometer(Device):
	def __init__(self, state):
		self.state = state
		self.type = "Termometer"