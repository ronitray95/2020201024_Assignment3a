#!/usr/bin/env python3

import json
import datetime


def parseFile(file_name):
    with open(file_name, 'r') as f:
        x = f.readlines()
    s = ''
    for a in x:
        s = (s + a).strip()
    ex = eval(s)
    return ex


def getOverlap(a1: list, a2: list, minToAdd: float):
    for i in range(0, len(a1)):
        for j in range(0, len(a2)):
            # if max(a1[i][0], a2[j][0]) <= min(a1[i][1], a2[j][1]):
            latest_start = max(a1[i][0], a2[j][0])
            earliest_end = min(a1[i][1], a2[j][1])
            timeDiff = (earliest_end-latest_start).seconds / 60
            if earliest_end > latest_start and timeDiff >= minToAdd:
                x = latest_start+datetime.timedelta(days=0, minutes=minToAdd)
                #print(latest_start, earliest_end, timeDiff, sep='\t')
                return str(latest_start.strftime('%-I:%M%p') + ' - ' + x.strftime('%-I:%M%p'))
    return 'Slot not available'


e1 = parseFile('Employee1.txt')
e2 = parseFile('Employee2.txt')
e1_name, e2_name = '', ''
meet_date = ''
e1_free, e2_free = [], []
for a in e1:
    e1_name = a
for a in e2:
    e2_name = a
for a in e1[e1_name]:
    meet_date = a

e1_occupied = (e1[e1_name])[meet_date]
e2_occupied = (e2[e2_name])[meet_date]

e1occ, e2occ = [], []
for d in e1_occupied:
    times = d.split('-')
    start = datetime.datetime.strptime(times[0].strip(), '%I:%M%p')
    finish = datetime.datetime.strptime(times[1].strip(), '%I:%M%p')
    e1occ.append([start, finish])

for d in e2_occupied:
    times = d.split('-')
    start = datetime.datetime.strptime(times[0].strip(), '%I:%M%p')
    finish = datetime.datetime.strptime(times[1].strip(), '%I:%M%p')
    e2occ.append([start, finish])

shiftStart = datetime.datetime(year=1900, month=1, day=1, hour=9)
shiftEnd = datetime.datetime(year=1900, month=1, day=1, hour=17, minute=0)

if e1occ[0][0] != shiftStart:
    e1_free.append([shiftStart, e1occ[0][0]])
for i in range(0, len(e1occ)-1):
    if e1occ[i][1] != e1occ[i+1][0]:
        e1_free.append([e1occ[i][1], e1occ[i+1][0]])

if e1occ[len(e1occ)-1][1] != shiftEnd:
    e1_free.append([e1occ[len(e1occ)-1][1], shiftEnd])

if e2occ[0][0] != shiftStart:
    e2_free.append([shiftStart, e2occ[0][0]])
for i in range(0, len(e2occ)-1):
    if e2occ[i][1] != e2occ[i+1][0]:
        e2_free.append([e2occ[i][1], e2occ[i+1][0]])

if e2occ[len(e2occ)-1][1] != shiftEnd:
    e2_free.append([e2occ[len(e2occ)-1][1], shiftEnd])

e1_free_fmt, e2_free_fmt = [], []
for x in e1_free:
    e1_free_fmt.append(x[0].strftime(
        '%-I:%M%p') + ' - '+x[1].strftime('%-I:%M%p'))
for x in e2_free:
    e2_free_fmt.append(x[0].strftime(
        '%-I:%M%p') + ' - '+x[1].strftime('%-I:%M%p'))

print('Available slot\n'+e1_name, ':', e1_free_fmt,
      '\n'+e2_name, ':', e2_free_fmt, sep=' ')
slot = float(input('Enter slot duration: '))
slot = float(slot)*60
freeSlot = {}
freeSlot[meet_date] = getOverlap(e1_free, e2_free, minToAdd=slot)
print(freeSlot)
