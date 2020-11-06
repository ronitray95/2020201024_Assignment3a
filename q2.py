#!/usr/bin/env python3

import re
import sys

month = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
         'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False


def getDateComponents(x: str, dateFormat: str):

    dd_pat1 = '^[0-9]+'
    mm_pat2 = '[A-Za-z]{3,}|[^0-9][0-9]{1,2}[^0-9]'

    dd_pat2 = '[^0-9][0-9]{1,2}[^0-9]'
    mm_pat1 = '^[A-Za-z]{3,}|^[0-9]+'

    yy_pat = '[0-9]{4}$'
    try:
        dd1 = re.findall(dd_pat1, x)[0].strip()
        dd1 = int(''.join(e for e in dd1 if e.isalnum()))

        mo1 = str(re.findall(mm_pat2, x)[0]).strip()
        mo1 = mo1.lower()
        mo1 = ''.join(e for e in mo1 if e.isalnum())
        if len(mo1) > 2:
            mm1 = int(month[mo1[:3]])
        else:
            mm1 = int(mo1)
        yy1 = int(re.findall(yy_pat, x)[0].strip())
    except Exception as e:
        dd1 = re.findall(dd_pat2, x)[0].strip()
        dd1 = int(''.join(e for e in dd1 if e.isalnum()))
        mo1 = str(re.findall(mm_pat1, x)[0]).strip()
        mo1 = mo1.lower()
        mo1 = ''.join(e for e in mo1 if e.isalnum())
        if len(mo1) > 2:
            mm1 = int(month[mo1[:3]])
        else:
            mm1 = int(mo1)
        yy1 = int(re.findall(yy_pat, x)[0].strip())
    hasAlpha = x.upper().isupper()
    if hasAlpha == False and dateFormat != '' and (dateFormat[0]).lower() == 'm':
        dd1, mm1 = mm1, dd1
    if mm1 > 12:
        dd1, mm1 = mm1, dd1
    return [dd1, mm1, yy1]


def checkValidDate(dateFormat: str):
    with open('date_calculator.txt', 'r') as f:
        x = f.readlines()

    x[0] = x[0].strip()
    x[1] = x[1].strip()
    date1 = getDateComponents(x[0], dateFormat)
    date2 = getDateComponents(x[1], dateFormat)
    dd1, mm1, yy1 = date1[0], date1[1], date1[2]
    dd2, mm2, yy2 = date2[0], date2[1], date2[2]

    if yy2 < yy1:
        yy1, yy2 = yy2, yy1
        mm1, mm2 = mm2, mm1
        dd1, dd2 = dd2, dd1
    elif yy2 == yy1 and mm2 < mm1:
        mm1, mm2 = mm2, mm1
        dd1, dd2 = dd2, dd1
    elif yy2 == yy1 and mm2 == mm1 and dd2 < dd1:
        dd1, dd2 = dd2, dd1

    diff = -dd1

    while yy1 < yy2 or mm1 <= mm2:
        diff += (days[mm1-1]+1 if isLeap(yy1) and mm1 == 2 else days[mm1-1])
        if yy1 == yy2 and mm1 == mm2:
            break
        mm1 += 1
        if mm1 == 13:
            mm1 = 1
            yy1 = yy1+1
    days[1] = 29 if mm2 == 2 and isLeap(yy2) else 28
    diff -= (days[mm2-1]-dd2)
    f = open('output.txt', 'w')
    f.write('Date difference: '+str(diff)+' day')
    f.close()


dateFmt = ''
if len(sys.argv) > 1:
    dateFmt = (sys.argv)[1]

checkValidDate(dateFmt)
