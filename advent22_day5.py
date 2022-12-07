# -*- coding: utf-8 -*-
import string
import copy
box_file = open("C:/Users/Nick Anderson/Desktop/input.txt")
box_list = box_file.read().splitlines()
box_file.close()

locations = range(1,len(box_list[0]),4)
locations = [locations[i] for i in range(len(locations))]
box_scheme = [[] for ii in range(0,len(locations))]
for row in range(7,-1,-1):
    current_level = box_list[row]
    for column in range(0,len(locations)):
        box_scheme[column].append(current_level[locations[column]])

for ii in range(0,len(box_scheme)):
    while ' ' in box_scheme[ii]:
        box_scheme[ii].remove(' ')

original_box_scheme = copy.deepcopy(box_scheme)

# CRATEMOVER 9000
for row in range(10,len(box_list)):
    row_list = box_list[row].split()
    move_num = int(row_list[1])
    donor = int(row_list[3]) - 1
    acceptor = int(row_list[5]) - 1
    for num in range(0,move_num):
        hold = box_scheme[donor].pop()
        box_scheme[acceptor].append(hold)

print('Cratemover 9000:')      
for ii in range(0,len(box_scheme)): print(box_scheme[ii].pop())

#CRATEMOVER 9001
box_scheme = copy.deepcopy(original_box_scheme)
for row in range(10,len(box_list)):
    row_list = box_list[row].split()
    move_num = int(row_list[1])
    donor = int(row_list[3]) - 1
    acceptor = int(row_list[5]) - 1
    hold = []
    for num in range(0,move_num):
        hold.insert(0,box_scheme[donor].pop())
    box_scheme[acceptor].extend(hold)
        
print('Cratemover 9001:')
for ii in range(0,len(box_scheme)): print(box_scheme[ii].pop())