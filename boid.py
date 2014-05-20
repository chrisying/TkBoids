# Boid object class

class Boid:
  def __init__(self, pos, vel, id):
    self.pos = pos    # tuple (x,y)
    self.vel = vel    # tuple (x vel,y vel)
    self.id = id

  def addVel(self, v):
    self.vel = (self.vel[0] + v[0], self.vel[1] + v[1])

  def doMove(self):
    self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
