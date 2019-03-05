from ... import Point

class MotionJumpDecorator(object):
	
	def __init__(self, velocity):
		self.velocity = velocity

	def GetVelocity(self):
		velocity = self.velocity.GetVelocity()
		velocity.Y += 8
		return velocity