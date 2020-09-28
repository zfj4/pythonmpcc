import math
import shared_functions

def fishertests(a, b, c, d, oTF):
  X = float(b)
  Y = float(c)

  lowfish = 0.0
  upfish = 0.0
  k = 0
  while k <=b:
    lowfish = lowfish + shared_functions.choosey(X + Y, float(k)) * pow(0.5, X + Y)
    k = k + 1
  k = b
  while k <= b + c:
    upfish = upfish + shared_functions.choosey(X + Y, float(k)) * pow(0.5, X + Y)
    k = k + 1
  lowup = 0.0
  if upfish < lowfish:
    lowup = 1.0
  oTF[0] = min(lowfish, upfish)

  p = oTF[0]
  Xp = shared_functions.choosey(X + Y, X) * pow(0.5, X + Y)
  if lowup == 1.0:
    k = 0
    while k < b:
      tempP = shared_functions.choosey(X + Y, float(k)) * pow(0.5, X + Y)
      if tempP < Xp:
        p = p + tempP
      k = k + 1
  else:
    k = b
    while k < b + c:
      tempP = shared_functions.choosey(X + Y, float(k)) * pow(0.5, X + Y)
      if tempP < Xp:
        p = p + tempP
      k = k + 1
  oTF[1] = p
