# -*- coding: utf-8 -*-
elf_calorie_file = open("C:/Users/Nick Anderson/Desktop/input.txt",)
elf_calorie_list = elf_calorie_file.readlines()

max_elf = 0
current_elf = 0
top_three_elves = [0,0,0]

for ii in range(len(elf_calorie_list)):
    current_line = elf_calorie_list[ii]
#    print(ii," ",current_line)
    if current_line == '\n':
        if max_elf < current_elf:
            max_elf = current_elf
        if current_elf > min(top_three_elves):
            top_three_elves[top_three_elves.index(min(top_three_elves))] = current_elf
        current_elf = 0
    else:
        current_elf = current_elf + int(current_line)

print(max_elf)
print(sum(top_three_elves))