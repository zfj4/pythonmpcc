import sys
import csv
import math
import mpcc_or
import mpcc_chisq
import mpcc_fishertests
import shared_functions
rowcount = 0
oldpairid = "-1"

excontrol=0
excase=0

exex=0
exun=0
unex=0
unun=0

with open(sys.argv[1], newline='') as csvfile:
  sickreader = csv.reader(csvfile, delimiter=',', quotechar='"')
  next(sickreader)
  sortsick=sorted(sickreader, key=lambda x: (int(x[0]), int(x[1])), reverse=False)
  row_count = sum(1 for row in sortsick)
  for row in sortsick:
    pairid = row[0]
    print(' '.join(row))
    rowcount = rowcount + 1
    if pairid != oldpairid:
      if rowcount > 1:
        if excase == 1:
          if excontrol == 1:
            exex = exex + 1
        if excase == 1:
          if excontrol == 0:
            exun = exun + 1
        if excase == 0:
          if excontrol == 1:
            unex = unex + 1
        if excase == 0:
          if excontrol == 0:
            unun = unun + 1
        excontrol=0
        excase=0
    oldpairid = pairid
    if int(row[1]) == 1:
      if int(row[2]) == 1:
        excase = excase + 1
    if int(row[1]) == 0:
      if int(row[2]) == 1:
        excontrol = excontrol + 1
    if rowcount == row_count:
      if excase == 1:
        if excontrol == 1:
          exex = exex + 1
      if excase == 1:
        if excontrol == 0:
          exun = exun + 1
      if excase == 0:
        if excontrol == 1:
          unex = unex + 1
      if excase == 0:
        if excontrol == 0:
          unun = unun + 1

#rint('Both Exposed = ', exex)
#rint('Case Exposed, Control Unexposed = ', exun)
#rint('Case Unexposed, Control Exposed = ', unex)
#rint('Both Unexposed = ', unun)
print('==========================')
print(str(exex) + '\t\t' + str(exun))
print(str(unex) + '\t\t' + str(unun))
print('Odds Ratio = ' + str(mpcc_or.oddsratio(exun, unex)) + ' (' + "{:.4f}".format(mpcc_or.lcl(exun, unex)) + ', ' + "{:.4f}".format(mpcc_or.ucl(exun, unex)) + ')')
fisherlimits = [-9.9, -9.9]
mpcc_or.fisherlimits(exex, exun, unex, unun, fisherlimits)
print('\t\t(' + "{:.4f}".format(fisherlimits[0]) + ', ' + "{:.4f}".format(fisherlimits[1]) + ')')
mcnemar = mpcc_chisq.uncorrected(exun, unex)
print('McNemar = ' + "{:.4f}".format(mcnemar) + '; p = ' + "{:.4f}".format(shared_functions.pvalfromchisq(mcnemar, 1.0)))
mcncorrected = mpcc_chisq.corrected(exun, unex)
print('Corrected = ' + "{:.4f}".format(mcncorrected) + '; p = ' + "{:.4f}".format(shared_functions.pvalfromchisq(mcncorrected, 1.0)))
fishertests = [-9.9, -9.9]
mpcc_fishertests.fishertests(exex, exun, unex, unun, fishertests)
print('\t' + "{:.6f}".format(fishertests[0]) + '\t' + "{:.6f}".format(fishertests[1]))
