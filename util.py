# Tuple utilities for 2 int tuples

def tadd(a, b):
  return (a[0] + b[0], a[1] + b[1])

def tsub(a, b):
  return (a[0] - b[0], a[1] - b[1])

def tmul(a, b):
  return (a[0] * b, a[1] * b)

def tdiv(a, b):
  return (a[0] / b, a[1] / b)
