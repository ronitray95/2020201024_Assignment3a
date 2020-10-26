#!/usr/bin/env python3

import json


def parseFile(file_name):
    with open(file_name, 'r') as f:
        x = f.readlines()
    s = ''
    for a in x:
        s = (s + a).strip()
    ex = eval(s)
    return ex


org_map = parseFile('org.json')
emp, emp_lvl = {}, {}
for lvl in org_map:
    for emp_list in org_map[lvl]:
        try:
            emp[emp_list['name']] = emp_list['parent']
        except Exception:
            emp[emp_list['name']] = 'X'
        emp_lvl[emp_list['name']] = int(lvl[1:])
print(emp, emp_lvl)
emp_id = input('Enter 2 employee ID (space separated) ').split(' ')
e1, e2 = emp_id[0], emp_id[1]
while True:
    if e1 not in emp or e2 not in emp:
        print('No common leader')
        break
    if emp[e1] == emp[e2]:
        print(emp[e1]+'\n', emp_id[0], 'is', emp_lvl[emp_id[0]]-emp_lvl[emp[e1]], 'levels below\n',
              emp_id[1], 'is', emp_lvl[emp_id[1]]-emp_lvl[emp[e1]], 'levels below', sep=' ')
        break
    elif emp_lvl[e1] > emp_lvl[e2]:
        e1 = emp[e1]
    elif emp_lvl[e1] < emp_lvl[e2]:
        e2 = emp[e2]
    else:
        e1 = emp[e1]
        e2 = emp[e2]
