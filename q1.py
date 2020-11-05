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
#print(emp, emp_lvl)
emp_id = input('Enter employee IDs (space separated) ').split(' ')
e1, e2 = emp_id[0], emp_id[1]
output = ''
common_leader = ''
i = 1
while i < len(emp_id):
    e1 = emp_id[0]
    e2 = emp_id[i]
    while True:
        if (e1 not in emp or e2 not in emp) or (emp[e1] == 'X' or emp[e2] == 'X'):
            common_leader = 'No common leader'
            output = common_leader
            break
        if emp[e1] == emp[e2]:
            common_leader = emp[e1] if common_leader == '' or emp_lvl[emp[e1]
                                                                      ] < emp_lvl[common_leader] else common_leader
            break
        elif emp_lvl[e1] > emp_lvl[e2]:
            e1 = emp[e1]
        elif emp_lvl[e1] < emp_lvl[e2]:
            e2 = emp[e2]
        else:
            e1 = emp[e1]
            e2 = emp[e2]
    i += 1
if output != 'No common leader':
    for e in emp_id:
        output = output+'\n'+common_leader+' is ' + \
            str(emp_lvl[e]-emp_lvl[common_leader]) + ' levels above ' + e
    output = common_leader+output
# print(common_leader)
f = open('output.txt', 'w')
f.write(output)
f.close()
