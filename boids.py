# Boids main

from random import random
import math

from tkinter import *
from boid import *
from boidsgui import *
from util import *

NUM = 10
TIME = 50
SIZE = 640
MAX = 20
REPEL = 0.1
CONFORM = 0.1
DRIFT = 1

class Boids:
  def __init__(self, num, size):
    self.num = num

    # Constants to test
    self.ATTRACT = 0.1
    self.boids = []
    for i in range(num):
      b = Boid((random() * size, random() * size), (random() - 0.5, random() - 0.5), i)
      self.boids += [b]

  def getBList(self):
    blist = []
    for b in self.boids:
      blist += [(b.pos, b.vel)]
    return blist

  def averages(self):
    sums = ((0.0, 0.0), (0.0, 0.0))
    for b in self.boids:
      sums = (tadd(sums[0], b.pos), tadd(sums[1], b.vel))
    return sums

  # Attraction
  def rule1(self, boid, sumPos):
    sum = tsub(sumPos, boid.pos)
    avg = tdiv(sum, self.num - 1)
    return tmul(tsub(avg, boid.pos), self.ATTRACT)
  
  # Repulsion
  def rule2(self, boid):
    sum = (0.0, 0.0)
    for b in self.boids:
      if b.id != boid.id and math.hypot(boid.pos[0] - b.pos[0], boid.pos[1] - b.pos[1]) < 50:
        sum = tadd(sum, tsub(boid.pos, b.pos))
    return tmul(sum, REPEL)

  # Conformity
  def rule3(self, boid, sumVel):
    sum = tsub(sumVel, boid.vel)
    avg = tdiv(sum, self.num - 1)
    return tmul(tsub(avg, boid.vel), CONFORM)

  # Soft boundary
  def rule4(self, boid):
    sum = (0.0, 0.0)
    mag = math.hypot(boid.vel[0], boid.vel[1])
    if boid.pos[0] < 0:
      sum = tadd(sum, (DRIFT * mag, 0.0))
    if boid.pos[0] > SIZE:
      sum = tsub(sum, (DRIFT * mag, 0.0))
    if boid.pos[1] < 0:
      sum = tadd(sum, (0.0, DRIFT * mag))
    if boid.pos[1] > SIZE:
      sum = tsub(sum, (0.0, DRIFT * mag))
    return sum

  def update(self):
    (sumPos, sumVel) = self.averages()
    for b in self.boids:
      v1 = self.rule1(b, sumPos)
      v2 = self.rule2(b)
      v3 = self.rule3(b, sumVel)
      v4 = self.rule4(b)
      b.addVel(tadd(tadd(tadd(v1, v2), v3), v4))
      if math.hypot(b.vel[0], b.vel[1]) > MAX:
        b.vel = tmul(b.vel, 0.9)
      b.doMove() 

def loop(app, boids):
  if app.running:
    boids.ATTRACT = app.ATTRACT
    boids.update()
    app.render(boids.getBList())
  app.parent.after(TIME, loop, app, boids)

boids = Boids(NUM, SIZE)
root = Tk(className="Boids")
root.resizable(0, 0)
app = BoidsApp(root, SIZE)
loop(app, boids)
root.mainloop()
