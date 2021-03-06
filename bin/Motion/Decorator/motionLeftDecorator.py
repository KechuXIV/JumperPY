from ... import Point

class MotionLeftDecorator(object):
	
	def __init__(self, velocity):
		self.velocity = velocity

	def GetVelocity(self):
		velocity = self.velocity.GetVelocity()
		velocity.X -= 4
		return velocity