import math

def choosey(chooa, choob):
  ccccc = chooa - choob
  if choob < chooa / 2:
    choob = ccccc
  retval = 1.0
  i = int(choob) + 1
  while i <= int(chooa):
    retval = (retval * float(i)) / (chooa - (float(i) - 1.0))
    i = i + 1
  return retval

def algama(s):
  ag = 0.0
  Z = 0.0
  F = 0.0
  x = s

  if x < 0:
    return ag

  if x < 7:
    F = 1.0
    Z = x - 1
    while Z < 7:
      Z = Z + 1
      if Z < 7:
        x = Z
        F = F * Z
    x = x + 1
    F = -math.log(F)

  Z = 1 / pow(x, 2.0)

  ag = F + (x - 0.5) * math.log(x) - x + 0.918938533204673 + (((-1.0 / 1680.0 * Z + 1.0 / 1260.0) * Z - 1.0 / 360.0) * Z + 1.0 / 12.0) / x
  return ag

def pvalfromchisq(x, df):
  j = 0.0
  k = 0.0
  l = 0.0
  m = 0.0
  pi = math.pi
  absx = x
  if x < 0:
    absx = -x

  if x < 0.00000001:
    return 1.0
  if df < 1.0:
    return 1.0

  rr = 1.0
  ii = int(df)

  while ii >= 2:
    rr = double(ii)
    ii = ii - 2

  k = math.exp(math.floor((df + 1.0) * 0.5) * math.log(absx) - x * 0.5) / rr

  if k < 0.00001:
    return 0.0

  if math.floor(df * 0.5) == df * 0.5:
    j = 1.0
  else:
    j = math.sqrt(2.0 / x / pi)

  l = 1.0
  m = 1.0

  if math.isnan(x) != True and math.isinf != True:
    while m >= 0.00000001:
      df = df + 2.0
      m = m * x / df
      l = l + m

  return 1 - j * k * l

def pfromz(_z):
  PFZ = math.nan
  UTZERO = 12
  CON = 1.28

  _x = _z
  if _z < 0:
    _x = -_z
  if _x > UTZERO:
    if _z < 0:
      PFZ = 1.0
    else:
      PFZ = 0.0
    return PFZ

  _y = pow(_z, 2.0) / 2.0
  if _x > CON:
    PFZ = _x - 0.151679116635 + 5.29330324926 / (_x + 4.8385912808 - 15.1508972451 / (_x + 0.742380924027 + 30.789933034 / (_x + 3.99019417011)))
    PFZ = _x + 0.000398064794 + 1.986158381364 / PFZ
    PFZ = _x - 0.000000038052 + 1.00000615302 / PFZ
    PFZ = 0.398942280385 * math.exp(-_y) / PFZ
  else:
    PFZ = _y / (_y + 5.75885480458 - 29.8213557808 / (_y + 2.624331121679 + 48.6959930692 / (_y + 5.92885724438)))
    PFZ = 0.398942280444 - 0.399903438504 * PFZ
    PFZ = 0.5 - _x * PFZ
  if _z < 0:
    PFZ = 1 - PFZ

  return PFZ

def pfromt(_t, _df):
  PFT = math.nan
  g1 = 0.3183098862
  MaxInt = 1000
  ddf = 0
  F = 0
  i = 0
  _a = math.nan
  _b = math.nan
  _c = math.nan
  _s = math.nan
  _p = math.nan

  if _t < 0:
    _t = -_t

  if _df < MaxInt:
    ddf = _df
    _a = _t / math.sqrt(ddf)
    _b = ddf / (ddf + pow(_t, 2.0))
    i = ddf % 2
    _s = 1
    _c = 1
    F = 2 + i
    while F <= ddf - 2:
      _c = _c * _b * (F - 1) / F
      _s = _s + _c
      F = F + 2
    if i <= 0:
      _p = 0.5 - _a * math.sqrt(_b) * _s / 2
    else:
      _p = 0.5 - (_a * _b * _s + math.atan(_a)) * g1
    if _p < 0:
      _p = 0
    if _p > 1:
      _p = 1
    PFT = _p
  else:
    PFT = pfromz(_t)

  return PFT

def pfromf(F, df1, df2):
  PFF = 0.0
  ACU = 0.000000001
  xx = 0.0
  pp = 0.0
  qq = 0.0
  index = True

  if F == 0.0:
    return 0.0
  if F < 0.0 or df1 < 1.0 or df2 < 1.0:
    return 0.0
  if df1 == 1:
    PFF = pfromt(math.sqrt(F), int(df2)) * 2
    return PFF
    
  x = df1 * F / (df2 + df1 * F);
  P = df1 / 2;
  q = df2 / 2;
  psq = P + q;
  cx = 1 - x;

  if P >= x * psq:
    xx = x
    pp = P
    qq = q
    index = False
  else:
    xx = cx
    cx = x
    pp = q
    qq = P
    index = True
    
  term = 1.0;
  ai = 1.0;
  b = 1.0;
  ns = pp + cx * psq;
  rx = xx / cx;
  term1 = 1.0;
  temp = 0.0;

  temp = qq - ai
  if ns == 0.0:
    rx = xx

  while True:
    term = term / (pp + ai) * temp * rx
    if abs(term) <= term1:
      b = b + term
      temp = abs(term)
      term1 = temp
      if temp > ACU or temp > ACU * b:
        ai = ai + 1.0
        ns = ns - 1.0
        if ns >= 0.0:
          temp = qq - ai
          if ns == 0.0:
            rx = xx
          continue
        temp = psq
        psq = psq + 1.0
        continue
    break

  beta = algama(P) + algama(q) - algama(P + q)
  temp = (pp * math.log(xx) + (qq - 1.0) * math.log(cx) - beta) - math.log(pp)

  if temp > -70:
    b = b * math.exp(temp)
  else:
    b = 0.0

  if index == True:
    b = 1 - b

  PFF = 1 - b
  return PFF
