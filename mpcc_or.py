import math
import shared_functions

def oddsratio(plusminus, minusplus):
  x = float(plusminus)
  y = float(minusplus)
  if x == 0:
    x = x + 0.5
    y = y + 0.5
  if y == 0:
    x = x + 0.5
    y = y + 0.5
  retval = x / y
  return retval

def lcl(plusminus, minusplus):
  x = float(plusminus)
  y = float(minusplus)
  if x == 0:
    x = x + 0.5
    y = y + 0.5
  if y == 0:
    x = x + 0.5
    y = y + 0.5
  retval = math.exp(math.log(oddsratio(plusminus, minusplus)) - 1.96 * pow(1 / x + 1 / y, 0.5))
  return retval

def ucl(plusminus, minusplus):
  x = float(plusminus)
  y = float(minusplus)
  if x == 0:
    x = x + 0.5
    y = y + 0.5
  if y == 0:
    x = x + 0.5
    y = y + 0.5
  retval = math.exp(math.log(oddsratio(plusminus, minusplus)) + 1.96 * pow(1 / x + 1 / y, 0.5))
  return retval

def fisherlimits(a, b, c, d, l):
  X = float(b)
  Y = float(c)
  if X == 0.0 or Y == 0.0:
    X = X + 0.5
    Y = Y + 0.5
  F = 0.0
  p = 1.0
  while p > 0.975:
    F = F + 1
    p = shared_functions.pfromf(F, 2.0 * X, 2.0 * (Y + 1))
  aa = F - 1.0
  bb = F
  precision = 0.0000001
  while bb - aa > precision:
    F = (bb + aa) / 2.0
    if shared_functions.pfromf(F, 2.0 * X, 2.0 * (Y + 1)) > 0.975:
      aa = F
    else:
      bb = F
  l[0] = X * F / (Y + 1.0)
  while p > 0.025:
    F = F + 1
    p = shared_functions.pfromf(F, 2.0 * (X + 1), 2.0 * Y)
  aa = F - 1.0
  bb = F + 0.5
  while bb - aa > precision:
    F = (bb + aa) / 2.0
    if shared_functions.pfromf(F, 2.0 * (X + 1), 2.0 * Y) > 0.025:
      aa = F
    else:
      bb = F
  l[1] = (X + 1.0) * F / Y
