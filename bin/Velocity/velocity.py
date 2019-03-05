

class Velocity(object):

	def __init__(self, point):
		self.point = point

	def isStanding(self):
		return self.point.X == 0

	def isGoingLeft(self):
		return self.point.X < 0

	def isGoingUp(self):
		return self.point.Y > 0