import os
import pickle

with open(os.getcwd()+'\groups.csv', 'rb') as file:
    data = pickle.load(file)
for groupe in data:
    print(f'Grade: {groupe}')
    print()
    for coding_l in data[groupe]:
        print(f'Coding language: {coding_l}')
        for student in data[groupe][coding_l]:
            print(student)
        print()