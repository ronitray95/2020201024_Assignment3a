#!/usr/bin/env python3

import json
import datetime
import os


def parseFile(file_name):
    with open(file_name, 'r') as f:
        x = f.readlines()
    s = ''
    for a in x:
        s = (s + a).strip()
    ex = eval(s)
    return ex


def getAllFreeSlots(a1: list, a2: list):
    newlist = []
    for i in range(0, len(a1)):
        for j in range(0, len(a2)):
            # if max(a1[i][0], a2[j][0]) <= min(a1[i][1], a2[j][1]):
            latest_start = max(a1[i][0], a2[j][0])
            earliest_end = min(a1[i][1], a2[j][1])
            if earliest_end > latest_start:
                newlist.append([latest_start, earliest_end])
    return newlist


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


ptr = 1
output = 'Available slot\n'
freeSlotAllEmp = []
meet_date = ''
while os.path.exists('Employee'+str(ptr)+'.txt') == True:
    e1 = parseFile('Employee'+str(ptr)+'.txt')
    ptr += 1
    e1_name = ''
    e1_free = []
    for a in e1:
        e1_name = a
    for a in e1[e1_name]:
        meet_date = a

    e1_occupied = (e1[e1_name])[meet_date]

    e1occ = []
    for d in e1_occupied:
        times = d.split('-')
        start = datetime.datetime.strptime(times[0].strip(), '%I:%M%p')
        finish = datetime.datetime.strptime(times[1].strip(), '%I:%M%p')
        e1occ.append([start, finish])

    shiftStart = datetime.datetime(year=1900, month=1, day=1, hour=9)
    shiftEnd = datetime.datetime(year=1900, month=1, day=1, hour=17, minute=0)

    if e1occ[0][0] != shiftStart:
        e1_free.append([shiftStart, e1occ[0][0]])
    for i in range(0, len(e1occ)-1):
        if e1occ[i][1] != e1occ[i+1][0]:
            e1_free.append([e1occ[i][1], e1occ[i+1][0]])

    if e1occ[len(e1occ)-1][1] != shiftEnd:
        e1_free.append([e1occ[len(e1occ)-1][1], shiftEnd])

    e1_free_fmt = []
    freeSlotAllEmp.append(e1_free)
    for x in e1_free:
        e1_free_fmt.append(x[0].strftime('%-I:%M%p') +
                           ' - '+x[1].strftime('%-I:%M%p'))
    output = output + e1_name + ' : ' + str(e1_free_fmt) + '\n'

ptr -= 1
slot = float(input('Enter slot duration (in hour): '))


freeSlot = {}
temp = getAllFreeSlots(freeSlotAllEmp[0], freeSlotAllEmp[1])
for i in range(2, ptr):
    temp = getAllFreeSlots(temp, freeSlotAllEmp[i])

for tt in temp:
    timeDiff = (tt[1]-tt[0]).seconds / 60
    if timeDiff >= slot*60:
        x = tt[0]+datetime.timedelta(days=0, minutes=slot*60)
        freeSlot[meet_date] = str(tt[0].strftime(
            '%-I:%M%p') + ' - ' + x.strftime('%-I:%M%p'))
        break
#freeSlot[meet_date] = getOverlap(e1_free, e2_free, minToAdd=float(slot)*60)
if meet_date not in freeSlot:
    freeSlot[meet_date] = 'Slot not available'

f = open('output.txt', 'w')
f.write(output+'\n'+'Slot duration: '+str(slot)+' hour\n'+str(freeSlot))
f.close()
