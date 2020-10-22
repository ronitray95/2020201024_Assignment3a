#!/usr/bin/env python3
import re
from datetime import date
import traceback

month = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
         'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False


def checkValidDate():
    with open('date_calculator.txt', 'r') as f:
        x = f.readlines()

    x[0] = x[0].strip()
    x[1] = x[1].strip()

    dd_pat = '^[0-9]+'
    mm_pat = '[A-Za-z]{3,}|[^0-9][0-9]{1,2}[^0-9]'
    yy_pat = '[0-9]{4}$'
    try:
        dd1 = int(re.findall(dd_pat, x[0])[0].strip())
        dd2 = int(re.findall(dd_pat, x[1])[0].strip())
        mo1 = str(re.findall(mm_pat, x[0])[0]).strip()
        mo1 = mo1.lower()
        if len(mo1) > 2:
            mm1 = int(month[mo1[:3]])
        else:
            mm1 = int(mo1)
        mo2 = str(re.findall(mm_pat, x[1])[0]).strip()
        mo2 = mo2.lower()
        mo2 = ''.join(e for e in mo2 if e.isalnum())
        # print('yoyoy ', mo2)
        if len(mo2) > 2:
            mm2 = int(month[mo2[:3]])
        else:
            mm2 = int(mo2)
        yy1 = int(re.findall(yy_pat, x[0])[0].strip())
        yy2 = int(re.findall(yy_pat, x[1])[0].strip())
    except Exception as e:
        traceback.print_exc()
        print('incorrect format ', str(e))
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

    delta = date(yy2, mm2, dd2)-date(yy1, mm1, dd1)
    while yy1 < yy2 or mm1 <= mm2:
        diff += (days[mm1-1]+1 if isLeap(yy1) and mm1 == 2 else days[mm1-1])
        mm1 += 1
        if mm1 == 13:
            mm1 = 1
            yy1 = yy1+1
    days[1] = 29 if mm2 == 2 and isLeap(yy2) else 28
    diff -= (days[mm2-1]-dd2)
    print(diff)
    print(delta.days)


checkValidDate()
