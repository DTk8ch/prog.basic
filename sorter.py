import pickle
import os

students = []
groups = {}
with open(os.getcwd()+"/data.csv", 'r') as file:
    next(file)
    for l in file:
        l = l.split(', ')
        students.append(l)
        if l[3] not in groups:
            groups[l[3]] = {}
        if l[5].replace('\n', '') not in groups[l[3]]:
            groups[l[3]][l[5].replace('\n', '')] = []

for student in students:
    groups[student[3]][student[5].replace('\n', '')].append([student[1],student[2],student[4]])


with open(os.getcwd()+'/groups.csv', 'wb') as file:
    students = pickle.dump(groups,file)