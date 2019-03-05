from ... import Point

class MotionGravityDecorator(object):
	
	def __init__(self, velocity):
		self.velocity = velocity

	def GetVelocity(self):
		velocity = self.velocity.GetVelocity()
		velocity.Y -= 0.4
		return velocity