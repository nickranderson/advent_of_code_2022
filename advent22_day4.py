# -*- coding: utf-8 -*-
import string
assignment_file = open("C:/Users/Nick Anderson/Desktop/input.txt")
assignment_list = assignment_file.read().splitlines()
assignment_file.close()

duplicated_assignments = 0

for ii in assignment_list:
    assignment = ii.split(',')
    first_elf = set(range(int(assignment[0].split('-')[0]),int(assignment[0].split('-')[1])+1))
    second_elf = set(range(int(assignment[1].split('-')[0]),int(assignment[1].split('-')[1])+1))
    overlap = first_elf.intersection(second_elf)
    if len(overlap) == 0:
        overlap = -1
    else:
        overlap = len(overlap)
    if (overlap == len(first_elf)) or (overlap == len(second_elf)):
        duplicated_assignments += 1
        
print(duplicated_assignments)

overlapped_assignments = 0
for ii in assignment_list:
    assignment = ii.split(',')
    first_elf = set(range(int(assignment[0].split('-')[0]),int(assignment[0].split('-')[1])+1))
    second_elf = set(range(int(assignment[1].split('-')[0]),int(assignment[1].split('-')[1])+1))
    overlap = first_elf.intersection(second_elf)
    if len(overlap):
        overlapped_assignments += 1
        
print(overlapped_assignments)