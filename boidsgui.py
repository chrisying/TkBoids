# Boids GUI

import math

from tkinter import *
from tkinter import ttk

class BoidsApp:
  def __init__ (self, master, size):
    self.parent = master
    self.ATTRACT = 0.01

    self.frame = ttk.Frame(master, padding="5 5 5 15")
    self.frame.pack()
        
    self.map = Canvas(self.frame, width=size, height=size, bg="#ccc")
    self.map.pack()
        
    self.buttons = ttk.Frame(self.frame, padding="0 10 0 0")
    self.buttons.pack()
        
    self.start = ttk.Button(self.buttons, text="Start", command=self.start)
    self.start.pack(side=LEFT)
    self.invert = ttk.Button(self.buttons, text="Invert", command= self.invert)
    self.invert.pack(side=LEFT)
    self.stop = ttk.Button(self.buttons, text="Stop", command=self.stop)
    self.stop.pack(side=RIGHT)

    self.running = True
                
  def start(self):
    self.running = True

  def stop(self):
    self.running = False

  def invert(self):
    self.ATTRACT = -1.0 * self.ATTRACT
  
  def drawObject(self, pos, vel):
    dir = math.atan2(vel[1], vel[0])
    mag = math.hypot(vel[0], vel[1])
    if mag < 0.1:
      mag = 0.1
    norm = (vel[0] / mag, vel[1] / mag)
    coords = [(pos[0] + norm[0] * (mag/2 + 3), pos[1] + norm[1] * (mag/2 + 3)),
              (pos[0] - norm[0] + math.cos(dir + math.pi / 2) * 3,
               pos[1] - norm[1] + math.sin(dir + math.pi / 2) * 3),
              (pos[0] - norm[0] - math.cos(dir + math.pi / 2) * 3,
               pos[1] - norm[1] - math.sin(dir + math.pi / 2) * 3)]
    return self.map.create_polygon(coords, fill="", activefill="red", outline="black") 

  # blist: list of (pos, vel), pos/vel = (x, y)
  def render(self, blist):
    self.map.delete("all")
    for b in blist:
      self.drawObject(b[0], b[1])
