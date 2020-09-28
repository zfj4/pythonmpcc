def uncorrected(plusminus, minusplus):
  x = float(plusminus)
  y = float(minusplus)
  if x == 0:
    x = x + 0.5
    y = y + 0.5
  if y == 0:
    x = x + 0.5
    y = y + 0.5
  retval = pow(x - y, 2.0) / (x + y)
  return retval

def corrected(plusminus, minusplus):
  x = float(plusminus)
  y = float(minusplus)
  if x == 0:
    x = x + 0.5
    y = y + 0.5
  if y == 0:
    x = x + 0.5
    y = y + 0.5
  retval = pow(abs(x - y) - 1.0, 2.0) / (x + y)
  return retval
